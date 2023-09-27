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

import sys

def cat(args):
    """concatenate files and print on the standard output"""
    for filename in args:
        file = open(filename)  # Just let open() crash if filename is invalid
        for line in file:
            print(line, end='')
        file.close()



def tac(args):
    """concatenate and print files in reverse"""
    print("TODO: concatenate and print files in reverse")

if __name__ == '__main__':
    cat(sys.argv[1:])                # skips argv[0] of the array.
    