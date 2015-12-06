from ..xml_parser import ParseError
from . import GenericXMLParser
from .object_identification_sub.title import TitleWrap
from .object_identification_sub.inscription import InscriptionsWrap


class ObjectIdentificationWrap(GenericXMLParser):
    def __init__(self, object_identification_xml):
        """
        Title or Object Name Wrapper (titleWrap)
(contents listed below)
Inscriptions and other Marks Wrapper (inscriptionsWrap)
(contents listed below)
Custody/Repository Location (Wrapper) (repositoryWrap)
(contents listed below)
Display State/Edition Wrapper (displayStateEditionWrap)
(contents listed below)
Object Description/Descriptive Note Wrapper (objectDescriptionWrap)
(contents listed below)
Object Measurements Wrapper (objectMeasurementsWrap)
(contents listed below)
        :param object_identification_xml:
        :return:
        """
        self.object_identficiation_xml = object_identification_xml
        self.titleWrap = self.get_title_wrap()
        self.inscriptionsWrap = self.get_inscriptions_wrap()
        self.repositoryWrap = self.get_repository_wrap()
        self.displayStateEditionWrap = self.get_display_state_edition_wrap()
        self.objectDescriptionWrap = self.get_object_description_wrap()
        self.objectMeasurementsWrap = self.get_object_measurements_wrap()

    def get_title_wrap(self):
        return self.single_required_node(self.object_identficiation_xml, 'lido:titleWrap', TitleWrap)

    def get_inscriptions_wrap(self):
        return self.single_optional_node(self.object_identficiation_xml, 'lido:inscriptionsWrap', InscriptionsWrap)
