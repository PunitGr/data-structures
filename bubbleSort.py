def bubbleSort(myList):
    swap = True
    while swap:
        swap = False
        for element in range(len(myList) - 1):
            if myList[element] > myList[element + 1]:
                swap = True
                temp = myList[element + 1]
                myList[element + 1] = myList[element]
                myList[element] = temp
    return myList


myList = [2, 98, 19, 2, 4, 5, 7, 9, -1, 0]
sortedList = bubbleSort(myList)
print sortedList
