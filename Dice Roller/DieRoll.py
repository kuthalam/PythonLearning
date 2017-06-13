# to print to the console: print "Hello, Python!"
# Here's an if, else statement:
    #if (True):
        #do something
    #elif (False):
        #do other thing
#Anywhere from one to three quotes can be used for strings, but 3 is usually for multi-line strings
#word = 'word', sentence = "This is a sentence"
    #multiLine = """I'm gonna span
                 #multiple lines"""
#And in case you haven't noticed yet, the (#) is for comment. But you already knew that
#import sys for basic I/O
#Oh, the most irritating thing of all: NO SEMICOLON. New lines mark the end of statements, and semicolons
    #exist only for the sake of a series of statements on the same line
#Here's a close second though: NO BRACES. A block of code is denoted by tabs (you probably noticed) and
    #the block (suite) starts with a colon after the beginning statement (by that, I mean if(condition),
    #while(condition)). See my if statement above for an example.
#Also, "else if" is "elif" in Python
#Explicit declaration for variables is unnecessary. Ex:
    #count = 10; name = "Mark"
    #Believe it or not, you can even do this: count, name = 10, "Mark" (Imo, Do yourself a favor
    # and just don't)
    #Variable names are references - meaning you can delete these references (Ex. del count)
#Overall types: Numbers, String, List, Tuple, Dictionary
    #Numbers subtypes: int, long (Use L to denote this), float, complex (yes, I mean like 4 + 5j)
#Finally, something familiar: Strings are like arrays.
    #print str #print whole string
    #print str[0] #print the first char
    #print str[2:5] #print characters 3 to 5
    #print str * 2 #print string twice
    #Yes, + is concatenation
#Lists work pretty much the same way
    #list = ['Multiple', 10, 'data', 100.7, 'types', 1000.5, 'allowed']
#While lists are dynamic (like Arraylists), tuples are not. They are VERY static. Can't change the
    # elements, nor the size. They're like Read-Only Lists
    #tuple = ("Oh", 10, "and", 100.5, "use", 1000.6, "parentheses")
#Dictionaries are like hash tables and can be just about any type, but are usually numbers and/or strings
    #tinydict = {'key':'value', 'one': 1, 'ECE': 'Enjoyable torture'}
#Plenty of functions for converting between data types, but you're not expecting me to list those, right?

#Arithmetic operators are supported, but here are a couple new ones: ** for exponent and // for
    # "floor division"
    # 10**20 is "10 to the power of 20"
    # // works a little strangely. If you're dividing postive numbers, divide and drop the fractional
    # part. But if you're throwing a negative, the result is floored (rounded toward negative infinity)
    # 9//2 = 4, and -11/3 = -4 (TODO: Come up with a "floored" example later)
#Comparison operators work like normal, thank God
#Yes, you can combine arithmetic and assignment operators (Ex. += or **=)
#Bitwise operators are also supported (&, ||, ^, ~, <<, and >>)
