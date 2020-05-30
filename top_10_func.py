from collections import Counter

def top_10_words_over_6_len(news_text):
	news_text_sorted = list(filter(lambda x: (len(x) > 6), news_text))

	words_query = {}

	for word in news_text_sorted:
		if word in words_query.keys():
			words_query[word] += 1
		else:
			words_query.setdefault(word, 1)

	top_10 = Counter(words_query).most_common(10)

	return top_10
