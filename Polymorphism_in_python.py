# polymorphims = poly(many ) + morphims(form )
# types of polymorphis : 1] compile time 2] run time 
# file => compile -> bytecode -> execution
#1. compile time : doesnt supported (mimic *args/**kwargs)
'''
2. run time : 
    1] method overriding 
    2] operator overloding 
    3] duck typing
'''

'''
method overriding : child class method will be overriden 
Method overriding in Python occurs when a subclass defines a method with the same name and parameters as a method in its parent class, thereby replacing (overriding) the parent class’s method behavior.

The version of the method that gets executed is determined at runtime, based on the object’s type, not the reference — making it a form of runtime polymorphism.
'''
class Vehicle :
    def start(self ):
        print("vehicle is started")
        
    def fuelType(self):
        print("vehicle uses fuel petrol/diesel ")

class Car(Vehicle):
    def start(self):
        print("Car is started")
        
    def fuelType(self):
        print("Car uses fuel petrol/diesel ")
        
# v = Vehicle()
# v.start()
# v.fuelType()

c = Car() # method overriding 
c.start()
