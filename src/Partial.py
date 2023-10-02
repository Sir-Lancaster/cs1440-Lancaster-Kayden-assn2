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
    line_count = 10  # Default line count

    if len(sys.argv) > 2 and sys.argv[1] == '-n':
        try:
            line_count = int(sys.argv[2])  # Get the line count from the command line arguments
        except ValueError:
            print("Using the default line count of 10.")
        args = args[1:]  # Remove the first two command-line arguments (-n and the line count)

    for filename in args:
        with open(filename) as file:
            lines_read = 0
            for line in file:
                print(line, end='')
                lines_read += 1
                if lines_read >= line_count:
                    break  # Stop reading after reaching the specified line count



def tail(args):
    line_count = 10  # Default line count

    if len(args) > 2 and args[0] == '-n':
        try:
            line_count = int(args[1])  # Get the line count from the command-line arguments
        except ValueError:
            print("Using the default line count of 10.")
        args = args[2:]  # Remove the first two command-line arguments (-n and the line count)

    for filename in args:
        lines = []  # Initialize an empty list to store the last N lines
        with open(filename) as file:
            for line in file:
                lines.append(line)  # Append each line to the list
                if len(lines) > line_count:
                    lines.pop(0)  # Remove the first line if the list exceeds N lines
        for line in lines:
            print(line, end='')