# php-class-comments

This repository contains a trivial piece of demonstration code, which is
to be used in my conjunction with my brief talk on parsing, lexing and
CI-linting


## Overview

There is a trivial lexer which will read a string which is expected to
contain PHP code, and turn that into a list of entries:

* Multi-line comments (i.e arbitrary text bound between `/*` and `*/`).
* Class definitions (i.e. "`class foo`").

The lexer is contained in [lexer.py](lexer.py).
