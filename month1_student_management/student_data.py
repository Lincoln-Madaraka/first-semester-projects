students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = float(input("Enter student grade(numerical): "))
    
    student = {"name": name, "age": age, "grade": grade}
    students.append(student)
    print(f"{name} has been added.\n")

def view_students():
    if not students:
        print("No students added yet.\n")
        return
    print("Students:")
    for i, student in enumerate(students, 1):
        print(f"{i}. {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    print()

def get_average_grade():
    if not students:
        print("No students added yet.\n")
        return
    total = sum(student['grade'] for student in students)
    average = total / len(students)
    print(f"Average grade: {average:.2f}\n")
