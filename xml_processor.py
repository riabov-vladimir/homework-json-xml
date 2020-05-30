import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()
print(root)
print(root.tag)
print(root.text)
print(root.attrib)

xml_items = root.findall("channel/item/description")
print(len(xml_items))
print(type(xml_items))
for item in xml_items:
	print(item.find("title").text)
	print()