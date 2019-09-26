var = input("Enter a sentence: ")
character_frequency= {}

for z in var:
    if z in character_frequency:
        character_frequency[z] +=1

    else:
        character_frequency[z]= 1

print(character_frequency)