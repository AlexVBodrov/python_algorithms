"""
из массива дубли из массива
и оставить больше 5
"""


def get_uniqeu(array: list):
    if len(array)<1:
        return None
    elif len(set(array)) == 1:
        if max(set(array)) > 5:
            return list(set(array))
        else:
            return None
    elif max(array) <= 5:
        return None
    else:
        list_num_uniqeu = set(array)
        list_num_uniqeu = list(list_num_uniqeu)
        for el in list_num_uniqeu:
            if el <= 5:
                list_num_uniqeu.remove(el)
        
        return sorted(list_num_uniqeu)
            


def test_get_uniqeu():
    result = get_uniqeu([1, 5, 8, 8, 10])
    assert result == [8, 10], f'Wrong answer: {result} = Test_1'
    result = get_uniqeu([])
    assert result == None, f'Wrong answer: {result} = Test_2'

    result = get_uniqeu([1, 5])
    assert result == None, f'Wrong answer: {result} = Test_3' 

    result = get_uniqeu([8, 8, 8, 8, 8])
    assert result == [8], f'Wrong answer: {result} = Test_4'

    result = get_uniqeu([5, 5, 5, 5, 5])
    assert result == None, f'Wrong answer: {result} = Test_5'

    result = get_uniqeu([5])
    assert result == None, f'Wrong answer: {result} = Test_6' 

    result = get_uniqeu([1, 5, 4, 4, -5, 0])
    assert result == None, f'Wrong answer: {result} = Test_7'

    print('All Tests => OK !!!')

def get_uniqeu_whith_out_dobble(array: list):
    if len(array) < 1:
        return None
    elif len(array) == 1 and (array) <= [5]:
        return None
    elif len(set(array)) <= 1:
        return None
    elif max(set(array)) <= 5:
        return None
    else:
        dobble = None
        result_array = array.copy()
        for el in array:
            if el <= 5:
                result_array.remove(el)
            if el == dobble:
                result_array.remove(el)
                a = result_array.index(el)
                del result_array[a]
            else:
                dobble = el

        return result_array if len(result_array) > 1 else None

def test_get_uniqeu_whith_out_dobble():

    result = get_uniqeu_whith_out_dobble([9, 1, 5, 8, 8, 10, 14])
    assert result == [9, 10, 14], f'Wrong answer: {result} = Test_1'

    result = get_uniqeu_whith_out_dobble([])
    assert result == None, f'Wrong answer: {result} = Test_2'

    result = get_uniqeu_whith_out_dobble([1, 5])
    assert result == None, f'Wrong answer: {result} = Test_3' 

    result = get_uniqeu_whith_out_dobble([8, 8, 8, 8, 8])
    assert result == None, f'Wrong answer: {result} = Test_4'

    result = get_uniqeu_whith_out_dobble([5, 5, 5, 5, 5])
    assert result == None, f'Wrong answer: {result} = Test_5'

    result = get_uniqeu_whith_out_dobble([5])
    assert result == None, f'Wrong answer: {result} = Test_6' 

    result = get_uniqeu_whith_out_dobble([1, 5, 4, 4, -5, 0])
    assert result == None, f'Wrong answer: {result} = Test_7'

    print('All Tests => OK !!!')


if __name__ == "__main__":
    test_get_uniqeu()
    test_get_uniqeu_whith_out_dobble()
