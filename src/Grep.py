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

def grep(args):
    """
    Search for a pattern in multiple files and print matching or non-matching lines based on options.
    """

    pattern = args[0]
    option = None
    filenames = []

    if args[0] in ['-f', '-v']:
        option = args[0]
        pattern = args[1]
        filenames = args[2:]
    else:
        filenames = args[1:]

    for filename in filenames:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if option == '-f':
                    if pattern in line:
                        print(line)
                elif option == '-v':
                    if pattern not in line:
                        print(line)
                else:
                    if pattern in line:
                        print(line)

