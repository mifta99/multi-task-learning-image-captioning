import tensorflow as tf
import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt
import torch  # Import PyTorch to handle tensor conversions

class Logger(object):
    def __init__(self, log_dir):
        """Create a summary writer logging to log_dir."""
        self.writer = tf.summary.create_file_writer(log_dir)

    def scalar_summary(self, tag, value, step): # only this function that is called in the trainer
        """Log a scalar variable."""
        # Convert PyTorch tensors to CPU scalars or NumPy arrays
        if torch.is_tensor(value):
            value = value.cpu().item()  # Convert to a Python scalar
        with self.writer.as_default():
            tf.summary.scalar(tag, value, step=step)
            self.writer.flush() # Flush the writer to write the data to disk

    def image_summary(self, tag, images, step): # not called in the trainer
        """Log a list of images."""
        with self.writer.as_default():
            for i, img in enumerate(images):
                # Convert PyTorch tensors to NumPy arrays
                if torch.is_tensor(img):
                    img = img.cpu().numpy()
                buffer = BytesIO()
                plt.imsave(buffer, img, format="png")
                buffer.seek(0)
                tf.summary.image(f"{tag}/{i}", 
                                 tf.convert_to_tensor(np.array([img])), 
                                 step=step)
                buffer.close()

    def histo_summary(self, tag, values, step, bins=1000): # not called in the trainer
        """Log a histogram of the tensor of values."""
        # Convert PyTorch tensors to NumPy arrays
        if torch.is_tensor(values):
            values = values.cpu().numpy()
        with self.writer.as_default():
            tf.summary.histogram(tag, values, step=step)
