import requests
import re
from bs4 import BeautifulSoup

def word_stats(entry: str, lang_short: str = 'pl'):
    entry = f"https://{lang_short}.wikipedia.org/wiki/{entry}"

    page = requests.get(entry)
    soup = BeautifulSoup(page.content, 'html.parser')

    word_list = soup.text.split()
    word_list = re.split('[.,!?|\n\t ]', soup.text)
    for i in range(len(word_list)):
        word_list[i] = re.sub('[\[\]().]', '', word_list[i]).lower()

    word_dict = {}
    for word in word_list:
        if (word.isalpha()) and word not in list(word_dict.keys()):
            word_dict[word] = word_list.count(word)

    return lang_short, dict(reversed(sorted(word_dict.items(), key=lambda item: item[1])))

with open('odm.txt', 'r+', encoding='utf-8') as words_file:
    words = re.split('\n|, ', words_file.read())
with open('names.txt', 'r+', encoding='utf-8') as names_file:
    names = re.split('\n|, ', names_file.read())

def isPlWord(word: str, dictionary: list[str]):
    return word in dictionary

def isPlName(word: str, names: list[str]):
    return word in names

lang_short, word_dict = word_stats('Ananas')
print(word_dict)
print('Words not in polish dictionary')
for word in list(word_dict.keys()):
    if not (isPlName(word, words) or isPlWord(word, names)):
        print(word)