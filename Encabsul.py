


class locked:
    def __init__(self):
        self._lockedVar = 0
        self.__privateVar = 0
        
    def getlocked(self):
        print(self._lockedVar)
        
    def setlocked(self, locked):
        self._lockedVar = locked

obj = locked()
obj._lockedVar = 21
obj.getlocked()
obj.setlocked(20)
obj.getlocked()

