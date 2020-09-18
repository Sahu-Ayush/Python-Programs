# Private Access Modifier

# program to illustrate private access modifier in a class 
  
class Student:

     # private members 
     __name = None
     __roll = None
     __branch = None

     # constructor
     def __init__(self, name, roll, branch):
          self.__name = name
          self.__roll = roll
          self.__branch = branch

     # private member function   
     def __displayDetails(self):

           # accessing private data members
           print("Name: ", self.__name) 
           print("Roll: ", self.__roll)
           print("Branch: ", self.__branch)

     # public member function
     def accessPrivateFunction(self):

           # accesing private member function
           self.__displayDetails()

# Derived class
class Child(Student):
    def __init__(sefl, name, roll, branch):
        super().__init__(name, roll, branch)

    def m():
        super().__displayDetails(self)

           
# creating object
obj = Student("R2J", 1706256, "Information Technology")

# calling public member function of the class 
obj.accessPrivateFunction()

####

c = Child()
c.__displayDetails()
