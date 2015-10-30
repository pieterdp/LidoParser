from . import GenericXMLParser, GenericTerm


class ClassificationWrap(GenericXMLParser):
    def __init__(self, xml_classification_wrap):
        self.xml_classification_wrap = xml_classification_wrap
        self.classification = self.get_classification()

    def get_classification(self):
        return self.repeatable_node(self.xml_classification_wrap, 'lido:classification', GenericTerm)
