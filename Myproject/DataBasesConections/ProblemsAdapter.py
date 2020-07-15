import mysql.connector
from mysql.connector import Error
from DataBaseClasses.problmes import Problem
import datetime


class ProblemsAdapter:
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

    def insert(self, problem: Problem):
        if problem is None:
            print("Problem can't be None")
            return
        try:
            connection = self.__connect()
            cursor = connection.cursor()
            sql = 'INSERT INTO Problems (id, name, type, File_Path, TimeLimit, MemoryLimit , validation, contest_id) ' \
                  'Values (%s , %s , ' \
                   '%s , %s , %s , %s , %s , %s) '
            values = problem.tuple()
            cursor.execute(sql, values)
            connection.commit()
            cursor.close()
            connection.close()
        except Error as e:
            print("Error while insert  on Problems DataBase" , e)

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
            sql = 'UPDATE Problems SET ' + string + ' where id=%s'
            values = tuple(values)
            cursor.execute(sql, values)
            connection.commit()
            cursor.close()
            connection.close()
        except Error as e:
            print("Error while update on Problems DataBase" , e)

    def delete(self, id: str):
        if id is None:
            print("ID can't be None")
            return
        try:
            connection = self.__connect()
            cursor = connection.cursor()
            sql = "DELETE from Problems Where id=" + "'" + id + "'"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            connection.close()
        except Error as e:
            print("Error while delete from Problems DataBase" , e)

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
            sql = 'Select * from Problems Where ' + string
            cursor.execute(sql, values)
            records = cursor.fetchall()
            problems = []
            for row in records:
                problems.append(Problem(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
            cursor.close()
            connection.close()
            return problems
        except Error as e:
            print("Error while select from Problems DataBase" , e)

    def selectall(self):
        try:
            connection = self.__connect()
            cursor = connection.cursor()
            sql = 'Select * from Problems'
            cursor.execute(sql)
            records = cursor.fetchall()
            problems = []
            for row in records:
                problems.append(Problem(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
            cursor.close()
            connection.close()
            return problems
        except Error as e:
            print("Error while selectALl from Problems DataBase" , e)

problemAdapter = ProblemsAdapter()
problemAdapter.insert(Problem('asd', 'sada', 'asd', 'sad', 1, 2, 1, '1'))

problemAdapter.update({'name': 'ds',
                       'type': 'wait'}, 'asd')
val = problemAdapter.select({'id': 'asd'})
print(val)
problemAdapter.delete('asd')
