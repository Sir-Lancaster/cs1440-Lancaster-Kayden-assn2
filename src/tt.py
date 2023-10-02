#!/usr/bin/env python

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

from Concatenate import cat, tac
from CutPaste import cut, paste
from Grep import grep
from Partial import head, tail
from Sorting import sort
from WordCount import wc
from Usage import usage


if len(sys.argv) < 2:
    usage()
    sys.exit(1)
elif sys.argv[1] == 'cat':
    cat(sys.argv[2:])
elif sys.argv[1] == 'head':
    head(sys.argv[2:])
elif sys.argv[1] == 'grep':
    grep(sys.argv[2:])    
elif sys.argv[1] == 'wc':
    wc(sys.argv[2:])
elif sys.argv[1] == 'sort':
    sort(sys.argv[2:])
elif sys.argv[1] == 'tac':
    tac(sys.argv[2:])
elif sys.argv[1] == 'tail':
    tail(sys.argv[2:])

