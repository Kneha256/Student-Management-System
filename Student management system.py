student={}
def add_student():
    stu=input("Enter Student name: ")
    marks=int(input("Enter marks : "))
    student[stu]=marks
    print(f"add:{stu} with marks = {marks}")
def update_marks():
    stu=input("enter student name: ")
    if stu in student.keys():
        marks=int(input("Enter marks: "))
        student.update({stu:marks})
        print(f"Updated marks:{student}")
    else:
        marks=int(input("Student not found! Enter marks: "))
        student.update({stu:marks})
        print(f"Updated marks:{student}")

def search_student():
    stu=input("Enter student name : ")
    if stu in student.keys():
        print(f"{stu}'s data exist")
    else:
        print(f"No data found related to {stu}")
def display_all():
    if student:
        print("All students and their marks:")
        for name, marks in student.items():
            print(f"Name: {name}, Marks: {marks}")
        print()
    else:
        print("No student data available.\n")

menu="""Enter A to add a new student
Enter B to updat marks of a student
Enter C to seach a student
Enter D to print all students data along with marks
Type STOP to exit..."""

print(menu)

while(True):
    action_key=input("Enter your action key: ").upper()
    if action_key=="STOP":
        break
    elif(action_key=="A"):
        add_student()
    elif(action_key=="B"):
        update_marks()
    elif(action_key=="C"):
        search_student()
    elif(action_key=="D"):
        display_all()
    else:
        print("Invaild input! please try again...")

