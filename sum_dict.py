"""
Дополните приведенный код так, чтобы он объединил содержимое двух словарей
 dict1 и dict2 по ключам, складывая значения по одному и тому же ключу,
  в случае, если ключ присутствует в обоих словарях.
   Результирующий словарь необходимо присвоить переменной result.
"""
dict11 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict21 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

# result = {}


def sum_dict(dict1: dict, dict2: dict) -> dict:
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result


def test_sum_dict():
    result = sum_dict({'a': 100}, {'a': 300})
    assert result == {'a': 400}, f'Wrong answer: {result} = Test_1'
    result = sum_dict({'b': 100}, {'a': 300})
    assert result == {'b': 100, 'a': 300}, f'Wrong answer: {result} = Test_2'
    result = sum_dict({'a': 300, 'e': 98}, {'b': 100, 'c': 12, 'p': 123})
    assert result == {'b': 100, 'c': 12, 'p': 123, 'a': 300, 'e': 98}, f'Wrong answer: {result} = Test_3'
    print('All Tests => OK !!!')




if __name__ == '__main__':
    test_sum_dict()
