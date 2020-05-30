import xml.etree.ElementTree as ET


def xml_news_text_reader(file='newsafr.xml'):
	parser = ET.XMLParser(encoding='utf-8')
	tree = ET.parse(file, parser)
	root = tree.getroot()

	xml_items = root.findall('channel/item')

	news_texts = []

	for item in xml_items:
		news_texts.append((item.find('description').text.lower().split()))

	news_text = []

	for text in news_texts:
		news_text.extend(text)

	return news_text
