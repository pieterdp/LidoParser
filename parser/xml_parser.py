

class ParseError(Exception):
    pass


class GenericXMLParser:
    """
    Generic XML Parser for LIDO parsing using lxml.etree methods.
    """
    namespaces = {'lido': 'http://www.lido-schema.org',
                  'oai': 'http://www.openarchives.org/OAI/2.0/'}

    def xpath(self, xml_object, expression):
        result = xml_object.xpath(expression, namespaces=self.namespaces)
        if type(result) != list:
            result = [result]
        return result

    def get_attributes_as_dict(self, xml_object):
        """
        Get all attributes of an XML object as a dictionary.
        :param xml_object:
        :return:
        """
        if hasattr(xml_object, 'attrib'):
            return dict(getattr(xml_object, 'attrib'))
        else:
            return {}

    def get_attribute_from_dict(self, attribute, attributes):
        """
        Given a dict containing attributes as name => value
        Return the value corresponding with attribute or None if it doesn't exist
        :param attribute:
        :param attributes:
        :return:
        """
        if attribute in attributes:
            return attributes[attribute]
        else:
            return None

    def repeatable_node(self, container, xpath_expression, node_class, required=False):
        """
        Most LIDO elements can be repeated. This function creates a list of
        repeatable nodes that have been converted to their generic_lido_parser objects.
        The object is defined by node_class (e.g. GenericLeafNode).
        If required is set to True, complain if xml_nodes is empty
        :param container:
        :param xpath_expression:
        :param node_class:
        :param required:
        :return:
        """
        xml_nodes = []
        input_nodes = self.xpath(container, xpath_expression)
        for input_node in input_nodes:
            xml_nodes.append(node_class(input_node))
        if required == True and len(xml_nodes) == 0:
            raise ParseError('Error: required repeatable node has no elements! Your XML is invalid!')
        return xml_nodes

    def single_optional_node(self, container, xpath_expression, node_class):
        """
        Some LIDO-elements are optional. While self.repeatable_node handles this well,
        the normal way to get a single node uses pop(), which doesn't work with empty lists.
        Returns the node_class(lido_element) in a list or an empty list.
        :param container:
        :param xpath_expression:
        :param node_class:
        :return:
        """
        input_nodes = self.xpath(container, xpath_expression)
        if len(input_nodes) > 1:
            raise ParseError('Error: multiple nodes for a single node. Either your XML is invalid or the programmer made a mistake.')
        if len(input_nodes) == 1:
            return [node_class(input_nodes[0])]
        else:
            return [None]

    def single_required_node(self, container, xpath_expression, node_class):
        """
        Return a single required event. Return node_class(lido_element) in a list.
        :param container:
        :param xpath_expression:
        :param node_class:
        :return:
        """
        input_nodes = self.xpath(container, xpath_expression)
        if len(input_nodes) != 1:
            raise ParseError('Error: multiple or no nodes for a required single node. Either your XML is invalid or the programmer made a mistake.')
        return [node_class(input_nodes[0])]
