from ..xml_parser import GenericXMLParser
from .leaf import GenericLeafNode


class GenericNameSet(GenericXMLParser):
    """
    All LIDO *place-elements are created quite the same:
    they have a appellationValue subelement and a sourceAppellation subelement,
    that is a list of string elements (GenericLeafNode)
    """
    def __init__(self, xml_node):
        self.xml_node = xml_node
        # Get the attributes, but do not parse them (this can be subclassed in more specific elements)
        self.attributes = self.get_attributes_as_dict(self.xml_node)
        self.appellationValue = self.get_appellation_values()
        self.sourceAppellation = self.get_source_appellation()
        self.type = self.get_attribute_from_dict('type', self.attributes)
        self.sortorder = self.get_attribute_from_dict('sortorder', self.attributes)

    def get_appellation_values(self):
        return self.repeatable_node(self.xml_node, 'lido:appellationValue', GenericLeafNode)

    def get_source_appellation(self):
        return self.repeatable_node(self.xml_node, 'lido:sourceAppellation', GenericLeafNode)
