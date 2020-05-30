from json_processor import json_news_text_reader
from top_10_func import top_10_words_over_6_len
from xml_processor import xml_news_text_reader

json_top10 = top_10_words_over_6_len(json_news_text_reader())
xml_top10 = top_10_words_over_6_len(xml_news_text_reader())

print('10 самых часто встречающихся в новостях слов длиннее 6 символов(JSON файл):')
print(json_top10)
print('10 самых часто встречающихся в новостях слов длиннее 6 символов(XML файл):')
print(xml_top10)
