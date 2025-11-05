# operator overloding 
# for addition 
# class Point:
#     def __init__(self , x , y ):
#         self.x = x 
#         self.y = y 
        
#     def __add__(self , other ):
#         # way 1 
#         # newX = self.x + other.x
#         # newY = self.y + other.y
#         # return Point(newX , newY)
    
#         #way 2 
#         return Point(self.x + other.x , self.y + other.y) # new obj will be created and returned 
        
# p1 = Point(10 , 20 )
# p2 = Point(5 , 10 )
# #          15 , 30 
# p3 = p1 + p2  # Error 
# print("the addition of onj is : = ",p3.x , p3.y)
# operator overloading in python is performed with predefined magic / special methods 


# for substraction 
class Point:
    def __init__(self , x , y ):
        self.x = x 
        self.y = y 
        
    def __sub__(self , other ):
        return Point(self.x - other.x , self.y - other.y) # new obj will be created and returned 
        
p1 = Point(10 , 20 )
p2 = Point(5 , 10 )
#          15 , 30 
p3 = p1 - p2  # Error 
print("the addition of onj is : = ",p3.x , p3.y)
 
 
'''
⚠️ Operators That CANNOT Be Overloaded in Python
Operator	Description
and	    Logical AND operator
or	    Logical OR operator
not	    Logical NOT operator
is	    Identity operator
is not	Negated identity operator
in	    Membership operator
not in	Negated membership operator
'''