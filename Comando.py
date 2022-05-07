from abc import abstractmethod


class Comando:
    @abstractmethod
    def transicao(self, s):
        pass
