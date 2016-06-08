def insertionSort(myList):
    for i in range(1, len(myList)):
        temp = myList[i]
        j = i - 1
        while(j >= 0 and temp < myList[j]):
            myList[j + 1] = myList[j]
            j = j - 1
        myList[j + 1] = temp
    return myList

myList = [5, 2, 7, 0, 99, 1, 100]
list = insertionSort(myList)
print list
