def commoncharacters(strings):
    str = strings[0]
    inAllList = []

    for ch in str:
        if inAllStrings(ch,strings):
            inAllList.append(ch)

    return inAllList

def inAllStrings(ch,strings):
    inAll = True    # initialize
    for i in range(len(strings)):
        if ch not in strings[i]:
            inAll = False
    return inAll
