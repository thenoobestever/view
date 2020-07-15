import mysql.connector
from mysql.connector import Error
from DataBaseClasses.Users import User
import datetime


class UsersAdapter:
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

    def insert(self, user: User):
        if user is None:
            print("User None object")
            return
        try:
            connection = self.__connect()
            cursor = connection.cursor()
            sql = 'INSERT INTO Users (name, handle , email , brithdate , password, isAdmin , Picture) Values (%s , %s , ' \
              '%s , %s , %s , %s , %s) '
            values = user.tuple()
            cursor.execute(sql, values)
            connection.commit()
            cursor.close()
            connection.close()
        except Error as e:
            print("Error while insert User on DataBase" , e)

    def update(self, fields: dict, primaryKey):
        if fields is None:
            print("Fileds Can't be None")
            return
        if primaryKey is None:
            print("Primary Key is None")
            return
        try:
            string = ''
            values = []
            for field, value in fields.items():
                string = string + str(field) + '= %s,'
                values.append(value)
            string = string[:-1]
            values.append(primaryKey)

            connection = self.__connect
            cursor = connection.cursor()
            sql = 'UPDATE Users SET ' + string + ' where handle=%s'
            values = tuple(values)
            cursor.execute(sql, values)
            connection.commit()
            cursor.close()
            connection.close()
        except Error as e:
            print("Error while update User On Database", e)

    def delete(self, handle: str):
        if handle is None:
            print("handle is None")
            return
        try:
            connection = self.__connect
            cursor = connection.cursor()
            sql = "DELETE from Users Where handle=" + "'" + handle + "'"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            connection.close()
        except Error as e:
            print("Error While Delete from User DataBase", e)


    def select(self, fileds: dict):
        if fileds is None:
            print("Fileds can't be None")
        try:
            string = []
            values = []
            for filed, value in fileds.items():
                string.append(filed + '= %s')
                values.append(value)
            string = 'and'.join(string)
            connection = self.__connect
            cursor = connection.cursor()
            values = tuple(values)
            sql = 'Select * from Users Where ' + string
            cursor.execute(sql, values)
            records = cursor.fetchall()
            users = []
            for row in records:
                users.append(User(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            cursor.close()
            connection.close()
            return users
        except Error as e:
            print("Error While select from User DataBase", e)

    def selectall(self):
        try:
            connection = self.__connect()
            cursor = connection.cursor()
            sql = 'Select * from Users'
            cursor.execute(sql)
            records = cursor.fetchall()
            users = []
            for row in records:
                users.append(User(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            cursor.close()
            connection.close()
            return users
        except Error as e:
            print("Error While select ALL from User DataBase", e)


UsersAdapter().insert(User('a', 'thenoobestever', 't', datetime.datetime(1997, 9, 27), 'asdas', True, 'ads'))

#UsersAdapter().update({'email': 'shit.com', 'name': 'ALI'}, 'thenoobestever')

#val = UsersAdapter().select({'handle': 'thenoobestever'})
#print(val)

#UsersAdapter().delete('thenoobestever')
