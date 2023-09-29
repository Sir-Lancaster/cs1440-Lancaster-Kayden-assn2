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

def sort(args):
    """sort lines of text files"""
    lines = []

    # Read lines from each file and store them in the 'lines' list
    for filename in args:
        file_lines = []
        with open(filename) as file:
            for line in file:
                file_lines.append(line)
        lines.extend(file_lines)

    # Sort the lines alphabetically
    sorted_lines = sorted(lines)

    # Print the sorted lines to the standard output
    for line in sorted_lines:
        print(line, end='')


if __name__ == '__main__':
    sort(sys.argv[1:])