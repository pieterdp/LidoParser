from ..xml_parser import ParseError
from . import GenericLeafNode, GenericXMLParser, GenericNameSet, GenericTerm
from .event_sub.event_place import EventPlace
from .event_sub.event_date import EventDate
from .event_sub.event_actor import EventActor
from .event_sub.event_materials_tech import EventMaterialsTech
from .event_sub.thing_present import ThingPresent


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
        return self.repeatable_node(self.xml_event, 'lido:culture', GenericTerm)

    def get_event_date(self):
        return self.single_optional_node(self.xml_event, 'lido:eventDate', EventDate)

    def get_period_name(self):
        return self.repeatable_node(self.xml_event, 'lido:periodName', GenericTerm)

    def get_event_places(self):
        return self.repeatable_node(self.xml_event, 'lido:eventPlace', EventPlace)

    def get_event_method(self):
        return self.repeatable_node(self.xml_event, 'lido:eventMethod', GenericTerm)

    def get_event_materials_tech(self):
        return self.repeatable_node(self.xml_event, 'lido:eventMaterialsTech', EventMaterialsTech)

    def get_thing_present(self):
        return self.repeatable_node(self.xml_event, 'lido:thingPresent', ThingPresent)

    def get_related_event_set(self):
        return self.repeatable_node(self.xml_event, 'lido:relatedEventSet', RelatedEventSet)

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
        return self.single_required_node(self.xml_event_set, 'lido:event', Event)

    def get_display_events(self):
        return self.repeatable_node(self.xml_event_set, 'lido:displayEvent', GenericLeafNode)


class RelatedEventSet(GenericXMLParser):
    def __init__(self, xml_related_event_set):
        self.xml_related_event_set = xml_related_event_set
        self.attributes = self.get_attributes_as_dict(self.xml_related_event_set)
        self.sortorder = self.get_attribute_from_dict('sortorder', self.attributes)
        self.relatedEvent = self.get_related_event()
        self.relatedEventRelType = self.get_related_event_rel_type()

    def get_related_event(self):
        return self.single_optional_node(self.xml_related_event_set, 'lido:relatedEvent', RelatedEvent)

    def get_related_event_rel_type(self):
        return self.single_optional_node(self.xml_related_event_set, 'lido:relatedEventRelType', GenericTerm)


class RelatedEvent(GenericXMLParser):
    def __init__(self, xml_related_event):
        self.xml_related_event = xml_related_event
        self.displayEvent = self.get_display_event()
        self.event = self.get_event()

    def get_display_event(self):
        return self.repeatable_node(self.xml_related_event, 'lido:displayEvent', GenericLeafNode)

    def get_event(self):
        return self.single_required_node(self.xml_related_event, 'lido:event', Event)


class EventWrap(GenericXMLParser):
    def __init__(self, xml_event_wrap):
        self.xml_event_wrap = xml_event_wrap
        self.eventSet = self.get_event_set()

    def get_event_set(self):
        return self.repeatable_node(self.xml_event_wrap, 'lido:eventSet', EventSet)
