def selectionSort(myList):
    for i in range(0, len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] > myList[j]:
                temp = myList[i]
                myList[i] = myList[j]
                myList[j] = temp
    return myList

myList = [5, 2, 7, 0, 99, 1, 100, 0, 666]
list = selectionSort(myList)
print list
