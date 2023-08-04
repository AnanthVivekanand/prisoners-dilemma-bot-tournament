from BasicBotInterface import BasicBotInterface

class AlwaysDefect(BasicBotInterface):
    def move(self, history, opponent):
        return "defect"