class Student:
    name = "aishwarya"
    
    def __init__(self , name ):
        Student.name = name 

    @classmethod
    def changeName(cls):
        cls.name = "xyz" 
        
   
s = Student("abc")
Student.changeName()
print("the class var name is : = ",Student.name )        
