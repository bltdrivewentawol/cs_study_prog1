#!/usr/bin/env python3

import sys

def DisplayHelp():
    print(
"""\
Usage: first_program.py [OPTIONS]

    -h        Display this help
    -a        Display the word: "Apple" 
""")

def DisplayApple():
    print("Apple!\n")

# Main

#print("The size of sys.argv = ", len(sys.argv), "\n")

if len(sys.argv) > 1:
    command_line_arguments_count = len(sys.argv)
    if (sys.argv[1] == '-h') or (sys.argv[1] == '--help'):
        DisplayHelp()
    elseif (sys.argv[1] == '-a'):
        DisplayApple()

# tmp1: this is testing the branch and checkout. this message should only
#       be visible on branch: tmp1.
