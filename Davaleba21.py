import json

class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

class Student:
    row_id = 0  

    def __init__(self, name, mark, address_city, address_street):
        self.name = name
        self.mark = mark
        self.address = Address(address_city, address_street)
        Student.row_id += 1
        self.student_id = Student.row_id
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.mark >= 91:
            return 'A'
        elif self.mark >= 81:
            return 'B'
        elif self.mark >= 71:
            return 'C'
        else:
            return 'D'

def save_students_to_file(filename, students):
    student_data = []
    for student in students:
        student_data.append({
            "row_id": student.student_id,
            "name": student.name,
            "mark": student.mark,
            "address": {
                "city": student.address.city,
                "street": student.address.street
            },
            "grade": student.grade
        })
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(student_data, file, indent=2)
        

def print_student_data(students):
    student_data = []
    for student in students:
        student_data.append({
            "row_id": student.student_id,
            "name": student.name,
            "mark": student.mark,
            "address": {
                "city": student.address.city,
                "street": student.address.street
            },
            "grade": student.grade
        })
    print(json.dumps(student_data, indent=2))

#===========================================
students = [
    Student("Paata", 87, "Tbilisi", "Saburtalo"),
    Student("Demetre", 100, "Tbilisi", "Gldani-7-11-4-93"),
    Student("Alexander", 100, "Tbilisi", "Gldani-7-11-4-93"),
    Student("Teona", 92, "Tbilisi", "Gldani-7-11-4-93"),
    Student("Nino", 99, "Tbilisi", "Leselidzs str. 25"),
    Student("Andria", 87, "Tbilisi", "Varketili IV 407-5-123")
]

print_student_data(students)

#პროგრამა დამატებით ცალკე ასევე წერს grade-ს (A, B, C, D), mark-ის (ქულის) შესაბამისად.