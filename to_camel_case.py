def to_camel_case(text):
    nw = ""
    f = False
    for i in range(len(text)):
        sy = ""
        if not f:
            sy = text[i]
        f = False
        if (text[i] == "-") or (text[i] == "_"):
            sy = text[i + 1].upper()
            f = True
        nw += sy

    return nw

