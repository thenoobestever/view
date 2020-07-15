class Friend:
    def __init__(self, firstHandle: str, secondHandle: str):
        self.__firstHandle = firstHandle
        self.__secondHandle = secondHandle

    def tuple(self):
        return self.firstHandle, self.secondHandle

    def __repr__(self):
        return "Friends : " + self.firstHandle + ' ' + self.secondHandle

    def __str__(self):
        return "Friends : " + self.firstHandle + ' ' + self.secondHandle

    @property
    def firstHandle(self):
        return self.__firstHandle

    @firstHandle.setter
    def firstHandle(self, firstHandle: str):
        self.__firstHandle = firstHandle

    @property
    def secondHandle(self):
        return self.__secondHandle

    @secondHandle.setter
    def secondHandle(self, secondHandle: str):
        self.__secondHandle = secondHandle