from ..xml_parser import ParseError
from . import GenericLeafNode, GenericXMLParser, GenericNameSet, GenericTerm
from .event_sub.event_place import EventPlace
from .event_sub.event_date import EventDate
from .event_sub.event_actor import EventActor


class Event(GenericXMLParser):
    def __init__(self, xml_event):
        self.xml_event = xml_event
        self.eventID = self.get_event_ids()
        self.eventType = self.get_event_type()
        self.roleInEvent = self.get_role_in_event()
        self.eventName = self.get_event_names()
        self.eventActor = self.get_event_actor()
        self.culture = self.get_culture()
        self.eventDate = self.get_event_date()
        self.periodName = self.get_period_name()
        self.eventPlace = self.get_event_places()
        self.eventMethod = self.get_event_method()
        self.eventMaterialsTech = self.get_event_materials_tech()
        self.thingPresent = self.get_thing_present()
        self.relatedEventSet = self.get_related_event_set()
        self.eventDescriptionSet = self.get_event_description_set()

    def get_event_ids(self):
        return self.repeatable_node(self.xml_event, 'lido:eventID', GenericLeafNode)

    def get_event_type(self):
        event_types = self.xpath(self.xml_event, 'lido:eventType')
        return [GenericTerm(event_types.pop())]

    def get_role_in_event(self):
        return self.repeatable_node(self.xml_event, 'lido:roleInEvent', GenericTerm)

    def get_event_names(self):
        return self.repeatable_node(self.xml_event, 'lido:eventName', GenericNameSet)

    def get_event_actor(self):
        return self.repeatable_node(self.xml_event, 'lido:eventActor', EventActor)

    def get_culture(self):
        pass

    def get_event_date(self):
        return self.single_optional_node(self.xml_event, 'lido:eventDate', EventDate)

    def get_period_name(self):
        pass

    def get_event_places(self):
        return self.repeatable_node(self.xml_event, 'lido:eventPlace', EventPlace)

    def get_event_method(self):
        pass

    def get_event_materials_tech(self):
        pass

    def get_thing_event(self):
        pass

    def get_thing_present(self):
        pass

    def get_related_event_set(self):
        pass

    def get_event_description_set(self):
        pass


class EventSet(GenericXMLParser):
    def __init__(self, xml_event_set):
        self.xml_event_set = xml_event_set
        self.displayEvent = self.get_display_events()
        self.event = self.get_event()
        self.attributes = self.get_attributes_as_dict(self.xml_event_set)
        self.sortorder = self.get_attribute('sortorder')

    def get_attribute(self, attribute):
        return self.get_attribute_from_dict(attribute, self.attributes)

    def get_event(self):
        events = self.xpath(self.xml_event_set, 'lido:event')
        if len(events) > 1:
            raise ParseError
        if len(events) < 1:
            return [None]
        return [Event(events.pop())]

    def get_display_events(self):
        xml_display_events = self.xpath(self.xml_event_set, 'lido:displayEvent')
        display_events = []
        for xml_display_event in xml_display_events:
            display_events.append(GenericLeafNode(xml_display_event))
        return display_events
