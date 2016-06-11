def useStack():
    stack = []
    choice = -1
    while choice < 4 or choice > 0:
        print("1. Push to stack \n")
        print("2. Pop from stack \n")
        print("3. Print stack \n")
        print("4. Exit")
        choice = int(input("Enter your choice - "))
        if choice == 1:
            item = input("What do you want to add in stack")
            stack.append(item)

        elif choice == 2:
            print("the last one in stack was ", stack[-1])
            del stack[-1]

        elif choice == 3:
            for counter in range(len(stack) - 1, -1, -1):
                print(stack[counter])

        else:
            exit
