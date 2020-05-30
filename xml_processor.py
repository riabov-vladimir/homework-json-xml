import xml.etree.ElementTree as ET


def xml_news_text_reader(file='newsafr.xml'):
	"""Функция для десериализации xml файла с новостями в список всех слов всех новостей.
	Принимает название файла (файл по умолчанию 'newsafr.xml'), возвращает список news_text."""

	parser = ET.XMLParser(encoding='utf-8')
	tree = ET.parse(file, parser)
	root = tree.getroot()

	xml_items = root.findall('channel/item')

	news_texts = []

	for item in xml_items: # не догадался как сделать, чтобы сразу получился список, а не список списков
		news_texts.append((item.find('description').text.lower().split()))

	news_text = [] # список списков --> список

	for text in news_texts:
		news_text.extend(text)

	return news_text
