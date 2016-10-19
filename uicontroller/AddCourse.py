from __init__ import *

class AddCourse(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(
            render_template('addCourses.html'),
            200, headers)

    def post(self):
        row = (request.form["CourseID"], request.form["CourseName"])
        conn = getConnection()
        # conn.execute(
        #     'CREATE TABLE courses (CourseID TEXT, CourseName TEXT)')
        conn.execute('insert into courses values (?,?)', row)
        conn.commit()
        print "Table created successfully"
        conn.close()
        return "course data stored"