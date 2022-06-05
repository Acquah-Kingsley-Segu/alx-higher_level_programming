def no_c(my_string):
    l_str = ""
    for char in my_string:
        if ord(char) == ord('c') or ord(char) == ord('C'):
            continue
        l_str += char
    return l_str
