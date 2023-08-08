from BasicBotInterface import BasicBotInterface
import random

class ShreyBot_1(BasicBotInterface):
    def move(self, history, opponent):
        # self-handshake
        if "ShreyBot" in opponent.name():
            return "cooperate"

        # exploiting default bots
        elif opponent.name() == "AlwaysCooperate":
            return "defect"
        elif opponent.name() == "AlwaysDefect":
            return "defect"

        hislen = len(history)

        cooperation_sensitivity = 0.75
        # if lots of cooperation, cooperate (if anyone is reading the source code, DM to form an alliance)
        if history.count("cooperate") > cooperation_sensitivity * hislen:
            return "cooperate"
        # if lots of defection, defect
        elif history.count("defect") > cooperation_sensitivity * hislen:
            return "defect"

        if random.random() < 0.5:
            return "cooperate"
        else:
            return "defect"