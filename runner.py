from bots.AlwaysCooperate import AlwaysCooperate
from bots.AlwaysDefect import AlwaysDefect
from bots.ShreyBot_1 import ShreyBot_1
from bots.AnanthBot_1 import AnanthBot_1


import pandas as pd

from bots.SimulationBot import SimulationBot
 
def simulate(playing_bot, opposing_bot):
    if (playing_bot == None and opposing_bot == None):
        return None
    if (playing_bot == None):
        return opposing_bot.name()
    if (opposing_bot == None):
        return playing_bot.name()
    
    score = 0
    history = []
    for _ in range(30):
        playing_bot_move = None
        
        try:
            playing_bot_move = playing_bot.move(history, opposing_bot)
        except Exception as e:
            score += -4
            print(e)
            continue
            
        try:
            opposing_bot_move = opposing_bot.move(history, playing_bot)
        except Exception as e:
            print(e)
            score += 5
            continue
                     
        history.append((playing_bot_move, opposing_bot_move))
        score += get_score(playing_bot_move, opposing_bot_move)
            
    return score 
            
def get_score(move1, move2):
    if (move1 == "cooperate" and move2 == "cooperate"):
        return 3
    elif (move1 == "cooperate" and move2 == "defect"):
        return 0
    elif (move1 == "defect" and move2 == "cooperate"):
        return 5
    elif (move1 == "defect" and move2 == "defect"):
        return 1
    else:
        raise Exception("Invalid move")
    

bots = [None, AlwaysCooperate(), AlwaysCooperate(), AlwaysDefect(), AlwaysDefect(), ShreyBot_1(), AnanthBot_1()]

scores = [[simulate(bot1, bot2) for bot2 in bots] for bot1 in bots]

pd.set_option('display.max_colwidth', None)
print(pd.DataFrame(scores))
pd.DataFrame(scores).to_csv("scores.csv", index=False, header=False)