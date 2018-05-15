import functools

names = ["Anna Mark", "Ali Sherali Abdukarim", "ali bobur dabba hama"]

def answer(name):
    splittedName = name.split(" ")
    last = splittedName.pop()

    n = len(splittedName)
    if n == 4:
        first, middle = ' '.join(splittedName[:2]), ' '.join(splittedName[2:])
    elif n == 3:
        middleNames = splittedName[1:]
        if middleNames[0] in ("Sh", "BS", "M"):
            first, middle = splittedName[0], "{}. {}.".format(middleNames[0][:1],middleNames[1][:1])
        else:
            first, middle = splittedName[0], "{}. {}.".format(middleNames[0][0],middleNames[1][0])
    elif n == 2:
        if splittedName[1]:
            print("Here")
            first, middle = splittedName[0], "{}.".format(splittedName[0][:1])
        else:
            first, middle = splittedName[0], "{}.".format(splittedName[0][0])
    else:
        back = "{} {}".format(splittedName[0], last)
        return back
    back = "{} {} {}".format(first, middle,last)
    return back



print(answer(names[1]))

# reduce((lambda x, y: x * y), [1, 2, 3, 4])