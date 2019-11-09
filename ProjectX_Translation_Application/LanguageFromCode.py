from Validator import Validator
class LanguageFromCode:
    
    def __init__(self,languageCode):
        self.languageCode = languageCode
        
    def getLanguageCode(self):
        LanguageCode = Validator.isValidLanguage(self)
        self.languageCode = LanguageCode
        return self.languageCode