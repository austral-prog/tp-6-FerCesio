def remove_elements(list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']):
    del list[0]
    del list[(len(list)-1)]
    del list[(len(list)-1)]
    return list
remove_elements()


def add_elements(list = ["Red", "Green", "White", "Black"]):
    list.insert(0, "Pink")
    list.insert((len(list)), "Yellow")
    return list
add_elements()

def is_empty(list = [1]):
    empty = []
    if list == empty:
        return "Vacio"
    else:
        return "Tiene elementos"
is_empty()

def check_lists(list1 = ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White'], list2 = ['Red', 'Green', 'White', 'Black', 'Pink']):
    if list1[2] == list2[2]:
        return True
    elif len(list1)<3 or len(list2)<3:
        return False
    else:
        return False
check_lists()


def list_of_lists(list = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]):
    a = list[0]
    b = list[1]
    c = list[2]
    del b[0]
    z=[a[:2], b[:3], c[-2:]]
    return z
list_of_lists()
