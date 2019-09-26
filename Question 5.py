var1 = int(input("Enter first number: "))
var2 = int(input("Enter second number: "))

def hcf(var3, var4):
    if var3 > var4:
        smaller = var4
    else:
        smaller = var3
    for x in range(1, smaller + 1):
        if ((var3 % x == 0) and (var4 % x == 0)):
            hcf = x
    return hcf



print("The H.C.F. of the two number is", hcf(var1, var2))