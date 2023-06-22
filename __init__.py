from mycroft import MycroftSkill, intent_file_handler


class Hangman(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('hangman.intent')
    def handle_hangman(self, message):
        self.speak_dialog('hangman')


def create_skill():
    return Hangman()

