import mysql.connector
from mysql.connector import Error
from DataBaseClasses.Friends import Friend


class FriendsAdapter:
    def __connect(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="alzawawi",
                password='alzawawi',
                database='work'
            )
        except Error as e:
            print("Error While Connecting to MySQL ", e)
        return connection

    def insert(self, friend: Friend):
        if friend is None:
            print("Friend can't be None")
            return
        try:
            connection = self.__connect()
            cursor = connection.cursor()
            sql = 'INSERT INTO friend (handle1, handle2) ' \
                  'Values (%s , %s)'
            values = friend.tuple()
            cursor.execute(sql, values)
            connection.commit()
            cursor.close()
            connection.close()
        except Error as e:
            print("Error while insert  on Friends DataBase", e)

    def update(self,  fields: dict, handle1: str, handle2: str):
        if handle1 is None:
            print("handle1 Can't be None")
            return
        if handle2 is None:
            print("handle2 Can't is None")
            return
        try:
            string = ''
            values = []
            for field, value in fields.items():
                string = string + str(field) + '= %s,'
                values.append(value)
            string = string[:-1]
            values.append(handle1)
            values.append(handle2)
            connection = self.__connect()
            cursor = connection.cursor()
            sql = 'UPDATE Friends SET ' + string + ' where handle1=%s and handle2=%s'
            values = tuple(values)
            cursor.execute(sql, values)
            connection.commit()
            cursor.close()
            connection.close()
        except Error as e:
            print("Error while update on Friends DataBase" , e)

    def delete(self, handle1: str, handle2: str):
        if id is None:
            print("ID can't be None")
            return
        try:
            connection = self.__connect()
            cursor = connection.cursor()
            sql = "DELETE from Friends Where handle1=" + "'" + handle1 + "' and handle2=" + "'" + handle2 + "'"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            connection.close()
        except Error as e:
            print("Error while delete from Friends DataBase" , e)

    def select(self, fileds: dict):
        if fileds is None:
            print("fileds Can't be None")
            return
        try:
            string = []
            values = []
            for filed, value in fileds.items():
                string.append(filed + '= %s')
                values.append(value)
            string = 'and'.join(string)
            connection = self.__connect()
            cursor = connection.cursor()
            values = tuple(values)
            sql = 'Select * from Friends Where ' + string
            cursor.execute(sql, values)
            records = cursor.fetchall()
            friends = []
            for row in records:
                friends.append(Friend(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
            cursor.close()
            connection.close()
            return Friend
        except Error as e:
            print("Error while select from Problems DataBase" , e)

    def selectall(self):
        try:
            connection = self.__connect()
            cursor = connection.cursor()
            sql = 'Select * from Friends'
            cursor.execute(sql)
            records = cursor.fetchall()
            friends = []
            for row in records:
                friends.append(Friend(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
            cursor.close()
            connection.close()
            return friends
        except Error as e:
            print("Error while selectALl from Friends DataBase" , e)

