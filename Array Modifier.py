# Write a python program that do the following:

# - display the initial content of the array
# - display a menu of options
# - allow user to select item in the menu (check if valid)
# - perform the selected option (you may prompt additional info to user when need)
# - display the resulting values of the array


# Note: 
# - The program has an array variable containing 10 random numbers
# - You may add other options and features
# - Your program should be uploaded to github before 1:30pm
# - Record a demo presenting your program
# - Send the demo directly to my messenger

# Example Output:

# Array: [1, 4, 3, 4, 4, 5, 6 ,2 ,56, 200]
# Menu:
#  1 -> Add an element
#  2 -> Insert an element
#  3 -> Modify an element
#  4 -> Delete an element
#  5 -> Arrange in ascending order
#  6 -> Arrange in descending order
# What do you want to do? (1-6): 4
# Enter the index you want to delete: 3
# The element has been deleted
# This is the new array: Array: [1, 4, 3, 4, 5, 6 ,2 ,56, 200]

array = [13, 5, 59, 65, 46, 72, 62, 87, 6, 98]

# Loop
i = 0
while i <= 1:
# Initial Content
    print("Array: ",array)
# Display Menu
    print("Menu: \n 1 -> Add an element \n 2 -> Insert an element \n 3 -> Modify an element")
    print(" 4 -> Delete an element\n 5 -> Arrange in ascending order \n 6 -> Arrange in descending order")
    print(" 7 -> Quit")
# Select item
    whatDo = int(input("What do you want to do? (1-7): "))
    if whatDo == 1:
        whatAdd = int(input("Enter Element you want to add: "))
    if whatDo == 2:
        whatIns = int(input("Enter Element you want to insert: "))
        whereIns = int(input("Enter the index you want to insert: "))
    if whatDo == 3:
        whereMod = int(input("Enter the index you want to modify: "))
        whatMod = int(input("Enter Element you want it to be: "))
    if whatDo == 4:
        whereDel = int(input("Enter the index you want to delete: "))
    if whatDo == 5:
        print("Arranging in ascending order....")
    if whatDo == 6:
        print("Arranging in descending order....")
    if whatDo == 7:
        confirm = input(("Are you sure? (y/n): "))
    else:
        print("Please enter a valid number")
# perform selected option
    if whatDo == 1:
        array.append(whatAdd)
    if whatDo == 2:
        array.insert(whereIns, whatIns)
    if whatDo == 3:
        array[whereMod] = whatMod    
    if whatDo == 4:
        array.pop(whereDel)
    if whatDo == 5:
        array.sort()
    if whatDo == 6:
        array.sort()
        array.reverse()
    if whatDo == 7:
        if confirm == "y":
            break
    print()

