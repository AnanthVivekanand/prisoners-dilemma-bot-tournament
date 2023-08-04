from abc import ABC, abstractmethod

class BasicBotInterface(ABC): 
    @abstractmethod
    def move(self, history: list[tuple[str, str]], opponent: 'BasicBotInterface') -> str:
        pass

    def name(self):
        return self.__class__.__name__