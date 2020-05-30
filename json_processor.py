import json
from pprint import pprint
from collections import Counter


with open('newsafr.json', 'r', encoding='UTF-8') as reader:
	news_feed = json.load(reader)

news_text = []

for item in news_feed['rss']['channel']['items']:
	for word in item['description'].split():
		news_text.append(word.lower())

# news_text = filter(lambda x: len(x)>6, news_text)

# news_text.sort(key=lambda x: len(x))

news_text_sorted = list(filter(lambda x: (len(x)>6), news_text))

words_query = {}

for word in news_text_sorted:
	if word in words_query.keys():
		words_query[word] += 1
	else:
		words_query.setdefault(word, 1)

top_10 = Counter(words_query).most_common(10)

print(top_10)