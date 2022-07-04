"""
pack list
w w w o r l d g g g g r e a t t e c c h e m g g p w w
"""
s = 'w w w o r l d g g g g r e a t t e c c h e m g g p w w'


def pack_el_in_list(input_str: str) -> list:
    string = input_str.replace(' ', '').strip()
    out_list = []
    print(out_list)
    print(string)
    for el in string:
        if string[el] == string[el - 1]:
            out_list.append(string[el])
        else:
            out_list[-1].append(string[el])

    return out_list


def test_pack_el_in_list():
    
    result = pack_el_in_list('a b c d')
    assert result == [['a'], ['b'], ['c'], ['d']], f'Wrong answer: {result} = Test_1'
   
    result = pack_el_in_list('w w w o r l d g g g g r e a t t e c c h e m g g p w w')
    assert result == [['w', 'w', 'w'], ['o'], ['r'], ['l'], ['d'], ['g', 'g', 'g', 'g'], ['r'], ['e'], ['a'], ['t', 't'], ['e'], ['c', 'c'], ['h'], ['e'], ['m'], ['g', 'g'], ['p'], ['w', 'w']], f'Wrong answer: {result} = Test_2'
    print('All Tests => OK !!!')


if __name__ == '__main__':
    #pack_el_in_list('w w w o r l d g g g g r e a t t e c c h e m g g p w w')
    print(pack_el_in_list('a b c d'))
    test_pack_el_in_list()