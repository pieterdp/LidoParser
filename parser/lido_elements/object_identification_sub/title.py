from . import GenericXMLParser, GenericNameSet


class TitleWrap(GenericXMLParser):
    def __init__(self, title_wrap_xml):
        self.title_wrap_xml = title_wrap_xml
        self.titleSet = self.get_title_set()

    def get_title_set(self):
        return self.repeatable_node(self.title_wrap_xml, 'lido:titleSet', GenericNameSet, required=True)
