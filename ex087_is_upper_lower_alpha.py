def isalpha(str):
    isalpha = True
    for char in str:
        if not ('a' <= char <= 'z' or 'A' <= char <= 'Z'):
            isalpha = False
            break

    return isalpha


def islower(str):
    yes = True
    for char in str:
        if char.isalpa() and not 'a' <= char <= 'z':
            yes = False
            break

    return yes


def isupper(str):
    yes = True
    for char in str:
        if char.isalpa() and not 'A' <= char <= 'Z':
            yes = False
            break

    return yes
