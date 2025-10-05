# menu driven for irrelavent menus 
while True:
    print("---- The Menu is ----- ")
    print("1 : Age Validation ")
    print("2 : Greater Among Two nos")
    print("3 : prime Nos ")
    print("4 : For Exit ")

    choice = int(input("Enter Your choice : = ")) #

    if choice == 1 :
        age = int(input("Enter The Age of the person : = "))
        if age > 18 and age <= 80 :
            print("The person is valid for vote ")
        elif age >= 0 and age <= 18 :
            print("The person is Invalid for vote ")
        else:
            print("The person doesn't Exist ... ! ")    
    elif choice ==  2 :
        a = int(input("Enter First Number  : = "))
        b = int(input("Enter Second Number : = ")) 
        if a > b :
            print("a is greater") 
        else:
            print("b is greater")
    elif choice == 3 :
        n = int(input("Enter The  Number  : = "))
        cnt = 0 
        for i in range(2 , n ):
            if n % i == 0 :  
                cnt += 1 
                break
        if cnt == 0 :
            print("The Number n is prime no ")
        else:
            print("The Number n is not prime no ")
    elif choice == 4 :
        break
    else:
        print("Invalid Choice ....! :( ")

print("Thank You ! Visit Again ..! ")