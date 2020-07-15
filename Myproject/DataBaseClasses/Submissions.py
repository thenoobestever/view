import datetime


class Submission:
    def __init__(self, id: str, problemId: str, language: str, handle: str, submissionDate: datetime, sourceCodePath: str, timeExcution: int,
                 memoryExcution: int, contestId: str, inContest: bool, isHidden: bool):
        self.__id = id
        self.__problemId = problemId
        self.__language = language
        self.__handle = handle
        self.__submissionDate = submissionDate
        self.__sourceCodePath = sourceCodePath
        self.__timeExcution = timeExcution
        self.__memoryExcution = memoryExcution
        self.__contestId = contestId
        self.__inContest = inContest
        self.__isHidden = isHidden

    def tuple(self):
        return self.id, self.problemId, self.language, self.handle, self.sourceCodePath, self.timeExcution, self.memoryExcution, self.contestId, self.inContest, self.isHiddenn

    def __repr__(self):
        return "Submission : " + self.id + ' ' + self.problemId + ' ' + self.language + ' ' + self.handle + ' ' + self.sourceCodePath + ' ' + str(self.timeExcution) + ' ' + str(self.memoryExcution) + \
               ' ' + self.contestId + ' ' + str(self.inContest) + ' ' + str(self.isHiddenn)

    def __str__(self):
        return "Submission : " + self.id + ' ' + self.problemId + ' ' + self.language + ' ' + self.handle + ' ' + self.sourceCodePath + ' ' + str(self.timeExcution) + ' ' + str(self.memoryExcution) + \
               ' ' + self.contestId + ' ' + str(self.inContest) + ' ' + str(self.isHiddenn)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def problemId(self):
        return self.__problemId

    @problemId.setter
    def problemId(self, problemId: str):
        self.__problemId = problemId

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def handle(self):
        return self.__handle

    @handle.setter
    def handle(self, handle: str):
        self.__handle = handle

    @property
    def submissionDate(self):
        return self.__submissionDate

    @submissionDate.setter
    def submissionDate(self, submissionDate):
        self.__submissionDate = submissionDate

    @property
    def sourceCodePath(self):
        return self.__sourceCodePath

    @sourceCodePath.setter
    def sourceCodePath(self, sourceCodePath: str):
        self.__sourceCodePath = sourceCodePath

    @property
    def timeExcution(self):
        return self.__timeExcution

    @timeExcution.setter
    def timeExcution(self, timeExcution: int):
        self.__timeExcution = timeExcution

    @property
    def memoryExcution(self):
        return self.__memoryExcution

    @memoryExcution.setter
    def memoryExcution(self, memoryExcution: int):
        self.__memoryExcution = memoryExcution

    @property
    def contestId(self):
        return self.__contestId

    @contestId.setter
    def contestId(self, contestId: str):
        self.__contestId = contestId

    @property
    def inContest(self):
        return self.__inContest

    @inContest.setter
    def inContest(self, inContest: bool):
        self.__inContest = inContest

    @property
    def isHidden(self):
        return self.__isHidden

    @isHidden.setter
    def isHiddenn(self, isHidden: bool):
        self.__isHidden = isHidden
