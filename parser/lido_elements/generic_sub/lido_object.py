from . import GenericLeafNode, GenericXMLParser


class ObjectWebResource(GenericXMLParser):
    def __init__(self, xml_object_web_resource):
        self.xml_object_web_resource = xml_object_web_resource
        self.attributes = self.get_attributes_as_dict(self.xml_object_web_resource)
        self.pref = self.get_attribute('pref')
        self.formatResource = self.get_attribute('formatResource')
        self.lang = self.get_attribute('xml:lang')
        self.encodinganalog = self.get_attribute('encodinganalog')
        self.label = self.get_attribute('label')

    def get_attribute(self, attribute):
        return self.get_attribute_from_dict(attribute, self.attributes)


class LidoObject(GenericXMLParser):
    def __init__(self, xml_object):
        self.xml_object = xml_object
        self.objectWebResource = self.get_object_web_resource()
        self.objectID = self.get_object_id()
        self.objectNote = self.get_object_note()

    def get_object_web_resource(self):
        return self.repeatable_node(self.xml_object, 'lido:objectWebResource', ObjectWebResource)

    def get_object_id(self):
        return self.repeatable_node(self.xml_object, 'lido:objectID', GenericLeafNode)

    def get_object_note(self):
        return self.repeatable_node(self.xml_object, 'lido:objectNote', GenericLeafNode)
