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

def cut(args):
    """remove sections from each line of files"""
    if args[0] == '-f':
        fields = args[1].split(',')
    else:
        fields = ['1']
    for filename in args[2:]:
        file = open(filename)
        for line in file:
            line = line.strip()
            parts = line.split(',')
            selected_fields = [parts[i - 1] for i in map(int, fields)]
            print(','.join(selected_fields))
        file.close()


def paste(args):
    """merge lines of files"""
    print("TODO: merge lines of files")
