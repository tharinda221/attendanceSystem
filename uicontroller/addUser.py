from __init__ import *


class AddUser(Resource):
    def get(self):
        conn = getConnection()
        cursor = conn.execute('SELECT * FROM students').fetchall()
        print cursor
        for item in cursor:
            print item
        print "Data fetched Successfully"
        conn.close()

    def post(self):
        row = (
            request.form["StudentID"], request.form["IDtype"], request.form["Name"], request.form["Faculty"],
            request.form["CardID"],
            request.form["FingerID"])
        print row
        conn = getConnection()
        # conn.execute(
        #     'CREATE TABLE students (StudentID TEXT, IDtype TEXT, Name TEXT, Faculty TEXT, CardID TEXT, FingerID TEXT)')

        conn.execute('insert into students values (?,?,?,?,?,?)', row)
        conn.commit()
        print "Table created successfully"
        conn.close()
        return "User data stored"
