class Estado:
    def __init__(self):
        self.mapeamento = {}

    def adicionar(self, variavel, valor):
        self.mapeamento[variavel] = valor

    def atualizar(self, variavel, valor):
        self.mapeamento[variavel] = valor

    def ler(self, variavel):
        inteiro = self.mapeamento[variavel]
        if inteiro is None:
            return 0
        else:
            return inteiro

    def toString(self):
        s = '['
        for aux, x in enumerate(self.mapeamento):
            s = s + x + ' -> ' + str(self.mapeamento[x])
            if aux < len(self.mapeamento)-1:
                s += ', '

        s += ']'
        return s
