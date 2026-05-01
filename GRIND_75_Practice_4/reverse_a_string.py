def reverse_a_string(st):
    reverse = ""
    length = len(st) - 1
    while length >= 0:
        reverse += st[length]
        length -= 1
    return reverse


print(reverse_a_string("abcdefg"))
