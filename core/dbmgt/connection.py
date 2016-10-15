import config
import sqlite3


def getConnection():
    filePath = config.BASE_DIR + "/attendanceSystem/database/database.db"
    return sqlite3.connect(filePath)

# conn = getConnection()
# conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
# print "Table created successfully"
# conn.close()