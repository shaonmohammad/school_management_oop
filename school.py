
class School:
    def __init__(self,name,address) -> None:
        self.name = name
        self.address = address
        self.teacher = {}
        self.classrooms = {}

    def add_teacher(self,subject,teacher):
        self.teacher[subject] = teacher

    def add_class_room(self,classroom):
        self.classrooms[classroom.name] = classroom

    def student_addmission(self,student):
        className = student.classroom.name
        if className in self.classrooms:
            self.classrooms[className].add_student(student)
        else:
            print(f'no class room as name {className}')
    def __repr__(self) -> str:
        print('-----------ALL Class Room------------')
        for key,value in self.classrooms.items():
            print(key)

        print('---------Student----------')
        eight = self.classrooms['eight']
        for stuent in eight.students:
            print(stuent.name)

        print('--------------Subject----------------')
        for subject in eight.subjects:
            print(subject.name, subject.teacher.name)

        print('-----------Student Exam Mark------------')
        for student in eight.students:
            for key,value in student.marks.items():
                print(student.name , key,value)
            print('----------student end-------')
        for key,value in eight.students[0].marks.items():
            print(key, value)
        return ''

class Subject:
    def __init__(self,name,teacher) -> None:
        self.name = name
        self.teacher = teacher
        max_marks = 100
        pass_marks = 33

    def exam(self,students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.name] = mark
class classRoom:
    def __init__(self,name) -> None:
        self.name = name 

        self.students = []
        self.subjects = []

    def add_student(self,student):
        serial_id = f'{self.name}-{len(self.students)+1}'
        student.id = serial_id
        self.students.append(student)

    def add_subject(self,subject):
        self.subjects.append(subject)

    def teke_semister_final(self):
        for subject in self.subjects:
            subject.exam(self.students)
            

    def __str__(self) -> str:
        return f'{self.name}-{self.students}'
    
    #find top student
    def get_top_students(self):
        pass

    