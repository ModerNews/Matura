import re

filename = input("Ścieżka pliku sprawdzanego:\n")
with open(filename, 'r', encoding='utf-8') as file:
    string = file.read()

string = string.replace("!", ".")
string = string.replace("?", ".")
sentence_list_1 = string.split('.')

temp_list = string.lower().split()

text1_words_dict = {}
all_words = 0

for word in temp_list:
    all_words += 1
    if word in text1_words_dict.keys():
        text1_words_dict[word] += 1
    else:
        text1_words_dict[word] = 1

filename = input("Ścieżka pliku porównawczego:\n")
with open(filename, 'r', encoding='utf-8') as file:
    string = file.read()

string = string.replace("!", ".")
string = string.replace("?", ".")
sentence_list_2 = string.split('.')

temp_list = string.lower().split()

text2_words_dict = {}

for word in temp_list:
    if word in text2_words_dict.keys():
        text2_words_dict[word] += 1
    else:
        text2_words_dict[word] = 1

for word in list(text2_words_dict.keys()):
    if not word in list(text1_words_dict.keys()):
        text2_words_dict.pop(word)

for word in list(text1_words_dict.keys()):
    if not word in list(text2_words_dict.keys()):
        text1_words_dict.pop(word)

repeated_words = 0
for word in list(text1_words_dict.keys()):
    if text1_words_dict[word] > text2_words_dict[word]:
        repeated_words += text2_words_dict[word]
    else:
        repeated_words += text1_words_dict[word]

print("Pokrywa się:\n", round(repeated_words/all_words * 100, 2), "% słów")

repeated_sentences = 0
for sentence in sentence_list_1:
    if sentence in sentence_list_2:
        repeated_sentences += 1

print(round(repeated_sentences/len(sentence_list_1) * 100, 2), "% zdań")

mistakes = 0
mistaken_words = []
with open("odm.txt", 'r+', encoding='utf-8') as words_file:
    words = re.split('\n|, ', words_file.read())

with open("names.txt", 'r+', encoding='utf-8') as names_file:
    names = re.split('\n|, ', names_file.read())

i = 0
for word in list(text1_words_dict.keys()):
    if word not in words and word not in names:
        if word in text2_words_dict.keys():
            mistakes += 1
            mistaken_words.append(word)
    i += 1

print(mistakes, "słów zostało wypisanych z błędem tak samo jak w pliku porównawczym, co daje", round(mistakes / all_words * 100, 2), "% sprawdzanego tekstu, są to:")
try:
    print(", ".join(mistaken_words))
except:
    print(mistaken_words)

