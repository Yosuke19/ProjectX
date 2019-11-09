from User import User
from Validator import Validator

class ReadandWrite:
    
    import sys
    def __init__(self,file,words):
        self.file = file
        self.words = words
        
    def readFile(self):
        while True:
            try:
                with open(User.fileName(self),'r') as userFile:
                    for self.words in userFile.readlines():
                        return self.words
            except FileNotFoundError:
                print("\nWrong file or file path/n")
                True
    
    def writeFile(self, translationResult, newFileName):
        with open(translationResult, 'w', encoding="utf-8") as newfile:
            words = print(newFileName, file=newfile)
            self.words = words
            return self.words