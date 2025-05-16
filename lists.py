def remove_elements(list_to_remove_elements):
    lista1 = list_to_remove_elements
    if len(lista1) > 5:
        del lista1[5]
    if len(lista1) > 4:
        del lista1[4]
    if len(lista1) > 0:
        del lista1[0]
    return lista1

def add_elements(list_to_add_elements):
    list_to_add_elements.append('Yellow')
    list_to_add_elements.insert(0,'Pink')
    return list_to_add_elements

def is_empty(list_to_check):
    return len(list_to_check) == 0


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        return list_to_compare1[2] == list_to_compare2[2]:
    else:
        return False

def list_of_lists(list_of_lists_to_modify):
    a = list_of_lists_to_modify[0][:2]
    b = list_of_lists_to_modify[1][1:4]
    c = list_of_lists_to_modify[2][-2:]
    return [a, b, c]
