import random

again = 'Y'  # Again, no need to declare types (this feels so weird)
score = 0  # A value for keeping track of player's score
numOfGuesses = 0
upperBound = (100)
lowerBound = (0)  # Defined as tuples to mimic constants

while (again == 'Y' or again == 'y'):
    value = random.randint(lowerBound, upperBound)  # Random value generation
    number = raw_input("Guess a number between 0 and 100: ")

    try:
        number = int(number)  # Try converting to an int
    except ValueError:
        print "That doesn't seem to be an integer. Please try again."
        continue  # Go back to the top of the loop

    if ((number < lowerBound) or (number > upperBound)):
        print "This number is not within the correct range. Please enter an appropriate value."

    else:
        numOfGuesses += 1
        if (number == value):
            print "Congrats! You got that right."
            score += 1  # I don't know which dude decided this, but post-increment is not a thing
        else:
            print "Ah, sorry. That isn't the generated value. Try again!"
        print "Here's your score so far: " + str(score) + "/" + str(numOfGuesses)
        # Need to convert int to string before concatenation
        again = raw_input("So...want to try again? (Y/N): ")
        if (again == 'N' or again == 'n'):
            print "Kay, see you again sometime! Unless the game is too frustrating :("
