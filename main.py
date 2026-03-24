# from https://www.py4e.com/html3/15-database

import sqlite3

connection = sqlite3.connect('registration.sqlite')
cursor = connection.cursor()

choice = ""

while choice != "QUIT":

    choice = input("Enter a choice: 1 - Manage Faculty")

    if choice == "1":
        action = input("Enter 1 for List Faculty, 2 for Add Faculty, 3 for Update Faculty")

        if action == "1":
            cursor.execute('SELECT * FROM Faculty')
            print("id, name, email")
            for row in cursor:
                print(row)
        elif action == "2":
            name = input("Enter name")
            email = input("Enter email")
            cursor.execute('INSERT INTO faculty (name, email) VALUES (?, ?)',(name, email))
            connection.commit()
        elif action == "3":
            id = int(input("Enter the ID to update"))
            name = input("Enter name")
            email = input("Enter email")
            cursor.execute('update faculty set name = ?, email = ? WHERE id = ?', (name, email, id) )
            connection.commit()


# to get a transcript for a given student
# select course.Department, Course.Number, course.Credits, Enrollment.Grade from Enrollment
# inner join student on Student.id = Enrollment.Student_ID
# inner join section on Section.ID = Enrollment.Section_ID
# inner join course on Course.id = Section.Course_ID
# where Student_ID = 1


connection.close()