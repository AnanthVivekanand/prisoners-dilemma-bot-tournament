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

        # tit for tat strat
        if len(history) > 0:
            if history[hislen - 1][0] == "defect":
                return "defect"
            else:
                return "cooperate"
        else:
            return "cooperate"