numberList = [2, 5, 7, 9, 19, 64, 154, 1, 23, 37, 53, 79, 101, 200]


# ? Find the highest number in the list
def find_highest_number():
    numberList.sort()
    return numberList[-1]


# * Test the function
highest_number = find_highest_number()
print(f"The highest number in the list is: {highest_number}")
