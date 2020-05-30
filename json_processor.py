import json


def json_news_text_reader(file='newsafr.json'):
	"""Функция для десериализации xml файла с новостями в список всех слов всех новостей.
	Принимает название файла (файл по умолчанию 'newsafr.xml'), возвращает список news_text."""

	with open(file, 'r', encoding='UTF-8') as reader:
		news_feed = json.load(reader)

	news_text = []

	for item in news_feed['rss']['channel']['items']:
		for word in item['description'].split():
			news_text.append(word.lower())

	return news_text
