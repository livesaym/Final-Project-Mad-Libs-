######################################################################
# Author: Matthew Livesay
# Username: livesaym
#
# Assignment: P0: Final Project
#
# Purpose: This is where the classes are held.
#
######################################################################

# class Verb:
#     """
#     The "Verb" class.
#     """
#     def __init__(self):
#         self.verb = input("Please input a verb.")
#
#
#     def past_tensify(self):
#         """Makes the verb past-tense."""
#         if self.verb[-1] == "e":
#             new_verb = self.verb[:-1] + "d"
#         else:
#             new_verb = self.verb[:-1] + "ed"
#         return new_verb
#
#
#     def present_tensify(self):
#         """Makes the verb present-tense."""
#         new_verb = self.verb[:999] + "ing"
#         return new_verb
#
#     def future_tensify(self):
#         """Makes the verb future-tense."""
#         new_verb = "will" + self.verb
#         return new_verb

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


class Paragraph:
    """
    Will contain the bulk story. The words placed in the story will involve using the "Word" class.
    """
    def __init__(self):
        self.lst = [Word("verb", 0), Word("noun", 1), Word("adjective", 2), Word("verb", 3)] # Contains the list of potential words that can be put in the story.
        self.Para = "Once upon a time the was a dragon who " + str(self.lst[0]) + " down a town. The king was very " + str(self.lst[1]) +\
                          ". He sent his " + str(self.lst[2]) + " soldier to go and " + str(self.lst[3]) + " the dragon for what it had done. "\
                            "Then that happened. "
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
        :return:
        """
        self.Para = "Once upon a time the was a dragon who " + str(self.lst[0]) + " down a town. The king was very " + str(self.lst[1]) +\
                          ". He sent his " + str(self.lst[2]) + " soldier to go and " + str(self.lst[3]) + " the dragon for what it had done. "\
                            "Then that happened. "
        print(self.Para)


    def __repr__(self):
        return self.Para



