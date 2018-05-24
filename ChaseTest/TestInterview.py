
import functools

# reverse the worrds
def reverseWords(input):
    inp = input.split(" ")
    temp = [word[::-1] for word in inp]
    newSentence = " ".join(temp)

    return newSentence

print(reverseWords("""RemoteIo is awesome
Candidates give interview
best candidates are selected"""))

def reverse_string2(s):
    """Return a reversed copy of `s`"""
    return " ".join(reversed(s))

#print(reverse_string2("Hello world this is the test this should work \n heloo alisher"))

def try_3(line):
    for l in reversed(list(line)):
        print(line.rstrip())

#print(try_3("Hello world this is the test this should work \n heloo alisher"))

def returnAverage(input):

    myNumberList = input.split(" ")
    integerList = list(map(lambda x: int(x), myNumberList))
    myNumberInt = functools.reduce(lambda a,b : int(a) + int(b), integerList)
    return min(input, key=lambda x:abs(int(x)-myNumberInt))

#print(returnAverage('5 4 5 2 3'))


def task5(array, target):
    ls = array
    while ls:
        num = ls.pop()
        diff = target - num
        if diff in ls:
            print([num, diff])

task5([2, 3, 7, 4, 5, 9, 1], 5)
