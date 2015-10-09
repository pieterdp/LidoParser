from . import GenericXMLParser, GenericLeafNode, GenericDateSet


class EventDate(GenericXMLParser):
    def __init__(self, xml_event_date):
        self.xml_event_date = xml_event_date
        self.displayDate = self.get_display_date()
        self.date = self.get_date()

    def get_display_date(self):
        return self.repeatable_node(self.xml_event_date, 'lido:displayDate', GenericLeafNode)

    def get_date(self):
        return self.single_optional_node(self.xml_event_date, 'lido:date', GenericDateSet)
