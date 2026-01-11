marks = int(input("Enter the marks of Student : = "))

if marks >= 90 and marks <= 100 :
    print(f"For The {marks} Grade is : = A")
elif marks >= 80 and marks < 90 :
    print(f"For The {marks} Grade is : = B")
elif marks >= 70 and marks < 80 :
    print(f"For The {marks} Grade is : = C")
elif marks >= 60 and marks < 70 :
    print(f"For The {marks} Grade is : = D")
elif marks >= 35 and marks < 60 :
    print(f"For The {marks} Grade is : = PASS")
else :
    print(f"Your Fail ... shame on you ! ")
    
    