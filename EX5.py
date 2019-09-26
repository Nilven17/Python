def swap(string_one, string_two):
    return string_two, string_one


var1 = input("Enter a word: ")
var2 = input("Enter a second word: ")


var1, var2 = swap(var1, var2)

var4 = str(var1[:-1])+ str(var2[2:])
var5 = str(var2[:-1]) + str(var1[2:])

print(var4,var5)
