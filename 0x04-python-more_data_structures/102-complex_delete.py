#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    new_dic = {}
    key_list = []
    for key, val in a_dictionary.items():
        if val != value:
            new_dic[key] = a_dictionary[key]
        else:
            key_list.append(key)
    for key in key_list:
        del a_dictionary[key]
    return new_dic
