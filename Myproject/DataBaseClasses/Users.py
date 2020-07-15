import datetime


class User:
    def __init__(self, name: str, handle: str, email: str, birthDate: datetime, password: str, isAdmin: bool,
                 picture: str):
        self.__name = name
        self.__handle = handle
        self.__email = email
        self.__birthDate = birthDate
        self.__password = password
        self.__isAdmin = isAdmin
        self.__picture = picture

    def tuple(self):
        return self.name, self.handle, self.email, self.birthDate, self.password, self.isAdmin, self.picture

    def __repr__(self):
        return 'User: ' + self.name + ' ' + self.handle + ' ' + self.email + ' ' + str(self.birthDate) + ' ' + self.password + ' ' + str(self.isAdmin) + ' ' + self.picture

    def __str__(self):
        return 'User: ' + self.name + ' ' + self.handle + ' ' + self.email + ' ' + str(self.birthDate) + ' ' + self.password + ' ' + str(self.isAdmin) + ' ' + self.picture

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def handle(self):
        return self.__handle

    @handle.setter
    def handle(self, handle: str):
        self.__handle = handle

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def birthDate(self):
        return self.__birthDate

    @birthDate.setter
    def birthDate(self, birthDate: datetime):
        self.__birthDate = birthDate

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def isAdmin(self):
        return self.__isAdmin

    @isAdmin.setter
    def isAdmin(self, isAdmin: bool):
        self.__isAdmin = isAdmin

    @property
    def picture(self):
        return self.__picture

    @picture.setter
    def picture(self, picture):
        self.__picture = picture


