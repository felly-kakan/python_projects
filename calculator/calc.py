import math

''''''
class Calculator:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
        


    def add(self):
      return self.a+self.b
    
    def sub(self):
       return self.a-self.b
    
    def mult(self):
       return self.a*self.b
    
    def div(self):
       if self.b !=0:
         return self.a/self.b
       else:
          return (f"{self.a} cannot be divided by zero")
# def add(a,b):
#     return a+b

# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def mult(a,b):
#     return a*b

# def div(a,b):
#     if b !=0:
#         return a/b
#     else:
#         return (f"{a} cannot be divided by zero")
    









    