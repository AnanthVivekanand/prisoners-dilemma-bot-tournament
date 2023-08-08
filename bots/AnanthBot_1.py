from BasicBotInterface import BasicBotInterface
import random

class AnanthBot_1(BasicBotInterface):
    def move(self, history, opponent):
        if (opponent.name() == "AnanthBot_1"):
            return "cooperate"
        
        if (opponent.move(history, self) == "cooperate"):
            test_history = history.copy()
            test_history.append(("defect", "cooperate"))
            if (opponent.move(test_history, self) == "defect"):
                return "cooperate"
            else:
                return "defect"
        else:
            return "defect"
    