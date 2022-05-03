from abc import ABC, abstractmethod


class Exp(ABC):
    @abstractmethod
    def transicao(self, s):
        pass

    @abstractmethod
    def toString(self):
        pass


