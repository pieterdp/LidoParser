from . import GenericXMLParser, GenericLeafNode
from ..generic_sub.lido_object import LidoObject


class ThingPresent(GenericXMLParser):
    def __init__(self, xml_thing_present):
        self.xml_thing_present = xml_thing_present
        self.attributes = self.get_attributes_as_dict(self.xml_thing_present)
        self.sortorder = self.get_attribute_from_dict('sortorder', self.attributes)
        self.displayObject = self.get_display_object()
        self.object = self.get_object()

    def get_display_object(self):
        return self.repeatable_node(self.xml_thing_present, 'lido:displayObject', GenericLeafNode)

    def get_object(self):
        return self.single_optional_node(self.xml_thing_present, 'lido:object', LidoObject)

