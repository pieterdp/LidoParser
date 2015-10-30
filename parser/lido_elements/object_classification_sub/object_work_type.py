from . import GenericXMLParser, GenericTerm


class ObjectWorkTypeWrap(GenericXMLParser):
    def __init__(self, xml_object_work_type_wrap):
        self.xml_object_work_type_wrap = xml_object_work_type_wrap
        self.objectWorkType = self.get_object_work_type()

    def get_object_work_type(self):
        return self.repeatable_node(self.xml_object_work_type_wrap, 'lido:objectWorkType', GenericTerm, required=True)
