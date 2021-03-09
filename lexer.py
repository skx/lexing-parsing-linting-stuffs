"""
This is a simple lexer for PHP classes.

It was written solely to accomplish my talk on CI-based tests,
using parsing, lexing, and CI-tests.

"""

class Lexer:
    """
    Lexer is a simple lexer class which will read a given piece of
    input and return only a list of two things:

    - C++-style comments (i.e. "/* Foo */")
    - Class names
    """

    # instance data
    input = ""
    len = 0
    i = 0

    def __init__(self, input):
        """
        Constructor.
        """
        self.input = input
        self.len = len(input)
        self.i = 0


    def Lex(self):
        """
        Convert our input into a series of tokens.

        Only two types are recognized - classes and comments
        """

        # Things we return to the caller
        tokens = list()

        while self.i < self.len:

            # Is this a "/*" ?  Then read a comment
            if self.input[self.i] == '/' and \
               self.i+1 < self.len  and \
               self.input[self.i+1] == '*' :
                tokens.append( self.read_comment() )
                continue

            # Is it a class token?
            if ( self.i + len("class ") < self.len ):
                if self.input[self.i + 0 ] == 'c' and \
                   self.input[self.i + 1 ] == 'l' and \
                   self.input[self.i + 2 ] == 'a' and \
                   self.input[self.i + 3 ] == 's' and \
                   self.input[self.i + 4 ] == 's' and \
                   self.input[self.i + 5 ] == ' ':
                      tokens.append( self.read_class_name() )
                      continue

            # next position - something we don't care about.
            self.i+= 1

        # parsing is over now.
        return tokens




    def read_comment(self):
        """
        Read a comment.

        At this point we're called with the index set to "/", the next
        character is "*", and so we read until we hit "*/"
        """

        # Bump over "/" + "*" (i.e. two characters)
        self.i += 2

        # The comment we'll return
        comment = dict()
        comment['type'] = 'comment'
        comment['value'] = ''

        while( self.i < self.len ):

            # Is this the end of the comment?
            if self.input[self.i] == '*' and \
               self.i+1 < self.len and \
               self.input[self.i+1] == '/':
                  self.i += 2
                  return comment
            else:
                # otherwise append the character to the currently open comment
                comment['value'] += self.input[self.i]

            self.i += 1

        return comment


    def read_class_name(self):
        """
        Read a class.

        At this point we're called with the index set to "c", and we
        know that we've got "lass " coming next.  Just read the next
        token until we hit whitespace.
        """

        # Bump over "class"
        self.i += len("class")

        clazz = dict()
        clazz['type'] = 'class'
        clazz['name'] = ''

        #
        # skip over any space between the "class" token, and the name
        # of the class.  We know we'll get at least one space since we've
        # previously tested for "class ".
        #
        while( self.i < self.len ):
            if self.input[self.i].isspace():
                self.i += 1
            else:
                break


        #
        # Build up ANY character until we hit whitespace, even if that
        # might not necessarily make sense.
        #
        while( self.i < self.len ):

            # hit space?  That's the end.
            if self.input[self.i].isspace():
                self.i += 1
                return clazz
            else:
                clazz['name'] += self.input[self.i]
                self.i += 1

        return clazz
