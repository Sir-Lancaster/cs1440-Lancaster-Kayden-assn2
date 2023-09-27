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

def head(args):
    """output the first part of files"""
    if sys.argv[4] is None:
        line_count = 10
    else:
        line_count = sys.argv[4]
    for filename in args:
        file = open(filename) 
        for line in file:
            print(line, end='')
            if line <= line_count:   #if statement will prevent the file from being read past the variable line_count.
                line += 1
        file.close()


def tail(args):
    """output the last part of files"""
    print("TODO: output the last part of files")
