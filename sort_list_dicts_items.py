items = [
    {'title': '3-к квартира 80м2 . 11/22 эт.', 'rooms': 2, 'price': 10000, 'petFryendly': True},
    {'title': '3-к квартира 80м2 . 11/22 эт.', 'rooms': 2, 'price': 70000, 'petFryendly': True},
    {'title': '3-к квартира 80м2 . 11/22 эт.', 'rooms': 2, 'price': 73000, 'petFryendly': True},
    {'title': '3-к квартира 80м2 . 11/22 эт.', 'rooms': 2, 'price': 80000, 'petFryendly': True},
    {'title': '3-к квартира 80м2 . 11/22 эт.', 'rooms': 2, 'price': 81000, 'petFryendly': True},
    {'title': '3-к квартира 80м2 . 11/22 эт.', 'rooms': 2, 'price': 50000, 'petFryendly': True},
    {'title': '3-к квартира 80м2 . 11/22 эт.', 'rooms': 2, 'price': 54000, 'petFryendly': True},
    {'title': '3-к квартира 80м2 . 11/22 эт.', 'rooms': 2, 'price': 76000, 'petFryendly': True}
]


def get_id_price_in_list_dicts(input_list: list) -> dict:
    out_dict = {}
    for i in range(len(input_list)):
        out_dict[i] = input_list[i]['price']
    return out_dict


def filter_price(data, low, hi):
    out_list = []
    for el in data:
        if low < el['price'] < hi:
            out_list.append(el)
    return out_list


def filter_id_price_in_list_dicts(input_dict: dict, low=0, hi=1000000) -> list:
    dict_filter = {}
    for key, value in sorted(input_dict.items(), key=lambda x: x[1]):
        if value >= low and value <= hi:
            dict_filter[key] = value
    return dict_filter


def sort_id_price_in_list_dicts(input_dict: dict) -> list:
    lisr_order = []
    for key, value in sorted(input_dict.items(), key=lambda x: x[1]):
        lisr_order.append(key)
    return lisr_order


def sort_input_data_list(data: list, list_order: list) -> list:
    sorted_data = []
    for num in list_order:
        sorted_data.append(data[num])
    return sorted_data


def sort_items_for_price(data, low=0, hi=1000000):
    dict_id_price = get_id_price_in_list_dicts(data)
    lisr_order = filter_id_price_in_list_dicts(dict_id_price, low, hi)
    result = sort_input_data_list(data, lisr_order)
    return result


if __name__ == '__main__':
    # print(sort_items_for_price(items, hi=70000))
    print(filter_price(items, 30000, 78000))
