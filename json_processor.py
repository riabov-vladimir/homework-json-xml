import json
from pprint import pprint


with open('newsafr.json', 'r', encoding='UTF-8') as reader:
	news_feed = json.load(reader)

news_text = []

for item in news_feed['rss']['channel']['items']:
	for word in item['description'].split():
		news_text.append(word)

print(news_text)