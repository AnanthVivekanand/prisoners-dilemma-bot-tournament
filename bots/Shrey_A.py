from BasicBotInterface import BasicBotInterface
import random

class ShreyBot_A(BasicBotInterface):
    def move(self, history, opponent):
        # self-handshake
        if opponent.name() == "ShreyBot":
            return "cooperate"

        # exploiting default bots
        elif opponent.name() == "AlwaysCooperate":
            return "defect"
        elif opponent.name() == "AlwaysDefect":
            return "defect"

        if random.random() < 0.5:
            return "cooperate"
        else:
            return "defect"