class User:
    
    def __init__(self,words, file,answer,userAnswer,writeConfirmation,confirmation):
        self.words = words
        self.file = file
        self.answer = answer
        self.userAnswer = userAnswer
        self.writeConfirmation = writeConfirmation
        self.confirmation = confirmation

    def FileOrTyping(self):
        userAnswer = input("\nWould you like to use file or typed input?\n1. File\n2. Typing\n")
        self.userAnswer = userAnswer
        return self.userAnswer
        
    def userChoice(self):
        answer = input("\nWould you like to continue?:\n1. Yes\n2. No\n")
        self.answer = answer
        return self.answer
    
    def fileName(self):
        file = input("\nPlease enter the file to translate:\n")
        self.file = file
        return self.file
        
    def typing(self):
        words = input("\nPlease enter words here:\n")
        self.words = words
        return self.words
        
    def writeConfirmation(self):
        wConfirmation = input("\nWould you like to save this translation?\n1. Yes\n2. No\n")
        self.writeConfirmation = wConfirmation
        return self.writeConfirmation

    def confirmation(self):
        confirmation = input("\nIs translation correct?\n1. Correct\n2. Incorrect\n")
        self.confirmation = confirmation
        return self.confirmation
