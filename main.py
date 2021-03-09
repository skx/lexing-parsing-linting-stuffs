#!/usr/bin/python3
#
# Trivial driver-script which will parse a simple "PHP-script", outputting
# only the two token-types we know about:
#
#   1.  Comments.
#
#   2.  Class definitions.
#


import lexer


input = """
    /* Class Bar is known for serving alcohol. */
    class Bar {
    }

    /* Class Foo reminds us that soft-drinks are also fine. */
    class Foo extends Bar {

      /* PHP code goes here */

      // Comment

      super!
    }

    /* Class Foo reminds us that soft-drinks are also fine. */
    class Baz extends Bar {

       // Oops I renamed here.  Copy pasting is bad!
    }

    /* Trailing comment - I'm not even closed!
"""


#
# Create a lexer object, giving it the input above
#
l = lexer.Lexer(input)

#
# Lex it
#
out = l.Lex()


#
# Show what we did found here.
#
for x in out:
    print( x )


print( "\n\n\n")
print( "Pretend we're linting now\n\n\n")

#
# If you wanted to look for class mismatches here's a trivial way
# of doing it
#
# NOTE: Here we start at the second index in our tokens.  This is fine,
# if the first entry is a class then there cannot be a comment ahead of
# it.  If the first entry is a comment it will be tested if the second is
# a class.
#
# We're just doing this to allow us to refer to the previous-token easily.
#
i = 1
while i < len(out):

    # Is this a class definition?
    if out[i]['type'] == 'class':

        # Get the name
        clazz = out[i]['name']
        print("Found class with name " + clazz)

        # If the previous thing is a comment
        if out[i-1]['type'] == 'comment':

            print("  The previous token was a comment.  Yay!")
            comment = out[i-1]['value']

            # And it mentions "class ..." then we'll test to see if
            # it has the name of the class in it
            if "class " in comment.lower():
                print( "  The comment refers to a class ..")
                if clazz in comment:
                    print( "  OK  : The comment refers to the expected class!")
                else:
                    print( "  FAIL: Comment does not refer to the expected class: " + clazz)
            else:
                print( "  The comment does not refer to a class")
    i += 1
