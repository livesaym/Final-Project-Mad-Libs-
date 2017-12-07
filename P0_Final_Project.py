######################################################################
# Author: Matthew Livesay
# Username: livesaym
#
# Assignment: P0: Final Project
#
# Purpose: Similar to the "Mad Libs" assignment, but improved with
#           classes.
######################################################################
from P0_Classes import Mad_Lib

def main():
    para = Mad_Lib()
    print (para)
    print ("Now, fill in the blanks of the story!")
    para.finder()
    para.assembler()

main()
