def no_c(my_string):
    l_str = ""
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        l_str += char
    return l_str
