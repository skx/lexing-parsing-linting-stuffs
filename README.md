# php-class-comments

This repository contains a trivial piece of demonstration code, which is
to be used in my conjunction with my brief talk on parsing, lexing and
CI-linting


## Overview

There is a trivial lexer which will read a string which is expected to
contain PHP code, and turn that into a list of entries:

* Multi-line comments (i.e arbitrary text bound between `/*` and `*/`).
* Class definitions (i.e. "`class foo`").

The lexer is contained in [lexer.py](lexer.py) and was written with the intention it would be easy to understand, rather than efficient.

There's a driver in [main.py](main.py) which will let you see output:

```
frodo ~/Repos/github.com/skx/php-class-comments $ ./main.py
{'type': 'comment', 'value': ' Class Bar is known for serving alcohol. '}
{'type': 'class', 'name': 'Bar'}
{'type': 'comment', 'value': ' Class Foo reminds us that soft-drinks are also fine. '}
{'type': 'class', 'name': 'Foo'}
{'type': 'comment', 'value': ' PHP code goes here '}
{'type': 'comment', 'value': ' Class Foo reminds us that soft-drinks are also fine. '}
{'type': 'class', 'name': 'Baz'}
{'type': 'comment', 'value': " Trailing comment - I'm not even closed!\n"}




Pretend we're linting now



Found class with name Bar
  The previous token was a comment.  Yay!
  The comment refers to a class ..
  OK  : The comment refers to the expected class!
Found class with name Foo
  The previous token was a comment.  Yay!
  The comment refers to a class ..
  OK  : The comment refers to the expected class!
Found class with name Baz
  The previous token was a comment.  Yay!
  The comment refers to a class ..
  FAIL: Comment does not refer to the expected class: Baz

```
