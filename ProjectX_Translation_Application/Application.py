from Validator import Validator
from Language import Language
from TranslationSub import TranslationMain

class Application():
    val = Validator()
    
    print("Welcome to the Translation App!!\n")
    while True:
        store = []
        answer = val.isValidNumber(1, 5)
        for i in range(answer):
            t = TranslationMain()
            store.append(("\nIn %s" %t.languageCode.upper()))
            store.append(t.data)
        store = "\n\n".join(store)
        storage = []
        storage.append(store)
        storage.append("%s" %t.date())
        storage = "\n".join(storage)
        print("__________________________________________")
        print(storage)
        print("__________________________________________")
        confirmation = val.isValidConfirmation('1' , '2')
        if confirmation == '1':
            answer = val.isValidAnswerforWriting("1","2")
            if answer == '1':
                newName = input("\nPlease enter file name\n")
                t.writeFile(newName,storage)
                answer =val.isValidChoice("1","2")
                if answer == '1':
                    True
                elif answer == '2':
                    break
            elif answer == "2":
                answer = val.isValidChoice("1","2")
                if answer == '1':
                    True
                elif answer == '2':
                    break
        elif confirmation == "2":
            print("\nSorry for that.")
            answer = val.isValidChoice("1","2")
            if answer == '1':
                True
            elif answer == '2':
                break
        
    print("Thank you for using this app!! Have a good day!!")
    
        

