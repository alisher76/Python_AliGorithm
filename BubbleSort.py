def sortArrayOfNumbersUsingBubbleSort(alist):

    if len(alist) > 0:
        changes = True
        highestSortedIndex = len(alist)-1
        while highestSortedIndex > 0 and changes:
             changes = False
             for i in range(highestSortedIndex):
                 if alist[i]>alist[i+1]:
                    changes = True
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp
             highestSortedIndex = highestSortedIndex-1
    else:
        print("list is empty")


alist=[]
sortArrayOfNumbersUsingBubbleSort(alist)
print(alist)
def letsStayThirstyForMoreKnowledge():
    print("Happy Coding to you All!")

letsStayThirstyForMoreKnowledge()