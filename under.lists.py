"""
a b
[[], ['a'], ['b'], ['a', 'b']]
"""

def get_under_lists(input_str: str) -> list:
    list_input = input_str.split(' ')
    res = [[]]
    list_dop = []
    for i in range(len(list_input)):
        for j in range(len(list_input)):
            # доп = входящий_список[j:i+j+1]
            list_dop = list_input[j:i+j+1]
            if len(list_dop) == i +1:
                res.append(list_dop)
    return res

print(get_under_lists('a b'))