from student import StudentInfo

class openAcc:
    def __init__(self, filename="student_data.txt"):
        self.filename = filename

    def open_studentAcc(self, idnum):
        with open(self.filename) as file:
            for line in file:
                student_data = line.strip().split(', ')

                name = student_data[0]
                age = student_data[1]
                id_number = student_data[2]
                email = student_data[3]
                phone = student_data[4]

                if id_number == idnum:
                    student = StudentInfo()
                    student.setName(name)
                    student.setAge(age)
                    student.setIdnum(id_number)    
                    student.setEmail(email)
                    student.setPhone(phone)

                    print(f"Welcome, {name}!")
                    return student
                
        print("ID not found..."); return False       


"""
from student import StudentInfo
import os

class openAcc:
    def __init__(self, filename="student_data.txt"):
        self.filename = filename  
        self.student_data = self.from_file()
    
    def from_file(self):
        students = []
        
        
        with open(self.filename, "r") as file:
            for line in file:
                try:
                   
                    name, age, idnum, email, phone = line.strip().split(', ')
                        
                 
                    student = StudentInfo()
                    student.setName(name)
                    student.setAge(int(age))  
                    student.setIdnum(idnum)
                    student.setEmail(email)
                    student.setPhone(phone)
            
                    students.append(student)
                        
                except ValueError:
                    print(f"Skipping invalid line (incorrect format): {line.strip()}")
                except IndexError:
                    print(f"Skipping invalid line (missing data): {line.strip()}")
                        
                except Exception as e:
                    print(f"Error reading file: {e}")
        
        return students

    def open_studentAcc(self, idnum):
        for student in self.student_data:
            if student.getIdnum() == idnum:
                print(f"\nWelcome, {student.getName()}!")
                return student
        else:
            print("ID not found..."); return False
"""