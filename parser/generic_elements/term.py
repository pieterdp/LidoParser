from ..xml_parser import GenericXMLParser
from .leaf import GenericLeafNode


class GenericTerm(GenericXMLParser):
    """
    Many nodes in LIDO are a 'term' and consist of two child elements (GenericLeafNodes)
        conceptID
        term
    Attributes:
        type
    """
    def __init__(self, xml_node):
        self.xml_node = xml_node
        self.attributes = self.get_attributes_as_dict(self.xml_node)
        self.type = self.get_attribute('type')
        self.conceptID = self.get_concept_id()
        self.term = self.get_term()

    def get_attribute(self, attribute):
        return self.get_attribute_from_dict(attribute=attribute, attributes=self.attributes)

    def get_concept_id(self):
        return self.repeatable_node(self.xml_node, 'lido:conceptID', GenericLeafNode)

    def get_term(self):
        return self.repeatable_node(self.xml_node, 'lido:term', GenericLeafNode)
