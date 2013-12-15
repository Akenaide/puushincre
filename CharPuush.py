"""
Created on 7 August 2013

@author: KMS
"""
import string

class CharPuush():
    """
    classdocs
    """

    def __init__(self, char):
        """
        param : char : a character alphanumeric

        """
        self.listChar = list(string.ascii_letters)
        self.listChar.extend(string.digits)
        self.index = self.listChar.index(char)

    def incre (self):
        good = False
        self.index += 1
        if self.index >= len(self.listChar):
            self.index = 0
            good = True
        return good
        
    def get_value(self):
        return self.listChar[self.index]
    
    def __repr__(self):
        return self.listChar[self.index]
    