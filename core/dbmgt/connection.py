import config
import sqlite3


def getConnection():
    filePath = config.BASE_DIR + "/attendanceSystem/database/database.db"
    return sqlite3.connect(filePath)

