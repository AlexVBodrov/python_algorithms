
def second_max(array: list):
    if len(array) < 2:
        return None
    elif len(set(array)) == 1:
        return None
    else:
        from math import inf
        max_1 = -inf
        max_2 = -inf
        for num in array:
            if num > max_1:
                max_2 = max_1
                max_1 = num
            elif num == max_1:
                continue
            elif num < max_1 and num > max_2:
                max_2 = num
            elif num < max_1 and num == max_2:
                return None
        return max_2 if max_2 > -inf else None


def test_second_max():
    result = second_max([3, 2, -10, 100, 45, 100])
    assert result == 45, f'Wrong answer: {result}   : Test_1'
    result =  second_max([3])
    assert result == None, f'Wrong answer: {result} : Test_2'
    result =  second_max([100, 100])
    assert result == None, f'Wrong answer: {result} : Test_3'
    result =  second_max([100, 100, 100])
    assert result == None, f'Wrong answer: {result} : Test_4'
    result =  second_max([])
    assert result == None, f'Wrong answer: {result} : Test_5'
    result =  second_max([3, 2, -10, 100, 45, 45, 100])
    assert result == None, f'Wrong answer: {result} : Test_6'
    print("All tests => complite OK !!!")


if __name__ == "__main__":
    test_second_max()
    