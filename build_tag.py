class Tag(object):
    def __init__(self, subset='all'):
        self.static_tags = self.__load_static_tags(subset=subset)
        self.id2tags = self.__load_id2tags()
        self.tags2id = self.__load_tags2id()

    def array2tags(self, array):
        tags = []
        for id in array:
            tags.append(self.id2tags[id])
        return tags

    def tags2array(self, tags):
        array = []
        for tag in self.static_tags:
            if tag in tags:
                array.append(1)
            else:
                array.append(0)
        return array

    def inv_tags2array(self, array):
        tags = []
        for i, value in enumerate(array):
            if value != 0:
                tags.append(self.id2tags[i])
        return tags

    def __load_id2tags(self):
        id2tags = {}
        for i, tag in enumerate(self.static_tags):
            id2tags[i] = tag
        return id2tags

    def __load_tags2id(self):
        tags2id = {}
        for i, tag in enumerate(self.static_tags):
            tags2id[tag] = i
        return tags2id

    def __load_static_tags(self, subset='all'):
        if subset == 'all':
            static_tags_name = ['abdomen', 'abnormal', 'acute', 'adipose tissue', 'airspace disease', 'anterior', 'aorta', 
                                'aortic aneurysm', 'aortic valve', 'apex', 'arthritis', 'atherosclerosis', 'azygos lobe', 
                                'base', 'bilateral', 'blister', 'blood vessels', 'blunted', 'bone', 'bone and bones', 
                                'bone diseases', 'borderline', 'breast', 'breast implants', 'bronchi', 'bronchiectasis', 
                                'bronchiolitis', 'bronchitis', 'bronchovascular', 'bullous emphysema', 'calcified granuloma', 
                                'calcinosis', 'cardiac shadow', 'cardiomegaly', 'cardiophrenic angle', 'carina', 'catheters', 
                                'cavitation', 'cervical vertebrae', 'cholelithiasis', 'chronic', 'chronic obstructive', 'cicatrix', 
                                'clavicle', 'colonic interposition', 'consolidation', 'contrast media', 'coronary vessels', 
                                'costophrenic angle', 'cystic fibrosis', 'cysts', 'deformity', 'degenerative', 'density', 
                                'diaphragm', 'diaphragmatic', 'diaphragmatic eventration', 'diffuse', 'diffuse idiopathic skeletal', 
                                'dislocations', 'elevated', 'emphysema', 'enlarged', 'epicardial fat', 'esophagus', 'expansile bone lesions', 
                                'fibrosis', 'flattened', 'focal', 'foreign bodies', 'fractures', 'funnel chest', 'granuloma', 
                                'granulomatous disease', 'healed', 'heart', 'heart atria', 'heart failure', 'heart ventricles', 
                                'hemopneumothorax', 'hemothorax', 'hernia', 'hiatal', 'hilum', 'humerus', 'hydropneumothorax', 'hyperdistention', 
                                'hyperlucent', 'hyperostosis', 'hypertension', 'hypoinflation', 'hypovolemia', 'implanted medical device', 
                                'indwelling', 'infiltrate', 'inserted', 'interstitial', 'irregular', 'kyphosis', 'large', 'left', 'lingula', 
                                'lower lobe', 'lucency', 'lumbar vertebrae', 'lung', 'lung diseases', 'lymph nodes', 'markings', 'mass', 'mastectomy', 
                                'mediastinum', 'medical device', 'metabolic', 'middle lobe', 'mild', 'mitral valve', 'moderate', 'multilobar', 'multiple', 
                                'neck', 'nipple shadow', 'no indexing', 'nodule', 'normal', 'obscured', 'opacity', 'osteophyte', 'osteoporosis', 
                                'paratracheal', 'patchy', 'pectus carinatum', 'pericardial effusion', 'pleura', 'pleural effusion', 'pleural sinus', 
                                'pneumonectomy', 'pneumonia', 'pneumoperitoneum', 'pneumothorax', 'posterior', 'prominent', 'pulmonary', 'pulmonary alveoli', 
                                'pulmonary artery', 'pulmonary atelectasis', 'pulmonary congestion', 'pulmonary disease', 'pulmonary edema', 
                                'pulmonary emphysema', 'pulmonary fibrosis', 'reticular', 'retrocardiac', 'ribs', 'right', 'round', 'sarcoidosis', 
                                'scattered', 'sclerosis', 'scoliosis', 'severe', 'shift', 'shoulder', 'small', 'spinal fusion', 'spine', 'spondylosis', 
                                'stents', 'sternum', 'streaky', 'subcutaneous  emphysema', 'subcutaneous emphysema', 'sulcus', 'supracardiac', 
                                'surgical instruments', 'sutures', 'technical quality of image unsatisfactory', 'thickening', 'thoracic', 'thoracic vertebrae', 
                                'thorax', 'tortuous', 'trachea', 'tube', 'tuberculosis', 'upper lobe', 'volume loss']
        elif subset == 'pulmonary':                
            static_tags_name = ['normal', 'pulmonary', 'pulmonary alveoli', 
                                'pulmonary artery', 'pulmonary atelectasis', 'pulmonary congestion', 
                                'pulmonary disease', 'pulmonary edema', 'pulmonary emphysema', 'pulmonary fibrosis']

        return static_tags_name
