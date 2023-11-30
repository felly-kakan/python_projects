from calc import Calculator



a=float(input("a>" ))
b=float(input("b> ")) 

calculator1=Calculator(a,b)


addition=calculator1.add()
print(f"addition = {addition}" )

a=float(input("a>" ))
b=float(input("b> ")) 
calculator1=Calculator(a,b)

# calculator1.a=a
# calculator1.b=b

subtraction=calculator1.sub()
print(f"substraction={subtraction}")

a=float(input("a>" ))
b=float(input("b> ")) 
calculator1=Calculator(a,b)

multiplication=calculator1.mult()
print(f"multiplication = {multiplication}")

a=float(input("a>" ))
b=float(input("b> ")) 
calculator1=Calculator(a,b)

division=calculator1.div()
print(f"division = {division}")

# import calc

# a=float(input("a>" ))
# b=float(input("b> ")) 
# addition=calc.add(a,b)

# print(f"addition ={addition}")

# a=float(input("a>" ))
# b=float(input("b> ")) 
# subtraction=calc.sub(a,b)

# print(f"subtraction ={subtraction}")

# a=float(input("a>" ))
# b=float(input("b> ")) 
# multiplication=calc.mult(a,b)

# print(f"multiplication ={multiplication}")

# a=float(input("a>" ))
# b=float(input("b> ")) 
# division=calc.div(a,b)

# print(f"division ={division}")


