from datetime import datetime
import faker
from random import randint, choice
import sqlite3

number_students = 30
number_teachers = 5
number_courses = 5

def generate_fake_data(number_students, number_teachers, number_courses) -> tuple():
    fake_students = []
    fake_teachers = []
    fake_courses = []

    fake_data = faker.Faker()

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    for _ in range(number_courses):
        fake_courses.append(fake_data.job())

    return fake_students, fake_teachers, fake_courses

def prepare_data(students, teachers, courses) -> tuple():
    for_students = []
    for_groups = []
    for_grades = []

    for student in students:
        for_students.append((student, ))
        for_groups.append((randint(1, 3), student))
        for month in range(1, 12 + 1):
            grade_date = datetime(2022, month, randint(10, 27)).date()
            for course in courses:
                for _ in range(1, randint(1, 20)):
                    for_grades.append((student, course, randint(1, 5), grade_date))

    for_teachers = []
    for_courses = []

    for teacher in teachers:
        for_teachers.append((teacher, ))
        for_courses.append((choice(courses), teacher))

    return  for_students, for_groups, for_teachers, for_courses, for_grades

def insert_data_to_db(students, groups, teachers, courses, grades) -> None:

    with sqlite3.connect('tables.db') as con:

        cur = con.cursor()

        sql_to_students = """INSERT INTO students(name)
                               VALUES (?)"""
        cur.executemany(sql_to_students, students)

        sql_to_groups = """INSERT INTO groups(group_number, student_name)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_groups, groups)

        sql_to_teachers = """INSERT INTO teachers(name)
                                       VALUES (?)"""
        cur.executemany(sql_to_teachers, teachers)

        sql_to_courses = """INSERT INTO courses(course, teacher_name)
                                       VALUES (?, ?)"""
        cur.executemany(sql_to_courses, courses)

        sql_to_grades = """INSERT INTO grades(student_name, course_name, grade, date_grade)
                              VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_grades, grades)

        con.commit()


if __name__ == "__main__":
    students, groups, teachers, courses, grades = prepare_data(*generate_fake_data(number_students, number_teachers, number_courses))
    insert_data_to_db(students, groups, teachers, courses, grades)