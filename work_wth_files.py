"""
Практическое задание
1: Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:

my_favourite_group = {
'name': 'Г.М.О.',
'tracks': ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок','year': 2016},
{'name': 'Шапито','year': 2014}]}

С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
 Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.

 """
import json
import music_serialize
import pickle

pickled = pickle.dumps(music_serialize.my_favourite_group)
json_ed = json.dumps(music_serialize.my_favourite_group)
print(pickled)
print(json_ed)

with open('group.pickle', "wb") as file:
    file.write(pickled)

with open('group.json', "w",  encoding='utf-8') as file:
    json.dump(music_serialize.my_favourite_group, file)
"""
2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle,
 прочитать из них информацию.
  И получить объект: словарь из предыдущего задания.
"""

import json
import pickle

with open('group.pickle', "rb") as file:
    my_dict = pickle.load(file, encoding='utf-8')

print(my_dict, "\n", 'Pickle') #-work


with open('group.json', "r",  encoding='utf-8') as file:
    my_dict_original = json.load(file)

print(my_dict_original, "\n",  "Json")
