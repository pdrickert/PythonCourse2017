# Create the following functions: with exceptions, errors, and such
# Create a test for those functions



#Hello. to HELLO!
def shout(txt):
        if type(txt) is str:
            txt = txt.replace(".", "!")
            new_txt = txt.upper()
            return new_txt
        else:
            raise Exception, "TypeError: Enter a string."

# Name to emaN
def reverse(txt):
    try:
        if type(txt) is str:
            if " " in txt:
                raise Exception, "SpaceError: String cannot have more than one word."
            else:
                new_txt = txt[::-1]
                return new_txt
        else:
            raise TypeError
    except TypeError:
        raise TypeError, "Please enter a string"
    else:
        print "Hey this is the end block"

# Hello world! to world! Hello

def reversewords(txt):
    if type(txt) is str:
        wordlist = txt.split( )
        new_txt = wordlist[1] + " " + wordlist[0]
        return new_txt
    else:
        raise Exception, "TypeError: Please enter a string"


# Hello world! to !dlrow olleH
def reversewordletters(txt):
        if type(txt) is str:
            new_txt = txt[::-1]
            return new_txt
        else:
            raise Exception, "TypeError: Please enter a string"





# Take a word and transfer to pig latin
