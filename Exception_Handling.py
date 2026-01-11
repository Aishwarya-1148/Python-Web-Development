# Exception handling : 

# Phase - 1 : Program will execute Normally (bcz denomenator is not zero )
# a = 100 
# b = 5 
# result = a / b 
# print("THe Division Result is : = ",result)

# Phase - 2 : Abnormal Termination of program (bcz Denomenator is zero )
# a = int(input("Enter The Number1 : = "))
# b = int(input("Enter The Number2 : = "))
# result = a / b 
# print("THe Division Result is : = ",result)

"""
Phase - 3 : In order to maintain the Normal Flow of the program We have a 
Concept Called as Exception Handling in Python 
"""

# Handling the Zero Division Error : 
# try :
#     a = int(input("Enter The Number1 : = "))
#     b = int(input("Enter The Number2 : = "))
#     result = a / b 
#     print("THe Division Result is : = ",result)
# except ZeroDivisionError :
#     print("Please Enter the Valid Denomenator ..! ")
# except ValueError: # values should be Numbers only 
#     print(" Please Enter the Number Only ...! ")


# Phase - 4 : In Order to handle All types of Exception 
# try :
#     a = int(input("Enter The Number1 : = "))
#     b = int(input("Enter The Number2 : = "))
#     result = a / b 
#     print("THe Division Result is : = ",result)
# except Exception :
#     print("Something Went Wrong ....! ")



# Phase - 5 : This Exception declration is invalid bcz Every exception is going to handled by Exception class itself so , zerodivision error will never get executed ...!
# try :
#     a = int(input("Enter The Number1 : = "))
#     b = int(input("Enter The Number2 : = "))
#     result = a / b 
#     print("THe Division Result is : = ",result)
# except Exception :
#     print("Something Went Wrong ....! ")
# except ZeroDivisionError :
#     print("please Enter valid input ")



# Phase - 6 : Thats Why We should declare the Top Most class (Base class i.e., Exception class ) At last..!
# Technically : Top Most class of Exception Hierarchy should be declared at last

try :
    a = int(input("Enter The Number1 : = "))
    b = int(input("Enter The Number2 : = "))
    result = a / b 
    print("THe Division Result is : = ",result)
except ZeroDivisionError :
    print("please Enter valid input ")
except Exception :
    print("Something Went Wrong ....! ")
