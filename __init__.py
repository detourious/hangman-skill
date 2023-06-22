from mycroft import MycroftSkill, intent_file_handler
from random import randint

class Hangman(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.random_words = ["apple", "banana", "cherry"]

    @intent_file_handler('hangman.intent')
    def handle_hangman(self, message):
        # pick a random word
        self.chosen_word = self.random_words[randint(0, len(self.random_words)-1)]
        self.speak_dialog('chosen_word', data={"length": len(self.chosen_word)})
        response = self.get_response('guess_letter')
        if not response is None:
            if response[0:5] == "letter":
                self.speak(f'valid letter {response[7:7]}')
            else:
                self.speak('invalid letter')
        else:
            self.speak('i dont know lol')

def create_skill():
    return Hangman()

