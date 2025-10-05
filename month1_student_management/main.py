from student_data import add_student, view_students, get_average_grade

def menu():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Get Average Grade")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            get_average_grade()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    menu()
