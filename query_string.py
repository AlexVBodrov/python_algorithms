def build_query_string(params: dict) -> str:
    lst_keys = []
    for k in params:
        lst_keys.append(k)
    lst_keys.sort()
    res = ''
    for k in lst_keys:
        res += k + '=' + str(params[k]) + '&'
    return res.rstrip('&')


def build_query_string_v2(params):
    res = [f'{k}={v}' for k, v in params.items()]
    res.sort()
    # print(res)  # => ['age=28', 'name=timur']
    return '&'.join(res)  # => 'age=28&name=timur'


result = build_query_string({'name': 'timur', 'age': 28})
assert build_query_string({'name': 'timur', 'age': 28}) == 'age=28&name=timur', f'test_1 {result=}'
result = build_query_string({'sport': 'hockey', 'game': 2, 'time': 17})
assert build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}) == 'game=2&sport=hockey&time=17', f'test_2 {result=}'

build_query_string_v2({'name': 'timur', 'age': 28})
