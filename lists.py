def remove_elements(list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']):
    list2 = []
    if list == list2:
        return list
    else:
        del list[0]
        if len(list)<5:
            if len(list)<4:
                return list
            else:
                del list[(len(list)-2)]
                return list 
        else:
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
        return True
    else:
        return False
is_empty()

def check_lists(list1 = ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White'], list2 = ['Red', 'Green', 'White', 'Black', 'Pink']):
    if len(list1)>= 3 and len(list2)>=3:
        if list1[2] == list2[2]:
            return True
        elif len(list1)<3 or len(list2)<3:
            return False
        else:
            return False
    elif len(list1)>=3 and len(list2)<3:
        return False
    else:
        return False
check_lists()


def list_of_lists(list):
    ret = [[], [], []]
    ret[0] = list[0][:2]
    ret[1] = list[1][1:][:3]
    ret[2] = list[2][-2:]
    return ret
list_of_lists1([[1,2,3],[4,5,6,7,8],[9,10,11,12]])
