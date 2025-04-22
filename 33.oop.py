
# Object Oriented Programming - Programare Orientata Obiect

## Definire a clasei
class Student:
    def __init__(self, p, n,  v):
        self.nume =  n
        self.prenume = p
        self.varsta = v

    def este_major(self):
        return self.varsta >= 18

## Crearea unui obiect

obiect_student = Student("Marius", "Florinescu", 17)
print(obiect_student)

print(obiect_student.nume, obiect_student.prenume, obiect_student.varsta)
print("Studentul este major:", obiect_student.este_major())

student2 = Student("Maria", "Marinescu", 22)
print(student2)
print(student2.nume, student2.prenume, student2.varsta)
print("Studentul2 este major:", student2.este_major())



