from DataBaseClasses.Submissions import Submission
import mysql.connector
from mysql.connector import Error
import datetime

class SubmissionsAdapter:
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

    def insert(self, submission: Submission):
        if submission is None:
            print("Submission None object")
            return
        try:
            connection = self.__connect()
            cursor = connection.cursor()
            sql = 'INSERT INTO Submissions (id, problem_id, handle , submissionDate, sorcecode_Path , TimeExcution , memoryExcution, Contest_Id, inContest , isHidden) Values (%s , %s , ' \
              '%s , %s , %s , %s , %s, %s , %s , %s, %s) '
            values = submission.tuple()
            cursor.execute(sql, values)
            connection.commit()
            cursor.close()
            connection.close()
        except Error as e:
            print("Error while insert Submission on DataBase", e)

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
            sql = 'UPDATE Submissions SET ' + string + ' where handle=%s'
            values = tuple(values)
            cursor.execute(sql, values)
            connection.commit()
            cursor.close()
            connection.close()
        except Error as e:
            print("Error while update Submission On Database", e)

    def delete(self, handle: str):
        if handle is None:
            print("handle is None")
            return
        try:
            connection = self.__connect
            cursor = connection.cursor()
            sql = "DELETE from Submissions Where handle=" + "'" + handle + "'"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            connection.close()
        except Error as e:
            print("Error While Delete from Submission DataBase", e)


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
            sql = 'Select * from Submissions Where ' + string
            cursor.execute(sql, values)
            records = cursor.fetchall()
            Submissions = []
            for row in records:
                Submissions.append(Submission(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
            cursor.close()
            connection.close()
            return Submissions
        except Error as e:
            print("Error While select from Submission DataBase", e)

    def selectall(self):
        try:
            connection = self.__connect()
            cursor = connection.cursor()
            sql = 'Select * from Submissions'
            cursor.execute(sql)
            records = cursor.fetchall()
            Submissions = []
            for row in records:
                Submissions.append(Submissions(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
            cursor.close()
            connection.close()
            return Submissions
        except Error as e:
            print("Error While select ALL from Submission DataBase", e)

