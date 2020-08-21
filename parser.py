import xmltodict
from pprint import pprint
import json


import xml.dom.minidom

dom = xml.dom.minidom.parse("53200807526557003206550260002858411102040883-procNFe.xml") # or xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = dom.toprettyxml()

# print(pretty_xml_as_string)


o = xmltodict.parse(pretty_xml_as_string)
print(json.dumps(o, indent=4))
