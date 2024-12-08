class SearchStud:
    def __init__(self, filename="student_data.txt"):
        self.filename = filename

    def searchstud(self, Idnum):
        with open(self.filename, "r") as file:
            for line in file:
                student_data = line.strip().split(', ')
                name = student_data[0]
                age = student_data[1]
                idnum = student_data[2]
                email = student_data[3]
                phone = student_data[4]

                if idnum == Idnum:
                    print("\n\tStudent Found!")
                    print("\tStudent's Info\n")
                    print(f"Name: {name}")
                    print(f"Age: {age}")
                    print(f"ID Number: {idnum}")
                    print(f"Email: {email}")
                    print(f"Phone: {phone}")
                    return ""
                
        return "Student not found..."    
    
    def printAllStudentInfo(self):
        print("\n======== All Student's Information ========\n")
        with open(self.filename, "r") as file:
            for line in file:
                student_data = line.strip().split(', ')
                name = student_data[0]
                age = student_data[1]
                idnum = student_data[2]
                email = student_data[3]
                phone = student_data[4]   

                print(f"Name: {name}")
                print(f"Age: {age}")
                print(f"ID Number: {idnum}")
                print(f"Email: {email}")
                print(f"Phone: {phone}")  
                print("")

"""
from student import StudentInfo
import os

class SearchStud:
    def __init__(self, filename="student_data.txt"):
        self.filename = filename
        self.student_data = self.from_file()
    
    def from_file(self):
        students = []
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                pass  # Create an empty file
            print(f"{self.filename} was created.")
        else:
            try:
                with open(self.filename, "r") as file:
                    for line in file:
                        name, age, idnum, email, phone = line.strip().split(', ')
                        student = StudentInfo()
                        student.setName(name)
                        student.setAge(int(age))  # Convert age to integer
                        student.setIdnum(idnum)
                        student.setEmail(email)
                        student.setPhone(phone)
                        students.append(student)
            except FileNotFoundError:
                print(f"File {self.filename} not found. A new file will be created.")
        return students

    def searchstud(self, Idnum):
        for student in self.student_data:
            if student.getIdnum() == Idnum:
                print("\n\t Student Found!")
                print("\t Student's Info")
                print(student)
                return ""
        else:
            return "Student not found..."
    
    def printAllStudentInfo(self):
        print("\n======== All Student's Information ========\n")
        for student in self.student_data.allstudents:
            print(student)
"""