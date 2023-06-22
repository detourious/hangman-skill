from mycroft import MycroftSkill, intent_file_handler
from random import randint

class Hangman(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.random_words = ["apple", "banana", "cherry"]

    @intent_file_handler('hangman.intent')
    def handle_hangman(self, message):
        # pick a random word
        self.chosen_word = self.random_words[randint(0, len(self.random_words))]
        self.speak_dialog('choosen_word', data={"length": len(self.chosen_word)})

def create_skill():
    return Hangman()

