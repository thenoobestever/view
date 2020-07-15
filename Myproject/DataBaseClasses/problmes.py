class Problem:
    def __init__(self, id: str, name: str, type: str, filePath: str, timeLimit: int, memoryLimit: int, validation: bool,
                 contestId: str):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__filePath = filePath
        self.__timeLimit = timeLimit
        self.__memoryLimit = memoryLimit
        self.__validation = validation
        self.__contestId = contestId

    def tuple(self):
        return self.id, self.name, self.type, self.filePath, self.timeLimit, self.memoryLimit, self.validation, self.contestId

    def __repr__(self):
        return 'Problem : ' + self.id + ' ' + self.name + ' ' + self.type + ' ' + self.filePath + ' ' + str(self.timeLimit) + ' ' + str(self.memoryLimit) + ' ' + str(self.validation) + ' ' + self.contestId

    def __str__(self):
        return 'Problem : ' + self.id + ' ' + self.name + ' ' + self.type + ' ' + self.filePath + ' ' + str(self.timeLimit) + ' ' + str(self.memoryLimit) + ' ' + str(self.validation) + ' ' + self.contestId

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def filePath(self):
        return self.__filePath

    @filePath.setter
    def filePath(self, filePath):
        self.__filePath = filePath

    @property
    def timeLimit(self):
        return self.__timeLimit

    @timeLimit.setter
    def timeLimit(self, timeLimit):
        self.__timeLimit = timeLimit

    @property
    def memoryLimit(self):
        return self.__memoryLimit

    @memoryLimit.setter
    def memoryLimit(self, memoryLimit):
        self.__memoryLimit = memoryLimit

    @property
    def validation(self):
        return self.__validation

    @validation.setter
    def validation(self, validation):
        self.__validation = validation

    @property
    def contestId(self):
        return self.__contestId

    @contestId.setter
    def contestId(self, contestId):
        self.__contestId = contestId