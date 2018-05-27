"""

// a = [2, 3, 3, 1, 5, 2] Input
// firstDuplicate(a) = 3 Ouput

/// The element in a that occurs in the array more than once and
/// has the minimal index for its second occurrence. 
If there are no such elements, return -1.

"""
import functools

def firstDuplicate(collection):

    seenDic = dict()
    for i in collection:
        if i not in seenDic:
            seenDic[i] = True
        else:
            return i

collection1 = [4,3,1,4,1]

# reuslt = firstDuplicate(collection1)

##############################################################
"""
You have two integer arrays, a and b, and an integer target value v. 
Determine whether there is a pair of numbers, where one number is taken 
from a and the other from b, that can be added together to get a sum of v. 
Return true if such a pair exists, otherwise return false.

Example

For a = [1, 2, 3], b = [10, 20, 30, 40], and v = 42, the output should be
sumOfTwo(a, b, v) = true.
"""

def sumOfTwo(a=[],b=[],v=0):
    #No need to iterate a huge list, if the other list is empty
    if not a or not b:
        return False
    
    #kill duplicates
    b = set(b)
    
    #iterate through list a to look if the wanted difference is in b
    for x in a:
        if (v-x) in b:
            return True
    return False

#result = sumOfTwo([1,2,3,4],[10,20,30,40], 44)
#print(result)
##############################################################
# Write a Python program to change the position of every n-th value with the (n+1)th in a list.
def convertListOfNumsInOne(list_of_nums):
    numString = x = int("".join(map(str, list_of_nums)))
    return numString

# convertListOfNumsInOne([1,2,3,4,5])

##############################################################
# Write a Python program to multiplies all the items in a list
def multiplyAllTheItemsIn(list_input):
    return functools.reduce(lambda a,b: a * b, list_input)

# print(multiplyAllTheItemsIn([2,3,4]))

##############################################################
# Write a Python program to get the largest number from a list.
def largestNumFrom(list1):
    list1.sort()
    return list1[-1]
# print(largestNumFrom([1,2,2,3,1,3,9,4,2,7]))

def smallestNumFrom(list1):
    if list1.count == 0: return 0
    list1.sort()
    return list1[0]

# print(smallestNumFrom([1,2,2,3,1,3,9,4,2,7]))

##############################################################

#  Write a Python program to replace dictionary values with their sum.



def changeValuesOfDict(dict):
    for d in list_of_dicts:
        n1 = d.pop('V')
        n2 = d.pop('VI')
        d['V+VI'] = (n1 + n2)/2
    return list_of_dicts
    student_details= [
    {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
    {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
    {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
    ]


