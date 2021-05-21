"""
2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle,
 прочитать из них информацию.
  И получить объект: словарь из предыдущего задания.
"""
import json
import pickle

with open('group.pickle', "rb") as file:
    my_dict = pickle.load(file, encoding='utf-8')

#print(my_dict) #-work


with open('group.json', "r",  encoding='utf-8') as file:
    pass
    #data = json.load(read_file)
    my_dict_original = json.load(file)

print(my_dict_original)

