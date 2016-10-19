# libraries
from flask import Flask
from flask_restful import Api
from flask_mail import Mail, Message

from services.FingerPrintScanner import *
from uicontroller.Main import *
from uicontroller.addUser import *
from uicontroller.GetStudents import *
from uicontroller.UploadAttendance import *
from uicontroller.AddCourse import *
from uicontroller.CourseRegister import *

app = Flask(__name__)
api = Api(app)


api.add_resource(Main, '/')
api.add_resource(FingerPrintScanner, '/fingerPrint/<sign>')
api.add_resource(AddUser, '/home/addUser')
api.add_resource(GetStudents, '/home/getStudents')
api.add_resource(AddUserPage, '/adduserpage')
api.add_resource(GetUserInformation, '/getuserinformation')
api.add_resource(uploadAttendance, '/uploadattendance')
api.add_resource(UploadAttendanceAPI, '/home/uploadattendance')
api.add_resource(AddCourse, '/addcourse')
api.add_resource(CourseRegister, '/courseregister')