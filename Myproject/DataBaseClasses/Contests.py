import datetime


class Contest:
    def __init__(self, id: str, name: str, description: str, filePath: str, handle: str, contestTime: float, startDate: datetime):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__filePath = filePath
        self.__handle = handle
        self.__contestTime = contestTime
        self.__startDate = startDate

    def tuple(self):
        return self.id, self.name, self.description, self.handle, self.contestTime, self.startDate

    def __str__(self):
        return "Contest : " + self.id + ' ' + self.name + ' ' + self.description + ' ' + self.handle + ' ' + str(
            self.contestTime) + ' ' + str(self.startDate)

    def __repr__(self):
        return "Contest : " + self.id + ' ' + self.name + ' ' + self.description + ' ' + self.handle + ' ' + str(
            self.contestTime) + ' ' + str(self.startDate)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.___id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def handle(self):
        return self.__handle

    @handle.setter
    def handle(self, handle):
        self.__handle = handle

    @property
    def contestTime(self):
        return self.__contestTime

    @contestTime.setter
    def contestTime(self, contestTime):
        self.__contestTime = contestTime

    @property
    def startDate(self):
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate):
        self.__startDate = startDate

    @property
    def filePath(self):
        return self.__filePath

    @filePath.setter
    def filePath(self, filePath):
        self.__filePath = filePath