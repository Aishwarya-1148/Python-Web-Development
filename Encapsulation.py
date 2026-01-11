#Encapsulation in python 
# priavate
# class Encapsulation:
#     def __init__(self , a , b ):
#         self.__a = a 
#         self.__b = b 
#         print("this is init method ")
    
#     def show(self):
#         print(f"a = {self.__a} , b = {self.__b }")

# e = Encapsulation(11,22)
# print(" a = ",e.a) #NO ERROR when a is public 
# print(" a = ",e.a) #ERROR when a is private
# e.show()

"""
There are total 3 access modifiers in python 
1. Private : Accessible  inside class only  (with self)
2. Protected  : Accessible  inside class and All child classes (with self)
3. Public  : Accessible  Outside of class but with obj name (sy :=> obj.AttributeNAme) 
"""

# protected 
class Encapsulation:
    def __init__(self , a , b , c ):
        self.__a = a 
        self.__b = b 
        self._c = c # protected
        print("this is init method ")
    
    def show(self):
        print(f"a = {self.__a} , b = {self.__b } , c = {self._c}")

class Child(Encapsulation):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
    
    def display(self):
        print("inside child class c = ",self._c)

# e = Encapsulation(11,22 , 33 ) 
# print("Outside of class c = ",e.c) # Error : bcz c is protected ( not accessible outside of class )

c = Child(11,22,33)
c.display()

