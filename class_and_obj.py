# # student ( id , name ,age , addhar card , pan etc . )

# # Encapsulation : class ( attribute + fucntions )
# class Person :
#     clg = "ITP" # class var 
#     def __init__(self,id , name  ):
#         self.id = id # instance var 
#         self.name = name # instance var 
    
#     def show(self):
#         print(f"id : = {self.id} , name : = {self.name} Clg name : = {self.clg}")

# p1 = Person(101,"aishu")
# p1.show()

# Person.clg = "abc"
# p2 = Person(102,"lalit")
# p2.show()

# student ( id , name ,age , addhar card , pan etc . )

# constructor in python : 
# type : 1] Default : without any parameter   
# 2] parametrized const : with parameters 
# class Person :
#     clg = "ITP" # class var 
#     # # default constructor 
#     def __init__(self): 
#         self.id = 11
#         self.name = "ketan"
#         print("default constructor ")
#         print(f"id : = {self.id} , name : = {self.name} ")

#     # note : only one in default and parameterized will work 

#     # # parameterized constructor 
#     def __init__(self , id , name ): 
#         self.id = id
#         self.name = name 
#         print("parameterized constructor ")
#         print(f"id : = {self.id} , name : = {self.name} ")
       
# p1 = Person(111,"aishu") # default constructor

# Inheritance :
    
# Need of INheritance : Use : for code reusability 
# inheritance is called as is-a relationship ( from child to base )
# [Base Class | parent class ] Person : id , name , age  , show()
# [child class ] : student(person) :, course 
# [child class ] :emp(person) :   , desi 
# [child class ] :manager(person) :   task 
# [child class ] :teacher(person)

# TYpes : 
# single Inheritance  : only one parent class and child class 
class Person :
    def __init__(self , name , age  ): 
        self.age  = age  
        self.name = name 
        print("Parent constructor ")
        
    def show(self):        
        print(f"name : = {self.name} , age : = {self.age} ")

class Student(Person) : 
    def __init__(self , name , age , rollno ):
        super().__init__(name,age)
        self.rollno = rollno 
        print("child constructor ")
    
    def display(self):
        print(f"rollno : = {self.rollno} name : = {self.name} , age : = {self.age} ")

# creating a obj of cild class is itself a obj of base class 
s = Student("aishu", 25 , 11)
s.show()
s.display()






