import zipfile

import zipstream

from __init__ import *


class GetStudents(Resource):
    def post(self):
        subject = request.form["CourseCode"]
        studentList = []
        conn = getConnection()
        query1 = 'SELECT * FROM students WHERE Subject1 =' + "'" + subject + "'"
        cursor1 = conn.execute(query1).fetchall()
        studentList.append(cursor1)

        query2 = 'SELECT * FROM students WHERE Subject2 =' + "'" + subject + "'"
        cursor2 = conn.execute(query2).fetchall()
        studentList.append(cursor2)

        query3 = 'SELECT * FROM students WHERE Subject3 =' + "'" + subject + "'"
        cursor3 = conn.execute(query3).fetchall()
        studentList.append(cursor3)

        query4 = 'SELECT * FROM students WHERE Subject4 =' + "'" + subject + "'"
        cursor4 = conn.execute(query4).fetchall()
        studentList.append(cursor4)

        # queryTest = 'ALTER TABLE students ADD COLUMN FacType TEXT;'
        # queryTest = 'alter table students drop column FacType'
        # conn.execute(queryTest)
        # conn.commit()


        print studentList

        zf = zipfile.ZipFile('data.zip',
                             mode='w',
                             compression=zipfile.ZIP_DEFLATED,
                             )

        for i in range(0, 4):
            if not len(studentList[i]) == 0:
                try:
                    for item in studentList[i]:
                        str = ""
                        str = str + item[1] + "\n"
                        str = str + item[2] + "\n"
                        str = str + item[0] + "\n"
                        str = str + item[8] + "\n"
                        str = str + item[9] + "\n"
                        zf.writestr(item[0], str)

                finally:
                    zf.close()
        archive = zipfile.ZipFile('data.zip', 'r')
        # for item in cursor:
        #     print item
        print "Data fetched Successfully"
        conn.close()
        archive.close()
        return send_from_directory('', 'data.zip', as_attachment=True,
                                   mimetype='application/octet-stream')

