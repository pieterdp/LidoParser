from . import GenericXMLParser, GenericLeafNode, GenericTerm


class MaterialsTech(GenericXMLParser):
    def __init__(self, xml_materials_tech):
        self.xml_materials_tech = xml_materials_tech
        self.termMaterialsTech = self.get_term_materials_tech()
        self.extentMaterialsTech = self.get_extent_materials_tech()
        self.sourceMaterialsTech = self.get_source_materials_tech()

    def get_term_materials_tech(self):
        return self.repeatable_node(self.xml_materials_tech, 'lido:termMaterialsTech', GenericTerm)

    def get_extent_materials_tech(self):
        return self.repeatable_node(self.xml_materials_tech, 'lido:extentMaterialsTech', GenericLeafNode)

    def get_source_materials_tech(self):
        return self.repeatable_node(self.xml_materials_tech, 'lido:sourceMaterialsTech', GenericLeafNode)


class EventMaterialsTech(GenericXMLParser):
    def __init__(self, xml_event_materials_tech):
        self.xml_event_materials_tech = xml_event_materials_tech
        self.attributes = self.get_attributes_as_dict(self.xml_event_materials_tech)
        self.sortorder = self.get_attribute_from_dict('sortorder', self.attributes)
        self.displayMaterialsTech = self.get_display_materials_tech()
        self.materialsTech = self.get_materials_tech()

    def get_display_materials_tech(self):
        return self.repeatable_node(self.xml_event_materials_tech, 'lido:displayMaterialsTech', GenericLeafNode)

    def get_materials_tech(self):
        return self.single_optional_node(self.xml_event_materials_tech, 'lido:materialsTech', MaterialsTech)
