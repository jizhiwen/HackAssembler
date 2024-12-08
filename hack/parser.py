import enum

class InstructionType(enum.Enum):
    A_INSTRUCTION = 0
    C_INSTRUCTION = 1
    L_INSTRUCTION = 2

class Parser:
    def __init__(self, file):
        self._file = file
        self._is = open(file, "r")
        self._current = None
        self._pre_fetch = None

    def hasMoreLines(self):
        if self._pre_fetch and len(self._pre_fetch):
            return True
        self._pre_fetch = self._is.readline()
        while self._pre_fetch:
            self._pre_fetch = self._pre_fetch.strip()
            if len(self._pre_fetch) and not self._pre_fetch.startswith("//"):
                return True
            self._pre_fetch = self._is.readline()
        else:
            return False

    def advance(self):
        self._current = self._pre_fetch
        self._pre_fetch = None

    def instructionType(self):
        if self._current.startswith('@'):
            return InstructionType.A_INSTRUCTION
        elif self._current.startswith('('):
            return InstructionType.L_INSTRUCTION
        else:
            return InstructionType.C_INSTRUCTION

    def symbol(self):
        if self.instructionType() == InstructionType.A_INSTRUCTION:
            return self._current[1:]
        elif self.instructionType() == InstructionType.L_INSTRUCTION:
            return self._current[1:-1]
        else:
            return ""

    def dest(self):
        if self.instructionType() != InstructionType.C_INSTRUCTION:
            return ""
        index = self._current.find('=')
        if index == -1:
            return ""
        return self._current[:index]

    def comp(self):
        if self.instructionType() != InstructionType.C_INSTRUCTION:
            return ""
        index_l = self._current.find('=')
        index_r = self._current.find(';')
        if index_r == -1:
            index_r = len(self._current)
        return self._current[index_l+1:index_r]

    def jump(self):
        if self.instructionType() != InstructionType.C_INSTRUCTION:
            return ""
        index = self._current.find(';')
        if index == -1:
            return ""
        return self._current[index+1:]