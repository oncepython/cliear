"""
cliear: A extremely simple CLI building tool.

Minimal, easy-to-use API for command line argument parsing.
Designed as a modern alternative to argparse.

Example:
>>> import cliear as cli
>>> c = cli.Cli(name="My first CLI")
>>> c.d("A simple CLI") # description
>>> c.a("name").h("Your name").b() # argument "name" with help string "Your name", set return type to bool
>>> c.d(True) # set default value to True
>>> c.s("group") # subcommand, just like git commit -m "message"
>>> c.e() # end of the subcommand definition
>>> c.x("arg1", "arg2") # mutex group


Still developing...
"""

__version__ = "0.0.1"
__author__ = "oncepython <hsxb2024@163.com>"
__license__ = "MIT"
__all__ = []
__authorsname__ = '*  * *** ***** ***\n* *   *  * * *  *\n**    *  * * *  *\n* *   *  * * *  *\n*  * *** * * * ***'