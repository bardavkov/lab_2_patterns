"""lab 2"""

'''import libraries'''

from datetime import datetime
from typing import List, Any
from dataclasses import dataclass
from abc import ABC, abstractmethod
import random

'''dataclass for info ab students and lecturers '''


@dataclass
class personal_info:
    id: int
    name: str
    surname: str
    # adress: str
    # phone_number: str
    # position: str
    # rank: str
    salary: float


'''you can send all your requests to department'''


class Department:
    def __init__(self, title: str):
        self.students: List[Student] = []
        self.lecturers: List[Lecturer] = []
        self.courses: List[Course.title] = []
        self.requests: List[Any] = []
        self.ill_requests: List[Any] = []

    def proceed_requests(self):
        return self.requests


class Course:  # info abt course

    def __init__(self, title: str,
                 assignments: list[str], limit: int, students_num: int, students_limit: int):
        self.title = title
        self.limit = students_limit

        self.assignments = assignments
        self.students: Student = []
        self.seminars: List = []

    # function for add students to list
    def add_student(self, student: List):

        if self.limit > len(self.students):
            student.courses.append(self.title)
            self.students.append(student)
            Enrollment.enroll(student, self)
            print(f'Student {student.name} as been added to the course {self.title}')
        else:
            print('Too many students')

    # function for removing students from list
    def delete_student(self, student):
        student.unenroll(self.title)
        self.students.remove(student)


# bridge between student\lecturer and department
class staff(personal_info):

    @abstractmethod
    def ask_sick_alive(self, department: Department) -> bool:
        pass

    @abstractmethod
    def send_request(self, department: Department) -> bool:
        pass


class Student(staff):
    average_mark = 0
    course_progress = [1, 2, 5, 7]
    courses: List[Course] = []

    def send_request(self, department: Department) -> bool:
        a = input('write request : ')
        department.requests.append(f'student {self.name} want a {a}')

    def ask_sick_alive(self, department: Department):
        department.ill_requests.append(f'student {self.name} is ill')
        rand = bool(random.getrandbits(1))
        if rand is True:
            return print(f'{self.name} are free')
        else:
            return print('sit on your lectures')

    def taken_courses(self):
        return print(f'{self.courses}')


class PostGraduateStudent(Student):
    pass

#class Lecturer inherit personal_info
class Lecturer(personal_info):
    average_mark = 0
    post_students: List[PostGraduateStudent] = []

    def check_assignment(self, assignment: dict) -> None:
        if assignment["is_done"]:
            assignment["mark"] = 5.0

    def ask_sick_alive(self, department: Department) -> bool:
        return print(department.ill_requests)

    def send_request(self, department: Department):
        return print(department.requests)

    def add_postgraduate_student(self, pst_student: PostGraduateStudent):
        self.post_students.append(pst_student)

#new class
class Seminars:
    def __init__(self, id):
        self.id = id

        title = ' '
        assignments: List[dict] = []
        related_course: str = ' '

        def implement_item(self, lol):
            pass


class CourseProgres:
    """ course progres of chosen student """

    def __init__(self, received_marks: dict,
                 visited_lectures: int,
                 assignment: dict):
        self.received_marks = received_marks
        self.visited_lectures = visited_lectures
        self.assignments = {}
        self.assignment = assignment

    # marks are taken from received marks
    def get_final_mark(self) -> float:
        final_mark = sum(self.received_marks.values()) / len(self.received_marks)
        return final_mark

#class for enroll on courses (bridge between student and course classes)
class Enrollment:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def enroll(student: Student, course: Course):
        student.courses.append(course)

    @staticmethod
    def unenroll(student: Student, course: Course):
        student.courses.remove(course)
        # self.courses = list(filter(lambda x: x.title == course_title, self.courses))
        print(f'Student {student.name} unenrolled from {course.title}')


lol = Student(4, 'lol', 'bardakov', 45.5)
lol_1 = Lecturer(4, 'lol', 'bardakov', 45.5)
enr = Enrollment
assignment_2 = {"title": "testing", "description": "testing", "is_done": True, "mark": 0.0}
course_2 = Course('course_fei', assignment_2, 11, 10, 78)
course_2.add_student(lol)
#enr.enroll(lol, course_2)
enr.unenroll(lol, course_2)