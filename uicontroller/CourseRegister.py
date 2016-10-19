from __init__ import *

class CourseRegister(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(
            render_template('CourseRegister.html'),
            200, headers)

    def post(self):
        row = (request.form["StudentID"], request.form["CourseID"])
        conn = getConnection()
        # conn.execute('CREATE TABLE register_courses (StudentID TEXT, CourseID TEXT)')
        conn.execute('insert into register_courses values (?,?)', row)
        conn.commit()
        print "Table created successfully"
        conn.close()
        return "User data stored"