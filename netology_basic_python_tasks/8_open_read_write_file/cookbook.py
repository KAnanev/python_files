def read_book(filename):
    cook_book = {}

    with open(filename, encoding="utf8") as f:
        raw_book = f.readlines()
    while len(raw_book) > 0:
        dish = raw_book.pop(0).strip()
        ing_count = int(raw_book.pop(0).strip())
        ingredient_list = []
        for i in range(ing_count):
            ingr_info = [x.strip() for x in raw_book.pop(0).split("|")]
            ingr_info[1] = int(ingr_info[1])
            ingredient_list.append(dict(zip(['ingredient_name', 'quantity', 'measure'], ingr_info)))
        cook_book[dish] = ingredient_list
        while len(raw_book) > 0 and raw_book[0].strip() == '':  # delete empty lines after dish block
            raw_book.pop(0)
    return cook_book


cook_book = read_book('recipes.txt')


def get_shop_list_by_dishes(dishes, person_count):
    temp_list1 = []
    dict_list3 = {}
    dishes = [x.strip() for x in dishes.pop(0).split(',')]
    for dish in dishes:
        if dish in cook_book.keys():
            for item in cook_book[dish]:
                if item not in temp_list1:
                    item['quantity'] = item['quantity'] * dishes.count(dish) * person_count
                    temp_list1.append(item)
    for item in temp_list1:
        dict_list3[item.pop('ingredient_name')] = item

    print(dict_list3)


get_shop_list_by_dishes(['Омлет, Омлет'], 3)
