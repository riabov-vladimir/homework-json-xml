import json
from pprint import pprint


with open('newsafr.json', 'r', encoding='UTF-8') as reader:
	news_feed = json.load(reader)
	pprint(news_feed.get(''))