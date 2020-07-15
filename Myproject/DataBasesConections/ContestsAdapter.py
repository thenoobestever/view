import mysql.connector
from mysql.connector import Error
from DataBaseClasses.Contests import Contest
import datetime


class ContestAdapter:
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

    def insert(self, contest: Contest):
        if contest is None:
            print("Contest can't be None")
            return
        try:
            connection = self.__connect()
            cursor = connection.cursor()
            sql = 'INSERT INTO Contests (id, name, description, filePath, handle, contestTime , startDate) ' \
                  'Values (%s , %s , %s , %s , %s , %s , %s) '
            values = contest.tuple()
            cursor.execute(sql, values)
            connection.commit()
            cursor.close()
            connection.close()
        except Error as e:
            print("Error while insert  on Contests DataBase" , e)

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
            connection = self.__connect()
            cursor = connection.cursor()
            sql = 'UPDATE Contests SET ' + string + ' where id=%s'
            values = tuple(values)
            cursor.execute(sql, values)
            connection.commit()
            cursor.close()
            connection.close()
        except Error as e:
            print("Error while update on Contests DataBase" , e)

    def delete(self, id: str):
        if id is None:
            print("ID can't be None")
            return
        try:
            connection = self.__connect()
            cursor = connection.cursor()
            sql = "DELETE from Contests Where id=" + "'" + id + "'"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            connection.close()
        except Error as e:
            print("Error while delete from Contests DataBase" , e)

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
            sql = 'Select * from Contests Where ' + string
            cursor.execute(sql, values)
            records = cursor.fetchall()
            contests = []
            for row in records:
                contests.append(Contest(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            cursor.close()
            connection.close()
            return contests
        except Error as e:
            print("Error while select from Contests DataBase" , e)

    def selectall(self):
        try:
            connection = self.__connect()
            cursor = connection.cursor()
            sql = 'Select * from Contests'
            cursor.execute(sql)
            records = cursor.fetchall()
            contests = []
            for row in records:
                contests.append(Contest(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            cursor.close()
            connection.close()
            return contests
        except Error as e:
            print("Error while selectALl from contests DataBase" , e)

## Didn't Test Yet!!!
