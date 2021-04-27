from random import *
import re

def to_pseudo_json(file):
    list = []
    temp = file.read().split('\n')
    temp[0] = temp[0].split('\t')
    for line in temp[1:-1]:
        line = line.split('\t')
        temp_dict = {}
        i = 0
        for element in line:
            temp_dict[temp[0][i]] = element
            i += 1
        list.append(temp_dict)
    return list


def min_max_from_array(array: list):
    return [min(array), max(array)]


def warden_search(array: list, value: int, warden: int = None):
    i = 0
    array.append(warden)
    if warden is None:
        warden = -1
        non_provided = True
    if warden in array:
        if non_provided:
            raise AttributeError('warden is an attribute that\'s missing')
        else:
            raise ValueError('warden should have that\'s not already inside array')
    while array[i] != value or array[i] != warden:
        i += 1

    if array[i] == warden:
        raise ValueError(f'value doesn\t belong to list')
    else:
        return i


def indexes(array: list, value: int):
    return [i for i in range(len(array)) if i == value]

def array_leader(array: list):
    dict = {}
    for n in array:
        if n in list(dict.keys()):
            dict[n] += 1
        else:
            dict[n] = 1
    max_count = max(list(dict.values()))
    if max_count > len(array) // 2:
        return list(dict.keys())[list(dict.values()).index(max_count)]
    else:
        raise ValueError('Providen array does not have a leader')


def array_leader_cross(array: list):
    leader = array[0]
    pair = 1
    for n in array:
        if pair > 0:
            if n == leader:
                pair += 1
            else:
                pair -= 1
        else:
            pair += 1
            leader == n

    if pair == 0:
        raise ValueError('Providen array does not have a leader')

    # count = array.count(leader)
    count = 0
    for i in range(len(array)):
        if array[i] == leader:
            count += 1

    if count > len(array) // 2:
        return leader

    raise ValueError('Providen array does not have a leader')


def array_leader_count(array: list):
    for x in array:
        if array.count(x) > (len(array)//2):
            return x
    raise ValueError('Providen array does not have a leader')


def list_generator(len: int, leader: int = None):
    array = []
    if 0 >= len:
        raise ValueError('len has to be greater then 0')
    if leader is not None:
        if not len % 2 == 0:
            len += 1
    for x in range(len):
        if x % 2 == 0 and leader is not None:
            array.append(leader)
        else:
            array.append(randint(0, 9))
    array.append(leader)
    return array


def iq_check(text: str, words_filename: str = 'odm.txt', names_filename: str = 'names.txt'):
    text = text.split()
    iq_checks = []
    with open(words_filename, 'r+', encoding='utf-8') as words_file:
        words = re.split('\n|, ', words_file.read())
    with open(names_filename, 'r+', encoding='utf-8') as words_file:
        names = re.split('\n|, ', words_file.read())

    i = 0
    for word in text:
        if word not in words and word not in names:
            iq_checks.append({word: i})
        i += 1
    return iq_checks
