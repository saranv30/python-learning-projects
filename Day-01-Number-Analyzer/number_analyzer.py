#number analyzer CLI


    
print("---------NUMBER ANALYZER----------")

choice = input("y/n:").lower()

while choice == "y":

    try:
        num = int(input("Enter a number: "))
        print("Number:",num)
        if num > 0:
            print("Type: Positive")
        elif num < 0 :
            print("Type: Negative")
        else:
            print("Type: Zero")

        if num % 2 == 0:
            print("Even or Odd: Even")
        else:
            print("Even or Odd: Odd")

        print("Square:", num ** 2)
        print("Cube:", num ** 3)

        if num % 5 == 0:
            print("Multiple of 5: Yes")
        else:
            print("Multiple of 5: No")

    except ValueError:
            print("Invalid Input!")

    choice = input("Continue? (y/n): ")
            

    if choice == "n":
        print("Thank you")
        break



