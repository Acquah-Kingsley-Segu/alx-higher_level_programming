def no_c(my_string):
    if my_string is None:
        return None
    l_str = ""
    for char in my_string:
        if ord(char) == ord('c') or ord(char) == ord('C'):
            continue
        l_str += char
    return l_str
