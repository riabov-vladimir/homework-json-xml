import json


def json_news_text_reader(file='newsafr.json', encoding='UTF-8'):
	with open(file, 'r') as reader:
		news_feed = json.load(reader)

	news_text = []

	for item in news_feed['rss']['channel']['items']:
		for word in item['description'].split():
			news_text.append(word.lower())
	return news_text
