from ..xml_parser import ParseError
from . import GenericXMLParser
from .object_classification_sub.object_work_type import ObjectWorkTypeWrap
from .object_classification_sub.classification import ClassificationWrap


class ObjectClassificationWrap(GenericXMLParser):
    def __init__(self, object_classification_xml):
        self.object_classification_xml = object_classification_xml
        self.objectWorkTypeWrap = self.get_object_work_type_wrap()
        self.classificationWrap = self.get_classification_wrap()

    def get_object_work_type_wrap(self):
        return self.single_optional_node(self.object_classification_xml, 'lido:objectWorkTypeWrap', ObjectWorkTypeWrap)

    def get_classification_wrap(self):
        return self.single_optional_node(self.object_classification_xml, 'lido:classificationWrap', ClassificationWrap)
