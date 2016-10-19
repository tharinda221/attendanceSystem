import zipfile

from __init__ import *


class GetStudents(Resource):
    def post(self):
        subject = request.form["CourseCode"]
        conn = getConnection()

        query1 = 'SELECT StudentID FROM register_courses WHERE CourseID =' + "'" + subject + "'"
        ids = conn.execute(query1).fetchall()
        zf = zipfile.ZipFile('data.zip',
                             mode='w',
                             compression=zipfile.ZIP_DEFLATED,
                             )
        for id in ids:
            query2 = 'SELECT * from students WHERE StudentID =' + "'" + id[0] + "'"
            item = conn.execute(query2).fetchall()
            str = ""
            str = str + item[0][1] + "\n"
            str = str + item[0][2] + "\n"
            str = str + item[0][0] + "\n"
            str = str + item[0][4] + "\n"
            str = str + item[0][5] + "\n"
            zf.writestr(item[0][0], str)

        zf.close()
        zipfile.ZipFile('data.zip', 'r')
        # for item in cursor:
        #     print item
        print "Data fetched Successfully"
        conn.close()
        return send_from_directory('', 'data.zip', as_attachment=True,
                                   mimetype='application/octet-stream')
