class Student:
     school = "AkiraChix"
     def __init__(self,firstName,LastName,age):
         self.firstName = firstName
         self.LastName =LastName
         self.age = age
     def speak(self):
        return f"Hello class, my name is {self.name}"  
     def birthday(self):  
        return f"hello class,my name is {self.age}"  
     def greet(self):
        return f"Hello{self.firstName} welcome to {self.school}"

    
        