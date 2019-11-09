from Language import Language
from User import User

class Validator:
    
    def isValidAnswer(self, yes, no):#if user input is valid
        answer = True 
        while True:
            self.userInput = User.FileOrTyping(self)
            if self.userInput == "1" or self.userInput == '2':
                return self.userInput
            else:
                print("You put an invalid number!\n")
                answer = True
            
    def isValidLanguage(self): #If user input is in json
        import json 
        f = open('Translation.json')
        json_dict = json.load(f)
        self.answer = True
        while self.answer == True:
            translationLanguage = Language.getLanguage(self)
            if translationLanguage in json_dict:
                return translationLanguage
            elif translationLanguage not in json_dict:
                print("You put an invalid language!\n")
                self.answer = True
                
    def isValidAnswerforWriting(self, y, t):#if user input is valid
        answer = True 
        while True:
            self.userInput = User.writeConfirmation(self)
            if self.userInput == "1" or self.userInput == '2':
                return self.userInput
            else:
                print("You put an invalid number!\n")
                answer = True
                
    def isValidChoice(self, yes, no):#if user input is valid
        answer = True 
        while True:
            self.userInput = User.userChoice(self)
            if self.userInput == "1" or self.userInput == '2':
                return self.userInput
            else:
                print("You put an invalid number!\n")
                answer = True
                
    def isValidNumber(self,u,i):#if user input is valid
        answer = True 
        while True:
            try:
                self.userInput = Language.getNumber(self)
                if self.userInput >= u and self.userInput <= i:
                    return self.userInput
                else:
                    print("You put an invalid input! Input should be 1 to 5:\n")
                    answer = True
            except ValueError:
                print("You put an invalid number!!\n ")
                True
                
    def isValidConfirmation(self, yes, no):#if user input is valid
        answer = True 
        while True:
            self.userInput = User.confirmation(self)
            if self.userInput == "1" or self.userInput == '2':
                return self.userInput
            else:
                print("You put an invalid number!\n")
                answer = True