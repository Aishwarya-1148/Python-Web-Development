while True:
    print("\n=== Simple Calculator ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    match choice:
        case 1:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            result = a + b   # store in 3rd variable
            print("Result = ", result)

        case 2:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            result = a - b
            print("Result = ", result)

        case 3:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            result = a * b
            print("Result = ", result)

        case 4:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            if b != 0:
                result = a // b   # integer division
                print("Result = ", result)
            else:
                print("Error! Division by zero not allowed.")

        case 5:
            print("Exiting Calculator... Goodbye!")
            break   # exit the loop

        case _:
            print("Invalid choice! Please enter between 1–5.")
