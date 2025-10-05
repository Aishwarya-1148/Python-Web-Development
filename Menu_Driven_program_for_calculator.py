# menu driven for calculator
while True:
    print("---- The Menu is ----- ")
    print("1 : Addition ")
    print("2 : Substraction  ")
    print("3 : Multiplication")
    print("4 : Division ")
    print("5 : For Exit ")
    
    choice = int(input("Enter Your choice : = ")) # 2 

    a = int(input("Enter First Number  : = "))
    b = int(input("Enter Second Number : = ")) 
    
    if choice == 1 :
        print("-----THe Addition is : = -------",a+b)
    elif choice == 2 :
        print("------- THe Substraction is : = ------- ",a-b)
    elif choice == 3 :
        print("------- THe Multiplication is : = ------- ",a*b)
    elif choice == 4 :
        print("------- THe Division is : = ------- ",a/b)
    elif choice == 5 :
        break # will came out of while loop 
        # exit() # imediately stops the program doesnt matter what the flow is !   
    else:
        print("Invalid Choice ....! :( ")

print("Thank You ! Visit Again ..! ")