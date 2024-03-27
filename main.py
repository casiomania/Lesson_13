# Lesson 13 / Homework
# Create a class hierarchy to describe the academy.
# Sample list of classes: Person, Teacher, Student, Subject, Academy, etc.
# Think about the architecture: implement the principles of OOP


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def __str__(self):
        return f"Name: {self.__name}, Age: {self.__age}"


class Teacher(Person):
    def __init__(self, name, age, subjects=None):
        super().__init__(name, age)
        self.__subjects = subjects if subjects else []

    def add_subject(self, subject):
        self.__subjects.append(subject)

    def get_subjects(self):
        return self.__subjects

    def __str__(self):
        return super().__str__() + f", Teaches: {', '.join(self.__subjects)}"


class Student(Person):
    def __init__(self, name, age, enrolled_subject=None):
        super().__init__(name, age)
        self.__enrolled_subject = enrolled_subject

    def enroll(self, subject):
        self.__enrolled_subject = subject

    def get_enrolled_subject(self):
        return self.__enrolled_subject

    def __str__(self):
        return super().__str__() + f", Enrolled in: {self.__enrolled_subject}"


class Subject:
    def __init__(self, name, teacher=None):
        self.__name = name
        self.__teacher = teacher

    def assign_teacher(self, teacher):
        self.__teacher = teacher

    def get_name(self):
        return self.__name

    def get_teacher(self):
        return self.__teacher

    def __str__(self):
        return f"Subject: {self.__name}, Teacher: {self.__teacher}"


class Academy:
    def __init__(self, name):
        self.__name = name
        self.__teachers = []
        self.__students = []
        self.__subjects = []

    def add_teacher(self, teacher):
        self.__teachers.append(teacher)

    def add_student(self, student):
        self.__students.append(student)

    def add_subject(self, subject):
        self.__subjects.append(subject)

    def __str__(self):
        return f"Academy: {self.__name}, Teachers: {len(self.__teachers)}, Students: {len(self.__students)}, Subjects: {len(self.__subjects)}"


# Example
academy = Academy("Python Academy")

teacher_andrii = Teacher("Andrii", 30)
teacher_andrii.add_subject("Django")
academy.add_teacher(teacher_andrii)

teacher_dmytro = Teacher("Dmytro", 35)
teacher_dmytro.add_subject("Flask")
academy.add_teacher(teacher_dmytro)

student_serhii = Student("Serhii", 26)
student_serhii.enroll("Django")
academy.add_student(student_serhii)

student_anton = Student("Anton", 22)
student_anton.enroll("Flask")
academy.add_student(student_anton)

subject_django = Subject("Django", teacher_andrii)
academy.add_subject(subject_django)

subject_flask = Subject("Flask", teacher_dmytro)
academy.add_subject(subject_flask)

print(academy)
