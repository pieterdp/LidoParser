from . import GenericXMLParser


class EventDescriptionSet(GenericXMLParser):
    def __init__(self, xml_event_description_set):
        self.xml_event_description_set = xml_event_description_set
        self.attributes = self.get_attributes_as_dict(self.xml_event_description_set)
        self.type = self.get_attribute_from_dict('type', self.attributes)
        self.sortorder = self.get_attribute_from_dict('sortorder', self.attributes)
