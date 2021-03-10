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


## Sample Output

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


## Bonus Links

I maintain a small collection of sysadmin-tools called [sysbox](https://github.com/skx/sysbox), packaged as a single binary.

One of the subcommands allows extraction of comments from multiple languages, as described in this blog-post:

* [I'm a bit of a git (hacker?)](https://blog.steve.fi/i_m_a_bit_of_a_git__hacker__.html)

As a result of using this tool I submitted a couple of spelling-mistakes to comments in the `git` tool:

* https://github.com/git/git/commit/538bb8286a9d3f7c8a99d5c06f0ba617de99af38
