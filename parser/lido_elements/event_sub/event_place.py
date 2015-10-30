from . import GenericNameSet, GenericXMLParser, GenericLeafNode, GenericTerm


class GML(GenericXMLParser):
    def __init__(self, xml_gml):
        self.xml_gml = xml_gml
        self.attributes = self.get_attributes_as_dict(self.xml_gml)
        self.lang = self.get_attribute_from_dict('xml:lang', self.xml_gml)
        self.Point = self.get_point()
        self.LineString = self.get_line_string()
        self.Polygon = self.get_polygon()

    def get_point(self):
        pass

    def get_line_string(self):
        pass

    def get_polygon(self):
        pass


class Place(GenericXMLParser):
    def __init__(self, xml_place):
        self.xml_place = xml_place
        self.attributes = self.get_attributes_as_dict(self.xml_place)
        self.politicalEntity = self.get_attribute('politicalEntity')
        self.geographicalEntity = self.get_attribute('geographicalEntity')
        self.placeID = self.get_place_ids()
        self.namePlaceSet = self.get_name_place_sets()
        self.gml = self.get_gml()
        self.partOfPlace = self.get_part_of_place()
        self.placeClassification = self.get_place_classification()

    def get_attribute(self, attribute):
        return self.get_attribute_from_dict(attribute, self.attributes)

    def get_place_ids(self):
        return self.repeatable_node(self.xml_place, 'lido:placeID', GenericLeafNode)

    def get_name_place_sets(self):
        return self.repeatable_node(self.xml_place, 'lido:namePlaceSet', GenericNameSet)

    def get_part_of_place(self):
        return self.repeatable_node(self.xml_place, 'lido:partOfPlace', Place)

    def get_gml(self):
        print("Warning: GML is not implemented (yet)")
        return self.repeatable_node(self.xml_place, 'gml', GML)

    def get_place_classification(self):
        return self.repeatable_node(self.xml_place, 'lido:placeClassification', GenericTerm)


class EventPlace(GenericXMLParser):
    def __init__(self, xml_event_place):
        self.xml_event_place = xml_event_place
        self.attributes = self.get_attributes_as_dict(self.xml_event_place)
        self.type = self.get_attribute('type')
        self.sortorder = self.get_attribute('sortorder')
        self.displayPlace = self.get_display_place()
        self.place = self.get_place()

    def get_attribute(self, attribute):
        return self.get_attribute_from_dict(attribute, self.attributes)

    def get_display_place(self):
        return self.repeatable_node(self.xml_event_place, 'lido:displayPlace', GenericNameSet)

    def get_place(self):
        places = self.xpath(self.xml_event_place, 'lido:place')
        return [Place(places.pop())]
