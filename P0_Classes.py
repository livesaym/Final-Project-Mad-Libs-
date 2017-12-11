######################################################################
# Author: Matthew Livesay
# Username: livesaym
#
# Assignment: P0: Final Project
#
# Purpose: This is where the classes are held.
#
######################################################################

class Word:
    """
    The word class.
    """
    def __init__(self, type, index, word = "_____"):
        self.word = word
        self.type = type
        self.index = index
    def set_word(self, tipe):
        self.word = tipe

    def __repr__(self):
        return str(self.word)


class Mad_Lib:
    """
    Will contain the bulk of the story. The words placed in the story will involve using the "Word" class.
    """
    def __init__(self):
        self.lst = [Word("verb", 0), Word("noun", 1), Word("adjective", 2), Word("verb", 3), Word("adjective", 4), Word("place", 5), Word("verb", 6), Word("combatant", 7), Word("adjective", 8)] # Contains the list of spots that the user can put words into the story.
        self.Para = "Once upon a time the was a dragon who " + str(self.lst[0]) + " down a town. The king was very " + str(self.lst[1]) +\
                          ". He sent his " + str(self.lst[2]) + " knight to go and " + str(self.lst[3]) + " the dragon for what it had done. "\
                            "The knight travel for many " + str(self.lst[4]) + " days before finally reaching the " + str(self.lst[5]) + " where" \
                            " the dragon lived. They " + str(self.lst[6]) + " long and hard, but eventually, the " + str(self.lst[7]) + " won." \
                            " The people of the kingdom lived " + str(self.lst[8]) + " ever after."
    def finder(self):
        """
        Asks the user for what words it wants in the story based on their type. After this, it will
        have to go into the Word class and ask for input.
        :return:
        """
        for i in range (len(self.lst)):
            a_word = input("What " + self.lst[i].type + " should go in postion " + str(self.lst[i].index))
            self.lst[i].set_word(a_word)
    def assembler(self):
        """
        Puts the user-inputed words into the predefined paragraph.
        :return: The finished story.
        """
        self.Para = "Once upon a time the was a dragon who " + str(self.lst[0]) + " down a town. The king was very " + str(self.lst[1]) +\
                          ". He sent his " + str(self.lst[2]) + " knight to go and " + str(self.lst[3]) + " the dragon for what it had done. "\
                            "The knight travel for many " + str(self.lst[4]) + " days before finally reaching the " + str(self.lst[5]) + " where" \
                            " the dragon lived. They " + str(self.lst[6]) + " long and hard, but eventually, the " + str(self.lst[7]) + " won." \
                            " The people of the kingdom lived " + str(self.lst[8]) + " ever after."
        print(self.Para)


    def __repr__(self):
        return self.Para



