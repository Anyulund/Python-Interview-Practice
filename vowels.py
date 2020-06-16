#Write a function to remove vowels from a string

string = "It takes a lot of courage to show your dreams to someone else."

#----------------------------------------------------- 1st attempt------------------------------------------------------------
'''
def RemoveVowels(string):   # how do you put input here? You put input into the function into parentheses after naming it

    consonants_list = ['b','c','d'] #not efficient strategy because the number of vowels is smaller than the number of consonants
    #Use tuple instead of a list. Actually need to check and see if it matters here.
    redacted_string = []
    #maybe need to do split function to split words. No need - we are just checking for letters thats it.
    for word in string: #for-if structure is good. Good job!
        if letter in consonants_list
        append #instead of removing and appending, simply replace the vowel with a space.
        if letter is not
        next

    return string
'''
#-----------------------------------------------------2nd attempt--------------------------------------------------------------
'''
# Python program to remove vowels from a string
# Function to remove vowels
def rem_vowel(string):
    vowels = ('a', 'e', 'i', 'o', 'u')  #Check if it runs with a list
    for x in string.lower():
        if x in vowels:
            string = string.replace(x, "")

    # Print string without vowels
    print(string) #don't have to return anything - simply print

# Driver program

rem_vowel(string)
'''
#------------------------------------------------------3rd attempt--------------------------------------------------------------

# Python program to remove vowels from a string
# Function to remove vowels

# import the module for regular expression (re)
import re
def rem_vowel(string):
    return (re.sub("[aeiouAEIOU]","",string))

# Driver program
print (rem_vowel(string))
