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
    for filename in args:
        try:
            with open(filename, 'r') as file:
                for line in file:
                    if sys.argv[3].isnumeric():
                        SearchPattern = sys.argv[4]
                    else:
                        SearchPattern = sys.argv[3]
                    if SearchPattern is None or SearchPattern in line:
                        print(line, end='')
        except FileNotFoundError:
            print(f"grep: {filename}: No such file or directory")