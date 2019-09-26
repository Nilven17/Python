a = input("Number1: ")
b = input("Number2: ")

def add():
    result1 = int(a) + int(b)
    return result1

def sub():
    result2 = int(a) - int(b)
    return result2

def mul():
    result3 = int(a) * int(b)
    return result3

def div():
    result4 = int(a) / int(b)
    return result4

var1 = add()
var2 = sub()
var3 = mul()
var4 = div()

print("Adddition=",var1)
print("Subtraction=",var2)
print("Multiplication=",var3)
print("Division=",var4)