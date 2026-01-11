while True:
    print("\n=== Area Calculator ===")
    print("1. Area of Circle")
    print("2. Area of Rectangle")
    print("3. Area of Square")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        result = 3.14 * radius * radius
        print("Result = ", result)

    elif choice == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        result = length * width
        print("Result = ", result)

    elif choice == 3:
        side = float(input("Enter the side of the square: "))
        result = side * side
        print("Result = ", result)

    elif choice == 4:
        print("Exiting the program... Goodbye!")
        break   # exits the loop

    else:
        print("Invalid choice! Please enter between 1–4.")
