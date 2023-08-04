from BasicBotInterface import BasicBotInterface

class AlwaysCooperate(BasicBotInterface):
    def move(self, history, opponent):
        return "cooperate"