from BasicBotInterface import BasicBotInterface

class SimulationBot(BasicBotInterface):
    def move(self, history, opponent):
        if (opponent.move(history, self) == "cooperate"):
            # simulate opponent's next move
            return "defect"
        else:
            return "defect"