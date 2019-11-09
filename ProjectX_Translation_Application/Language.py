class Language:
    
    def __init__(self,getTranslationLanguage,languageNumber):
        self.getTranslationLanguage = getTranslationLanguage
        self.languageNumber = languageNumber
        
    def getLanguage(self):
        getTranslationLanguage = input("Please enter the language you want to translate:\n").lower()
        self.getTranslationLanguage = getTranslationLanguage
        return self.getTranslationLanguage
    
    def getNumber(self):
        languageNumber = input("How many languages would you like to translate?\n")
        self.languageNumber = int(languageNumber)
        return self.languageNumber
