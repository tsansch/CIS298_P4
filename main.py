# from https://www.py4e.com/html3/15-database

import sqlite3

connection = sqlite3.connect('registration.sqlite')
cursor = connection.cursor()

choice = ""

while choice != "QUIT":
    print()
    print("--- Main Menu ---")
    print("1 - Manage Faculty")
    print("2 - Manage Courses")
    print("3 - Manage Sections")
    print("4 - Manage Students")
    print("5 - Manage Enrollments")
    print("6 - View Student Transcript")
    print("QUIT - Exit")
    
    choice = input("Enter a choice: ")

    if choice == "1":
        action = input("Enter 1 for List Faculty, 2 for Add Faculty, 3 for Update Faculty: ")

        if action == "1":
            cursor.execute('SELECT * FROM Faculty')
            print("id, name, email")
            for row in cursor:
                print(row)
        elif action == "2":
            name = input("Enter name: ")
            email = input("Enter email: ")
            cursor.execute('INSERT INTO faculty (name, email) VALUES (?, ?)',(name, email))
            connection.commit()
            print("Faculty added.")
        elif action == "3":
            id = int(input("Enter the ID to update: "))
            name = input("Enter name: ")
            email = input("Enter email: ")
            cursor.execute('update faculty set name = ?, email = ? WHERE id = ?', (name, email, id) )
            connection.commit()
            print("Faculty updated.")

    elif choice == "2":
        action = input("Enter 1 for List Courses, 2 for Add Course, 3 for Update Course: ")

        if action == "1":
            cursor.execute('SELECT * FROM Course')
            print("id, department, number, credits, description")
            for row in cursor:
                print(row)
        elif action == "2":
            dept = input("Enter department: ")
            number = input("Enter course number: ")
            credits = int(input("Enter credits: "))
            desc = input("Enter description: ")
            cursor.execute('INSERT INTO Course (Department, Number, Credits, Description) VALUES (?, ?, ?, ?)', (dept, number, credits, desc))
            connection.commit()
            print("Course added.")
        elif action == "3":
            id = int(input("Enter the ID to update: "))
            dept = input("Enter department: ")
            number = input("Enter course number: ")
            credits = int(input("Enter credits: "))
            desc = input("Enter description: ")
            cursor.execute('UPDATE Course SET Department = ?, Number = ?, Credits = ?, Description = ? WHERE ID = ?', (dept, number, credits, desc, id))
            connection.commit()
            print("Course updated.")

    elif choice == "3":
        action = input("Enter 1 for List Sections, 2 for Add Section, 3 for Update Section: ")

        if action == "1":
            cursor.execute('SELECT * FROM Section')
            print("id, course_id, faculty_id, semester, day, time")
            for row in cursor:
                print(row)
        elif action == "2":
            course_id = int(input("Enter Course ID: "))
            faculty_id = int(input("Enter Faculty ID: "))
            semester = input("Enter Semester: ")
            day = input("Enter Day: ")
            time = input("Enter Time: ")
            cursor.execute('INSERT INTO Section (Course_ID, Faculty_ID, Semester, Day, Time) VALUES (?, ?, ?, ?, ?)', (course_id, faculty_id, semester, day, time))
            connection.commit()
            print("Section added.")
        elif action == "3":
            id = int(input("Enter the ID to update: "))
            course_id = int(input("Enter Course ID: "))
            faculty_id = int(input("Enter Faculty ID: "))
            semester = input("Enter Semester: ")
            day = input("Enter Day: ")
            time = input("Enter Time: ")
            cursor.execute('UPDATE Section SET Course_ID = ?, Faculty_ID = ?, Semester = ?, Day = ?, Time = ? WHERE ID = ?', (course_id, faculty_id, semester, day, time, id))
            connection.commit()
            print("Section updated.")

    elif choice == "4":
        action = input("Enter 1 for List Students, 2 for Add Student, 3 for Update Student: ")

        if action == "1":
            cursor.execute('SELECT * FROM Student')
            print("id, name, major")
            for row in cursor:
                print(row)
        elif action == "2":
            name = input("Enter student name: ")
            major = input("Enter student major: ")
            cursor.execute('INSERT INTO Student (Name, Major) VALUES (?, ?)', (name, major))
            connection.commit()
            print("Student added.")
        elif action == "3":
            id = int(input("Enter the ID to update: "))
            name = input("Enter student name: ")
            major = input("Enter student major: ")
            cursor.execute('UPDATE Student SET Name = ?, Major = ? WHERE ID = ?', (name, major, id))
            connection.commit()
            print("Student updated.")

    elif choice == "5":
        action = input("Enter 1 for List Enrollments, 2 for Add Enrollment, 3 for Update Enrollment, 4 for Delete Enrollment: ")

        if action == "1":
            cursor.execute('SELECT * FROM Enrollment')
            print("id, student_id, section_id, grade")
            for row in cursor:
                print(row)
        elif action == "2":
            student_id = int(input("Enter Student ID: "))
            section_id = int(input("Enter Section ID: "))
            grade = input("Enter Grade: ")
            cursor.execute('INSERT INTO Enrollment (Student_ID, Section_ID, Grade) VALUES (?, ?, ?)', (student_id, section_id, grade))
            connection.commit()
            print("Enrollment added.")
        elif action == "3":
            id = int(input("Enter the ID to update: "))
            student_id = int(input("Enter Student ID: "))
            section_id = int(input("Enter Section ID: "))
            grade = input("Enter Grade: ")
            cursor.execute('UPDATE Enrollment SET Student_ID = ?, Section_ID = ?, Grade = ? WHERE ID = ?', (student_id, section_id, grade, id))
            connection.commit()
            print("Enrollment updated.")
        elif action == "4":
            id = int(input("Enter the ID to delete: "))
            cursor.execute('DELETE FROM Enrollment WHERE ID = ?', (id,))
            connection.commit()
            print("Enrollment deleted.")

    elif choice == "6":
        student_id = int(input("Enter the Student ID to view their transcript: "))
        
        # to get a transcript for a given student
        cursor.execute('''
            SELECT Course.Department, Course.Number, Course.Credits, Enrollment.Grade 
            FROM Enrollment
            INNER JOIN Student ON Student.ID = Enrollment.Student_ID
            INNER JOIN Section ON Section.ID = Enrollment.Section_ID
            INNER JOIN Course ON Course.ID = Section.Course_ID
            WHERE Student.ID = ?
        ''', (student_id,))
        
        results = cursor.fetchall()
        
        print()
        print("--- Transcript for Student ID", student_id, "---")
        print("Department, Number, Credits, Grade")
        for row in results:
            print(row)
        print("-----------------------------------")

connection.close()