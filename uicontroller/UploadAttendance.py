from werkzeug.utils import secure_filename
from flask_mail import Message
import config
from __init__ import *

class UploadAttendanceAPI(Resource):
    def post(self):
        file = request.files['AttendanceFile']
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save("uploadAttendance")
        readFile("uploadAttendance")
        sendMail(config.mail)
        return "Email was sent"


def readFile(fileName):
    with open(fileName) as f:
        for line in f:
            print line

def sendMail(mail):
    msg = Message('Hello', sender='attendance.sys.999@gmail.com', recipients=['tharinda221@gmail.com'])
    msg.body = "This is generated message"
    mail.send(msg)