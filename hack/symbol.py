class Symbol:
    def __init__(self):
        self._table = {}

    def addEntry(self, symbol, address):
        self._table[symbol] = address

    def contains(self, symbol):
        return symbol in self._table

    def getAddress(self, symbol):
        if not self._contains(symbol):
            return -1
        return self._table[symbol]