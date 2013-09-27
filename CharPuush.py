'''
Created on 7 août 2013

@author: KMS
'''
import string

class CharPuush():
    '''
    classdocs
    ''' 
    index = 0
    listChar = list(string.ascii_letters)
    listChar.extend(string.digits)
    
    def __init__(self, char):
        '''
        Constructor
        '''
        self.index = self.listChar.index(char)

    def incre (self):
        good = False
        self.index += 1
        if (self.index >= len(self.listChar)):
            self.index = 0
            good = True
        return good
        
    def getValue(self):
        return self.listChar[self.index]
    
    def __repr__(self):
        return self.listChar[self.index]
    