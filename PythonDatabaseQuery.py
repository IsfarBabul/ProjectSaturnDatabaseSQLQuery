import mysql.connector


def get_database_connection():
    connection = mysql.connector.connect(user='isfarb2',
                                   password='222499881',
                                   host='10.8.37.226',
                                   database='isfarb2_db')
    return connection


def execute_statement(connection, statement):
    cursor = connection.cursor()
    cursor.execute(statement)
    results = []

    for row in cursor:
        results.append(row)

    cursor.close()
    connection.close()

    return results


def get_student_schedule(student_id):
    statement = "CALL Select_Student('" + student_id + "')"
    return execute_statement(get_database_connection(), statement)


student_id = input("Enter a student ID: ")
results = get_student_schedule(student_id)

for result in results:
    print("Period: ", result[0])
    print("Course: ", result[1])
    print("Room: ", result[2])
    print("Teacher: ", result[3])
    print()






