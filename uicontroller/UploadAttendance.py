from werkzeug.utils import secure_filename
from flask_mail import Message
import config
from __init__ import *

class UploadAttendanceAPI(Resource):
    def post(self):
        email = request.form['EmailAddress']
        file = request.files['AttendanceFile']
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save("uploadAttendance")
        msg = readFile("uploadAttendance")
        # sendMail(config.mail, email, msg)
        f = open('myfile.pdf', 'w')
        f.write(msg)  # python will convert \n to os.linesep
        f.close()  # you can omit in most cases as the destructor will call it
        return "Email was sent"


def readFile(fileName):
    d = set()
    with open(fileName) as f:
        for line in f:
            d.add(line.split(" ")[0])
        str = "Hi, Attended student list is given below" + "\n"
        for item in d:
            conn = getConnection()
            query = 'SELECT * from students WHERE StudentID =' + "'" + item + "'"
            student = conn.execute(query).fetchall()
            print student
            str = str + student[0][0] + " " + student[0][2] + "\n"
        return str

def sendMail(mail, email, userMessage):
    msg = Message('Attendance System Report', sender='tharinda2221@gmail.com', recipients=[email])
    msg.body = userMessage
    mail.send(msg)