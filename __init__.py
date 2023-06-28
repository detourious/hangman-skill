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

        # initialize game variables
        self.lives_left = 6
        self.win_state = False
        self.guessed_letters = []

        # start the game by telling the user the length of the word
        self.speak_dialog('chosen_word', data={"length": len(self.chosen_word)})
        
        # start the game loop
        while self.lives_left > 0 and not self.win_state:
            # check if the user has won

            # assume they won...
            has_won = True

            for i in range(len(self.chosen_word)):
                if not self.chosen_word[i] in self.guessed_letters:
                    # until we find a letter that hasn't been guessed
                    # in that case, we know they haven't won yet
                    has_won = False 

            # if they have won, break out of the loop
            if has_won:
                self.win_state = True
                self.stop()
                break

            # otherwise, ask them to guess a letter
            response = self.get_response('guess_letter', num_retries=0)

            # check if they responded
            if response is not None:
                # check if they guessed a letter and parse it to "letter <a/b/d/e/...>" format
                if self.voc_match(response, "valid_letters", None, True):
                    # parse the letter from the response
                    letter_guess = response[7:8]

                    # check if the letter has already been guessed
                    if not letter_guess in self.guessed_letters:
                        # check if the letter is in the word
                        if self.chosen_word.find(letter_guess) > -1:
                            # if it is, tell them they're correct and add it to the list of guessed letters
                            self.speak("That is correct.")
                            self.guessed_letters.append(letter_guess)
                        else:
                            # if it isn't, tell them they're incorrect and subtract a life
                            self.lives_left -= 1
                            self.speak("That is incorrect. You now have " + str(self.lives_left) + " lives left.")
                            self.guessed_letters.append(letter_guess)
                    else:
                        # if they already guessed that letter, tell them
                        self.speak("You already guessed that letter.")
                else:
                    # if they didn't guess a letter, tell them
                    self.speak("That is not a valid letter.")

        # check if they won or lost
        if self.win_state:
            self.speak("You win!")
        else:
            self.speak("You lose!")

    # stop the game
    def stop(self):
        self.lives_left = 0
        self.win_state = True

def create_skill():
    return Hangman()

