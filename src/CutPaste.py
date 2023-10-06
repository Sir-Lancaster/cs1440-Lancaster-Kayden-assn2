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
            
            # Ensure that the indices in 'fields' are valid
            selected_fields = []
            for field_index in map(int, fields):
                if 1 <= field_index <= len(parts):
                    selected_fields.append(parts[field_index - 1])
                else:
                    selected_fields.append('')  # Add an empty field for out-of-range indices
            
            print(','.join(selected_fields))
        file.close()


    """merge lines of files"""
def paste(args):
    # Initialize an empty list to store the lines from each file
    lines = []

    # Read lines from each file and append them to the 'lines' list
    for file_path in args:
        with open(file_path, 'r') as current_file:
            current_lines = current_file.readlines()
            lines.append(current_lines)

    # Determine the maximum number of lines among all files
    max_lines = max(len(lines[i]) for i in range(len(lines)))

    # Pad shorter files with empty lines if necessary
    for i in range(len(lines)):
        while len(lines[i]) < max_lines:
            lines[i].append('\n')

    # Paste the lines together with a tab delimiter and print the result
    for i in range(max_lines):
        combined_line = '\t'.join(lines[j][i].rstrip('\n') for j in range(len(lines)))
        print(combined_line)

