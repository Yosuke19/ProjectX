from ReadandWrite import ReadandWrite
from Translation import Translation
from LanguageFromCode import LanguageFromCode
from Validator import Validator
from Language import Language
from User import User
from Date import Date

class TranslationSub(User, ReadandWrite):
    from googletrans import Translator
    def __init__(self, data):
        self.data = data
    
    def askTranslator(self):
        useropt = Validator.isValidAnswer(self,'1', '2') 
        if useropt =='1':
            translator_obj = self.Translator()
            translated_phrase = translator_obj.translate(ReadandWrite.readFile(self), dest=LanguageFromCode.getLanguageCode (self))
            self.data = "\n%s \n\nOriginal Language was %s" %(translated_phrase.text,Translation.detectLanguage(self))
            return self.data
        elif useropt == '2':
            translator_obj = self.Translator()
            translated_phrase = translator_obj.translate(User.typing(self), dest=LanguageFromCode.getLanguageCode (self))
            self.data = "\n%s \n\nOriginal Language was %s" %(translated_phrase.text,Translation.detectLanguage(self))
            return self.data
            

class TranslationMain(TranslationSub,ReadandWrite, Date,LanguageFromCode):
    def __init__(self):
        TranslationSub.askTranslator(self)
        
if __name__ == "__main__":
    TranslationSub.askTranslator(self)
        