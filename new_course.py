# list_nums = list(map(int, input().split()))
# lst = [int(i) for i in input().split()]
# lst = [int(input()) for _ in range(int(input()))]


def forwar_to_back(input_list: list) -> list:
    for i in range(0, len(input_list), 2):
        # print(i)
        if i < len(input_list) - 1:
            input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
    out = ' '.join(str(x) for x in input_list)
    return out


def test_forwar_to_back():
    result = forwar_to_back([1, 2, 3, 4, 5])
    assert result == '2 1 4 3 5', f'Wrong answer: {result} = Test_1'
    result = forwar_to_back([2, 3, 2, 4])
    assert result == '3 2 4 2', f'Wrong answer: {result} = Test_2'
    result = forwar_to_back([1, 2, 3, 4, 5])
    assert result == '2 1 4 3 5', f'Wrong answer: {result} = Test_3'
    result = forwar_to_back([1])
    assert result == '1', f'Wrong answer: {result} = Test_4'
    print('All Tests => OK !!!')


if __name__ == "__main__":
    print(forwar_to_back([1, 2, 3, 4, 5]))
    test_forwar_to_back()
