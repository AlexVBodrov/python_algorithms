"""
Напишите функцию matrix(), которая создает, заполняет и возвращает матрицу заданного размера.
При этом (в зависимости от переданных аргументов) она должна вести себя так:
print(matrix())                   # матрица 1 × 1 из 0
print(matrix(3))                  # матрица 3 × 3 из 0
print(matrix(2, 5))               # матрица 2 × 5 из 0
print(matrix(3, 4, 9))            # матрица 3 × 4 из 9

[[0]]
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
[[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]]
"""


def matrix(r=0, c=0, num=0):
    if c == 0 and c != r:
        c = r
    if r == 0:
        return [[0]]
    res = []
    for r in range(1, r + 1):
        out_list_2 = []
        for c in range(1, c + 1):
            out_list_2.append(num)
        res.append(out_list_2)
    return res


def matrix_2(n=1, m=None, value=0):
    if m is None:
        m = n
    return [[value] * m for _ in range(n)]


def test_matrix():
    result = matrix()
    assert result == [[0]], f'Wrong answer: {result} = Test_1'
    result = matrix(3)
    assert result == [[0, 0, 0], [0, 0, 0], [0, 0, 0]], f'Wrong answer: {result} = Test_2'
    result = matrix(2, 5)
    assert result == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], f'Wrong answer: {result} = Test_3'
    result = matrix(3, 4, 9)
    assert result == [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]], f'Wrong answer: {result} = Test_4'
    print('\033[32m All Tests => OK !!! \033[0;0m')


if __name__ == '__main__':
    # test_matrix()
    print(matrix(3, 1))

