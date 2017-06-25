import random

story1 = """Zeus, the ___ of the Gods, was married to a nice ____ woman named Metis. But one day, his ____""" \
         """_____ told him that when Metis had a _____, it would overthrow him. He was very ____. Soon, when""" \
         """Metis was transforming into various ____, she ____ into a dragonfly, and Zeus ate her. Metis ___""" \
         """inside of Zeus' head for a very long time. Eventually, she had her baby and the ____ began to""" \
         """grow older. Metis taught her daughter about ____ and ____. One day, the inside of Zeus' head""" \
         """became too ____ for both of them to live in, and Zeus got a headache. He ____ his _____ and asked""" \
         """them to split his ____ open to get out whatever was hurting him. They split open his ___ and out""" \
         """came Metis' _____: the goddess Athena."""

stories = (story1) #Make it a tuple so it is immutable

####Here's the code itself (there are no block comments in Python):
def main():
    print "Right, so let's play Mad Libs! Here, I've got a few stories with blanks. Fill in the blanks with" \
        "whatever you would like and I'll tell you the resultant story. Remember, order matters!"

    whichStory = stories[random.randint(0, len(stories))] #Random index into which story to pick
    num = numberOfBlanks(whichStory)
    print num

def numberOfBlanks(story):
    blanks = 0 #Number of blanks in story
    for i in story:
        print i
        fill = False #Set to true if we have found a possible blank
        if i == "_" and i-1 == ' ': #Sign of a possible blank
            fill = True
            while i==' ': #Now keep iterating across this possible blank
                if i != '_': #If you run across something that is not an underscore
                    fill = False
                    break
            if fill: #If it was a blank
                blanks += 1 #Then we found a blank
    return blanks

if __name__ == "__main__": main() #Execute main, which is the true functionality of the code