def filter_words(st):
    New_String = ""

    if st[-1] == ' ':
        st = st[:-1]

    if ord(st[0]) in range(97, 123):
        New_String += chr(ord(st[0]) - 32)
    else:
        New_String += st[0]

    for char in st[1:]:
        if New_String[-1] == ' ' and char == ' ':
            continue
        if ord(char) in range(65, 91):
            New_String += chr(ord(char) + 32)
        else:
            New_String += char

    return New_String
