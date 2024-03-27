# Lesson 13 / Homework
# Create a class hierarchy to describe the academy.
# Sample list of classes: Person, Teacher, Student, Subject, Academy, etc.
# Think about the architecture: implement the principles of OOP


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Teacher(Person):
    def __init__(self, name, age, subjects=None):
        super().__init__(name, age)
        self.subjects = subjects if subjects else []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def __str__(self):
        return super().__str__() + f", Teaches: {', '.join(self.subjects)}"


class Student(Person):
    def __init__(self, name, age, enrolled_subject=None):
        super().__init__(name, age)
        self.enrolled_subject = enrolled_subject

    def enroll(self, subject):
        self.enrolled_subject = subject

    def __str__(self):
        return super().__str__() + f", Enrolled in: {self.enrolled_subject}"


class Subject:
    def __init__(self, name, teacher=None):
        self.name = name
        self.teacher = teacher

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def __str__(self):
        return f"Subject: {self.name}, Teacher: {self.teacher}"


class Academy:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        self.subjects = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def __str__(self):
        return f"Academy: {self.name}, Teachers: {len(self.teachers)}, Students: {len(self.students)}, Subjects: {len(self.subjects)}"


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
