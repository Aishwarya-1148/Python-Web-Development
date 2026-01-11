# Fully Encapsulated class ( All attribute should be Private and all method by which we are accessing the values of class should be with Getters and Setters ) 

class BankAccount:
    
    def __init__(self , accNo , name , balance ):
        self.__accNo = accNo
        self.__name = name
        self.__balance = balance 
        
    # ------- Getters : To Return teh values of Obj Attributes 
    def getAccNo(self):
        return self.__accNo # only value of private data member is returned 
    
    def getName(self):
        return self.__name # only value of private data member is returned 
    
    def getBalance(self):
        return self.__balance # only value of private data member is returned 
    
    # ------- Setters : to set the values for obj Attributes
    def setAccNo(self ,accNo ):
        self.__accNo = accNo
        
    def setName(self , name ):
        self.__name = name 
        
    def setBalance(self , balance):
        self.__balance = balance

    # regular show method 
    def show(self):
        print(f"id = {self.__accNo} , name = {self.__name} , balance = {self.__balance}")

ba = BankAccount(12345 , "lalit" , 100000)
ba.setAccNo(67890)
ba.setName("Lalu")
ba.setBalance(-1000)
# ba.show()

# print(f"The Id = {ba.getAccNo()} whos name is : = {ba.getName()} and Hes balance is = {ba.getBalance()}") # Allowed becuase methods are Retuning the values 

# print(f"The Id = {ba.setAccNo()} whos name is : = {ba.setName()} and Hes balance is = {ba.setBalance()}")# Not Allowed becuase methods are not  Retuning the values 


