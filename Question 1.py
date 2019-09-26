var=input("Enter a sentence:")

lowercase=0
uppercase=0
digit=0
characters=0
for x in var:

    if(x.islower()):
        lowercase = lowercase+1
    elif(x.isupper()):
        uppercase =uppercase+1
    elif(x.isdigit()):
        digit = digit+1
    else:
        characters = characters+1


print("The number of lowercase characters is:",lowercase)
print("The number of uppercase characters is:", uppercase)
print("The number of digit is:", digit)
print("The number of character is:", characters)
