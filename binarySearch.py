def binarySearch(item, numberList):
	found = False
	top = len(numberList)-1
	bottom = 0
	while not found and bottom <= top:
		middle = (bottom+top)/2
		if numberList[middle] == item:
			found = True
		elif numberList[middle] < item:
			bottom = middle + 1
		else:
			top = middle - 1
	return found

if __name__ == "__main__":
	numberList = [2,4,6,8,10,40,44,56,78,90]
	item = int(raw_input("Enter the number you want to search "))
	result = binarySearch(item, numberList)
	if result == True:
		print("The number is found")
	else:
		print("Not Found")
