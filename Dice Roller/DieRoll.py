import random

sidesOfADie = (1, 2, 3, 4, 5, 6)
choice = ''

while (choice != 'N' and choice != 'n'):
    choice = raw_input("Would you like to roll the die? (Y/N): \n")
    if (choice == 'Y') or (choice == 'y'):
        print sidesOfADie[random.randint(0, 5)]
    elif ((choice == 'N') or (choice == 'n')):
        break
    else:
        print "Please enter a valid response to the prompt."

print "Thank you for using this dice roller."
