# -*- coding: utf-8 -*-
from ..xml_parser import GenericXMLParser


class GenericLeafNode(GenericXMLParser):
    """
    Class for a generic leaf node.
    A generic leaf node is a LIDO-node that contains a single text field (e.g. lido:lidoTerm)
    It may also contain the following attributes:
        lang
        label
        encodinganalog
        pref
        type
        source
    It is represented as string (__str__ and __repr__)
    """
    def __init__(self, xml_leaf_node):
        self.xml_leaf_node = xml_leaf_node
        self.content = self.get_content()
        # Get attributes
        self.attributes = self.get_attributes_as_dict(self.xml_leaf_node)
        self.lang = self.get_attribute('xml:lang')
        self.label = self.get_attribute('label')
        self.encodinganalog = self.get_attribute('encodinganalog')
        self.pref = self.get_attribute('pref')
        self.type = self.get_attribute('type')
        self.source = self.get_attribute('source')
        self.addedSearchTerm = self.get_attribute('addedSearchTerm')

    def get_attribute(self, attribute):
        return self.get_attribute_from_dict(attribute, self.attributes)

    def __str__(self):
        return self.content

    def __unicode__(self):
        return self.content

    def get_content(self):
        if self.xml_leaf_node.text:
            return unicode(self.xml_leaf_node.text).encode('utf-8')
        else:
            return str(None)
