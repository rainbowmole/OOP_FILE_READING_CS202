from student import StudentInfo

class AddStudent:
    def __init__(self, student_data, filename="student_data.txt"):
        self.student_data = student_data
        self.filename = filename

    def store_in_file(self, student):
        with open(self.filename, "a+") as file:
            file.write(student.to_file())

    def add_student(self, name, age, idnum, email, phone):
        student = StudentInfo()

        student.setName(name)
        student.setAge(age)
        student.setIdnum(idnum)
        student.setEmail(email)
        student.setPhone(phone)

        self.store_in_file(student)
        print(f'\nAdded student {name} to the list')
    
    def new_student(self):
        newstud = StudentInfo()

        print("\n===ADD NEW STUDENT===")
        name, age, idnum, email, phone = input("\nEnter Name: "), int(input("Enter Age: ")), input("Enter ID Number: "), input("Enter Email: "), input("Enter Phone Number: ")
        print("\n===NOTHING FOLLOWS===\n")

        newstud.setName(name)
        newstud.setAge(age)
        newstud.setIdnum(idnum)
        newstud.setEmail(email)
        newstud.setPhone(phone)

        self.store_in_file(newstud)
        print(f'\nAdded student {name} to the list')

    

