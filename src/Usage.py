#              Copyright © 2023 DuckieCorp. All Rights Reserved.
#
#                       __      Redistribution and use of this code, with or
#                     /` ,\__   without modification, are permitted provided
#                    |    ).-'  that the following conditions are met:
#                   / .--'
#                  / /          0. Redistributions of this code must retain
#    ,      _.==''`  \             the above copyright notice, this list of
#  .'(  _.='         |             conditions and the following disclaimer.
# {   ``  _.='       |          1. The name of the author may not be used to
#  {    \`     ;    /              endorse or promote products derived from
#   `.   `'=..'  .='               this software without specific prior written
#     `=._    .='                  permission.
#  jgs  '-`\\`__                2. Neither the name of the University nor the
#           `-._{                  names of its contributors may be used to
#                                  endorse or promote products derived from
#                                  this software without specific prior written
#                                  permission.

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !! YOU DO NOT NEED TO EDIT THIS FILE TO COMPLETE THE ASSIGNMENT !!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


CAT = """tt.py cat|tac FILENAME...
    Concatenate and print files in order or in reverse"""

CUT = """tt.py cut [-f LIST] FILENAME...
    Remove comma-separated sections from each line of files
    -f  List of comma-separated integers indicating fields to output (default LIST=1)"""

PASTE = """tt.py paste FILENAME...
    Merge lines of files into one comma-separated text"""

GREP = """tt.py grep [-v] PATTERN FILENAME...
    Print lines of files matching PATTERN
    -v  Invert matching; print lines which DO NOT match PATTERN"""

HEAD = """tt.py head|tail [-n N] FILENAME...
    Output the first or last part of files
    -n  Number of lines to print (default N=10)"""

SORT = """tt.py sort FILENAME...
    Output lines of text file in sorted order"""

WC = """tt.py wc FILENAME...
    Print newline, word, and byte counts for each file"""


def usage(error=None, tool=None):
    """Provide a unified error reporting interface"""
    # Print a specific error message, if requested
    if error is not None:
        print(f"Error: {error}\n")

    # Print a tool-specific message where possible; otherwise, display
    # instructions for all tools
    if tool == 'cat' or tool == 'tac':
        print(f"\t{CAT}")
    elif tool == 'cut':
        print(f"\t{CUT}")
    elif tool == 'paste':
        print(f"\t{PASTE}")
    elif tool == 'grep':
        print(f"\t{GREP}")
    elif tool == 'head' or tool == 'tail':
        print(f"\t{HEAD}")
    elif tool == 'sort':
        print(f"\t{SORT}")
    elif tool == 'wc':
        print(f"\t{WC}")
    else:
        print("Python Text Tools Usage:\n========================",
              CAT, CUT, PASTE, GREP, HEAD, SORT, WC,
              sep="\n\n", end="\n\n")
