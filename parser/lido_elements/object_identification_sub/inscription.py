from . import GenericXMLParser, GenericLeafNode


class InscriptionsWrap(GenericXMLParser):
    def __init__(self, inscriptions_wrap_xml):
        self.inscriptions_wrap_xml = inscriptions_wrap_xml
        self.inscriptions = self.get_inscriptions()

    def get_inscriptions(self):
        return self.repeatable_node(self.inscriptions_wrap_xml, 'lido:inscriptions', Inscriptions)


class InscriptionDescription(GenericXMLParser):
    def __init__(self, inscription_description_xml):
        self.inscription_description_xml = inscription_description_xml
        self.attributes = self.get_attributes_as_dict(self.inscription_description_xml)
        self.type = self.get_attribute_from_dict('type', self.attributes)
        self.sortorder = self.get_attribute_from_dict('sortorder', self.attributes)
        self.descriptiveNoteID = self.get_descriptive_note_id()
        self.descriptiveNoteValue = self.get_descriptive_note_value()
        self.sourceDescriptiveNote = self.get_source_descriptive_note()


class Inscriptions(GenericXMLParser):
    def __init__(self, inscriptions_xml):
        self.inscriptions_xml = inscriptions_xml
        self.attributes = self.get_attributes_as_dict(self.inscriptions_xml)
        self.type = self.get_attribute_from_dict('type', self.attributes)
        self.sortorder = self.get_attribute_from_dict('sortorder', self.attributes)
        self.inscriptionTranscription = self.get_inscription_transcription()
        self.inscriptionDescription = self.get_inscription_description()

    def get_inscription_transcription(self):
        return self.repeatable_node(self.inscriptions_xml, 'lido:inscriptionTranscription', GenericLeafNode)
