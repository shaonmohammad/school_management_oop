from school import School,classRoom,Subject
from person import Student,Teacher

def main():
    school = School('Adam jee','U TT Ra')
    eight = classRoom('eight')
    school.add_class_room(eight)
    nine = classRoom('nine')
    school.add_class_room(nine)
    ten = classRoom('ten')
    school.add_class_room(ten)

    abul = Student('abir khan',eight)
    school.student_addmission(abul)
 
    babul = Student('babul khan',eight)
    school.student_addmission(babul)
 
    kabul = Student('kabul khan',eight)
    school.student_addmission(kabul)

    #subject
   
    physics_teacher = Teacher('sahjahan')
    physics = Subject('physics',physics_teacher)
    eight.add_subject(physics)
   
    chemistry_teacher = Teacher('haradon')
    chemistry = Subject('chemistry',chemistry_teacher)
    eight.add_subject(chemistry)
    
    biology_teacher = Teacher('ajmol Sir')
    biology = Subject('biology',biology_teacher)
    eight.add_subject(biology)

    eight.teke_semister_final()
    print(school)
if __name__ == '__main__':
    main()
    