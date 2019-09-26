var = input("Enter a word: ")
name_length = len(var)

while True:
    if name_length >2 :
        var1 = (var[:2])
        var2 = (var[-2:])

        value = str(var1) + str(var2)
        print(value)
        break
    else:
        print("Invalid,please enter again.")
        var = input("Enter a word: ")
        name_length = len(var)