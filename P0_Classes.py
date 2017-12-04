######################################################################
# Author: Matthew Livesay
# Username: livesaym
#
# Assignment: P0: Final Project
#
# Purpose: This is where the classes are held.
#
######################################################################

class Verb:
    """
    The "Verb" class.
    """
    def __init__(self):
        self.word = input("Please input a verb.")
        self.len = len(self)

    def past_tensify(self):
        """Makes the varb past-tense."""
        if self.find("e") == self.len:
            new_verb = self.word[:999] + "d"
        else:
            new_verb = self.word[:999] + "ed"
        return new_verb


    def present_tensify(self):
        """Makes the verb present-tense."""
        new_verb = self.word[:999] + "ing"
        return new_verb

    def future_tensify(self):
        """Makes the verb future-tense."""
        new_verb = "will" + self.word[:999]

