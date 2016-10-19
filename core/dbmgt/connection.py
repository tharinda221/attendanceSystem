import config
import sqlite3


def getConnection():
    filePath = config.BASE_DIR + "/attendanceSystem/database/database.db"
    return sqlite3.connect(filePath)

# conn = getConnection()
# conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
# print "Table created successfully"
# conn.close()

# conn.execute(
#     'CREATE TABLE students (StudentID TEXT, IDtype TEXT, Name TEXT, Faculty TEXT, Subject1 TEXT, Subject2 TEXT, Subject3 TEXT, Subject4 TEXT, CardID TEXT, FingerID TEXT)')
# print "Table created successfully"

