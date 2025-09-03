#Check if the given integer number is Even or Not.
input_number=int(input("Enter a Number to check if it is Even: "))
if input_number % 2 == 0:
    print(f"The given number ", input_number, "is an Even Number ")
else:
    print(f"The given number ", input_number, "is not an Even Number ")