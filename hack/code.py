class Code:
    def __init__(self):
        self._comp_table = {
            "0": "0101010",
            "1": "0111111",
            "-1": "0111010",
            "D": "0001100"
        }

        self._dest_table = {
            "null": "000", "M": "001", "D": "010", "DM": "011",
            "A": "100", "AM": "101", "AD": "110", "ADM": "111"
        }

        self._jump_table = {
            "null": "000", "JGT": "001", "JEQ": "010", "JGE": "011",
            "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"
        }


    def dest(self, symbol):
        if symbol not in self._dest_table:
            return ""
        return self._dest_table[symbol]

    def comp(self, symbol):
        if symbol not in self._comp_table:
            return ""
        return self._comp_table[symbol]

    def jump(self, symbol):
        if symbol not in self._jump_table:
            return ""
        return self._jump_table[symbol]