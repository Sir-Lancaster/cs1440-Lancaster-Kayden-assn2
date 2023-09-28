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

def wc(files):
    """print newline, word, and byte counts for each file"""
    for filename in files:
        newline_count = 0
        char_count = 0
        word_count = 0

        with open(filename) as file:
            for line in file:
                newline_count += 1
                char_count += len(line)
                word_count += len(line.split())

        print("File:", filename)
        print("Newline count:", newline_count)
        print("Word count:", word_count)
        print("Character count:", char_count)
        print()

        file.close()


if __name__ == '__main__':
    wc(sys.argv[1:])