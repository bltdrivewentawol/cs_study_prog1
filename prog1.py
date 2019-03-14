# -*- coding: utf-8 -*-
#
# Authors:
# Jonathan Duff <jonathan@intertechsci.com>
"""This is an educational script to learn and to test Python features"""

import sys
import prog1_help
import prog1_apple
import prog1_bannana

# Main command line
if len(sys.argv) > 1:

    command_line_arguments_count = len(sys.argv)
    
    if (sys.argv[1] == '-h') or (sys.argv[1] == '--help'):
        prog1_help.DisplayHelp()
        
    elif (sys.argv[1] == '-a') or (sys.argv[1] == '--apple'):
        prog1_apple.DisplayApple()

    elif (sys.argv[1] == '-b') or (sys.argv[1] == '--bannana'):
        prog1_bannana.DisplayBannana()

# User interaction
