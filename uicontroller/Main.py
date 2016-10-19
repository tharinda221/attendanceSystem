from __init__ import *


class Main(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(
            render_template('index.html'),
            200, headers)


class AddUserPage(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(
            render_template('addUser.html'),
            200, headers)

class GetUserInformation(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(
            render_template('GetUsers.html'),
            200, headers)

class uploadAttendance(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(
            render_template('uploadAttendance.html'),
            200, headers)
