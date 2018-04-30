"""

// a = [2, 3, 3, 1, 5, 2] Input
// firstDuplicate(a) = 3 Ouput

/// The element in a that occurs in the array more than once and
/// has the minimal index for its second occurrence. 
If there are no such elements, return -1.

"""
def firstDuplicate(collection):

    seenDic = dict()
    for i in collection:
        if i not in seenDic:
            seenDic[i] = True
        else:
            return i

collection1 = [4,3,1,4,1]

# reuslt = firstDuplicate(collection1)

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

result = sumOfTwo([1,2,3,4],[10,20,30,40], 44)
print(result)