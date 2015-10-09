from . import GenericXMLParser, GenericLeafNode, GenericTerm, GenericNameSet, GenericDateSet


class LActor(GenericXMLParser):
    def __init__(self, xml_actor):
        self.xml_actor = xml_actor
        self.attributes = self.get_attributes_as_dict(self.xml_actor)
        self.type = self.get_attribute_from_dict('type', self.attributes)
        self.actorID = self.get_actor_id()
        self.nameActorSet = self.get_name_actor_set()
        self.nationalityActor = self.get_nationality_actor()
        self.vitalDatesActor = self.get_vital_dates_actor()
        self.genderActor = self.get_gender_actor()

    def get_actor_id(self):
        return self.repeatable_node(self.xml_actor, 'lido:actorID', GenericLeafNode)

    def get_name_actor_set(self):
        return self.repeatable_node(self.xml_actor, 'lido:nameActorSet', GenericNameSet, required=True)

    def get_nationality_actor(self):
        return self.repeatable_node(self.xml_actor, 'lido:nationalityActor', GenericTerm)

    def get_vital_dates_actor(self):
        return self.single_optional_node(self.xml_actor, 'lido:vitalDatesActor', GenericDateSet)

    def get_gender_actor(self):
        return self.repeatable_node(self.xml_actor, 'lido:genderActor', GenericLeafNode)


class ActorInRole(GenericXMLParser):
    def __init__(self, xml_actor_in_role):
        self.xml_actor_in_role = xml_actor_in_role
        self.actor = self.get_actor()
        self.roleActor = self.get_role_actor()
        self.attributionQualifierActor = self.get_attribution_qualifier_actor()
        self.extentActor = self.get_extent_actor()

    def get_actor(self):
        return self.single_optional_node(self.xml_actor_in_role, 'lido:actor', LActor)

    def get_role_actor(self):
        return self.repeatable_node(self.xml_actor_in_role, 'lido:roleActor', GenericTerm)

    def get_attribution_qualifier_actor(self):
        return self.repeatable_node(self.xml_actor_in_role, 'lido:attributionQualifierActor', GenericLeafNode)

    def get_extent_actor(self):
        return self.repeatable_node(self.xml_actor_in_role, 'lido:extentActor', GenericLeafNode)


class EventActor(GenericXMLParser):
    def __init__(self, xml_event_actor):
        self.xml_event_actor = xml_event_actor
        self.attributes = self.get_attributes_as_dict(self.xml_event_actor)
        self.sortorder = self.get_attribute_from_dict('sortorder', self.attributes)
        self.displayActorInRole = self.get_display_actor_in_role()
        self.actorInRole = self.get_actor_in_role()

    def get_actor_in_role(self):
        return self.single_optional_node(self.xml_event_actor, 'lido:actorInRole', ActorInRole)

    def get_display_actor_in_role(self):
        return self.repeatable_node(self.xml_event_actor, 'lido:displayActorInRole', GenericLeafNode)
