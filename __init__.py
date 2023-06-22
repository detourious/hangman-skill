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
        self.lives_left = 6
        self.win_state = False
        self.guessed_letters = []
        self.speak_dialog('chosen_word', data={"length": len(self.chosen_word)})
        
        while self.lives_left > 0 and not self.win_state:
            response = self.get_response('guess_letter', num_retries=0)
            if response is not None:
                self.speak('you said ' + response)
                
                if self.voc_match(response, "valid_letters", None, True):
                    letter_guess = response[7:7]
                    self.speak("You guessed " + letter_guess)

                    if self.chosen_word.find(letter_guess) > -1:
                        self.speak("That is correct.")
                    else:
                        self.lives_left -= 1
                        self.speak("That is incorrect. You now have " + str(self.lives_left) + " lives left.")
                else:
                    self.speak("bad")

        if self.win_state:
            self.speak("You win!")
        else:
            self.speak("You lose!")

    def stop(self):
        self.lives_left = 0
        self.win_state = True

def create_skill():
    return Hangman()

