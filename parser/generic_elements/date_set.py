from ..xml_parser import GenericXMLParser
from .leaf import GenericLeafNode


class GenericDateSet(GenericXMLParser):
    def __init__(self, xml_date):
        self.xml_date = xml_date
        self.earliestDate = self.get_earliest_date()
        self.latestDate = self.get_latest_date()

    def get_earliest_date(self):
        return self.single_optional_node(self.xml_date, 'lido:earliestDate', GenericLeafNode)

    def get_latest_date(self):
        return self.single_optional_node(self.xml_date, 'lido:latestDate', GenericLeafNode)
