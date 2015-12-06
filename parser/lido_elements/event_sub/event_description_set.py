from . import GenericXMLParser, GenericLeafNode


class EventDescriptionSet(GenericXMLParser):
    def __init__(self, xml_event_description_set):
        self.xml_event_description_set = xml_event_description_set
        self.attributes = self.get_attributes_as_dict(self.xml_event_description_set)
        self.type = self.get_attribute_from_dict('type', self.attributes)
        self.sortorder = self.get_attribute_from_dict('sortorder', self.attributes)
        self.descriptiveNoteID = self.get_descriptive_note_id()
        self.descriptiveNoteValue = self.get_descriptive_note_value()
        self.sourceDescriptiveNote = self.get_source_descriptive_note()

    def get_descriptive_note_id(self):
        return self.repeatable_node(self.xml_event_description_set, 'lido:descriptiveNoteID', GenericLeafNode)

    def get_descriptive_note_value(self):
        return self.repeatable_node(self.xml_event_description_set, 'lido:descriptiveNoteValue', GenericLeafNode)

    def get_source_descriptive_note(self):
        return self.repeatable_node(self.xml_event_description_set, 'lido:sourceDescriptiveNote', GenericLeafNode)
