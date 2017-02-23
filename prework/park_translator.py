english_to_korean = {"cat":"go-yang-ee","dog":"gae", "water":"mul",
                     "fire":"bul", "earth":"ddang","tree":"na-mu",
                     "wind":"baram","metal":"gum-sok",
                     "time":"shigan", "location":"jang-so"}

eWord = raw_input("Please enter an English word: ")

def translate_etok(eWord):
    if eWord in english_to_korean:
        print english_to_korean[eWord]
    else:
        print 'Oh no! That word doesn\'t exist in this dictionary!'

translate_etok(eWord)
