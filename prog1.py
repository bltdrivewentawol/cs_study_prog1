#!/usr/bin/env python3

import sys


def DisplayHelp():
    """Displays the Help info at the command line."""
    
    print(
"""\
Usage: first_program.py [OPTIONS]

    -h        Display this help
    -a        Display the word: "Apple" 
""")

def DisplayApple():
    """Prints to the screen the word \"Apple\"."""
    print("Apple!\n")


# Main
if len(sys.argv) > 1:
    command_line_arguments_count = len(sys.argv)
    if (sys.argv[1] == '-h') or (sys.argv[1] == '--help'):
        DisplayHelp()
    elif (sys.argv[1] == '-a'):
        DisplayApple()

