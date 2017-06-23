import random

story1 = "Zeus, the ___ of the Gods, was married to a nice ____ woman named Metis. But one day, his ____" \
         "_____ told him that when Metis had a _____, it would overthrow him. He was very ____. Soon, when" \
         "Metis was transforming into various ____, she ____ into a dragonfly, and Zeus ate her. Metis ___" \
         "inside of Zeus' head for a very long time. Eventually, she had her baby and the ____ began to" \
         "grow older. Metis taught her daughter about ____ and ____. One day, the inside of Zeus' head" \
         "became too ____ for both of them to live in, and Zeus got a headache. He ____ his _____ and asked" \
         "them to split his ____ open to get out whatever was hurting him. They split open his ___ and out" \
         "came Metis' _____: the goddess Athena."

stories = (story1) #Make it a tuple so it is immutable
blanks = 0 #Number of blanks in story

####Here's the code itself (there are no block comments in Python):
print "Right, so let's play Mad Libs! Here, I've got a few stories with blanks. Fill in the blanks with" \
      "whatever you would like and I'll tell you the resultant story. Remember, order matters!"
whichStory = stories[random.randint(0, len(stories))] #Random index into which story to pick

## Now iterate over the story to find number of words needed
for i in whichStory:
    if i != 0 and i-1 == ' ' 