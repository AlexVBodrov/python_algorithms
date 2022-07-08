# Треугольник Паскаля 🌶️🌶️
# Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов,
#  имеющая треугольную форму. В этом треугольнике
#  на вершине и по бокам стоят единицы.
#  Каждое число равно сумме двух расположенных над ним чисел.


def pascal_s_triangle(num_str: int) -> list:
    list1 = []
    num_str = num_str  # если № строк начинаеться с 1 и =>else: num_str + 1
    for i in range(num_str):
        temp_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(list1[i - 1][j - 1] + list1[i - 1][j])
        list1.append(temp_list)
    return list1


def print_row_pascal_s_triangle(num_str: int):
    list_pt = pascal_s_triangle(num_str)
    for el in list_pt:
        print(*el)


if __name__ == '__main__':
    print_row_pascal_s_triangle(4)
