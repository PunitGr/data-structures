def linearSearch(item, myList):
    found = False
    position = 0
    counter = 0
    while position < len(myList) and not found:
        if myList[position] == item:
            found = True
        position += 1
        counter = counter + 1
    if found is True:
        temp = 'found at position %d with %d number of searches' % (position, counter)
        print temp
    else:
        print("""Not Found in the list \n -------------Processing List
	      ------------------Appending to the list""")
        myList.append(item)
if __name__ == "__main__":
    mylist = raw_input("Enter the list ").split()
    item = raw_input("Enter the item to be found ")
    linearSearch(item, mylist)
    print ("lets search again")
    linearSearch(item, mylist)
