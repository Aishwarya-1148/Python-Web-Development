# abstraction in python 

from abc import abc , abstractmethod #[abc=abstract base class] this import is standard one.
#class is called as abstarct class when there is atleast one abstract-method present.it can be more than one as well.
class Shape(abc):
    @abstractmethod
    def area():
       pass


class Square(Shape):
    



class Circle(Shape):
    def __init__(self , r ):
        self.r = r 
        
    def area(self):
        print("cicle is : = ",3.14 * self.r * self.r )
        
c = Circle(5)
c.area()







