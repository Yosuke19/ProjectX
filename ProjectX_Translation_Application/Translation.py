from Language import Language
from abc import ABC ,abstractmethod
from User import User
from ReadandWrite import ReadandWrite

class Translation(ABC, ReadandWrite, User):
    from googletrans import Translator
    
    def __init__(self,detectLang):
        self.detectLang = detectLang
    
    @abstractmethod
    def askTranslator(self):
        pass
        
    def detectLanguage(self):
        import json 
        
        f = open('Translation.json')
        json_dict = json.load(f)
        translator = self.Translator()
        detect_result = translator.detect(self.words)
        self.detectLang = detect_result.lang
        keys = [k for k, v in json_dict.items() if v == self.detectLang]
        self.detectLang = ", ".join(keys).upper()
        return  self.detectLang