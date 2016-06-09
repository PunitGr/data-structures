def QuickSort(myList, first, last):
    if first < last:
        pivot = partition(myList, first, last)
        QuickSort(myList, first, pivot - 1)
        QuickSort(myList, pivot + 1, last)
    return myList


def partition(myList, first, last):
    pivot = myList[last]
    i = first - 1
    for j in range(first, last):
        if myList[j] <= pivot:
            i = i + 1
            myList[i], myList[j] = myList[j], myList[i]
    myList[i + 1], myList[last] = myList[last], myList[i + 1]
    return (i + 1)


myList = [5, 2, 7, 0, 99, 1, 100, 0, 666]
list = QuickSort(myList, 0, len(myList) - 1)
print list
