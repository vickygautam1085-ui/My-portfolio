students = []


def add_student():

    try:
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))

        student = {
            "name": name,
            "marks": marks
        }

        students.append(student)

        print("Student added!")

    except ValueError:
        print("Please enter valid marks.")


def show_students():

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print("\nName:", student["name"])
        print("Marks:", student["marks"])
        print("----------------")


def search_student():

    name = input("Enter name to search: ")

    for student in students:

        if student["name"].lower() == name.lower():

            print("Student found!")
            print("Name:", student["name"])
            print("Marks:", student["marks"])

            return

    print("Student not found.")


def delete_student():

    name = input("Enter name to delete: ")

    for student in students:

        if student["name"].lower() == name.lower():

            students.remove(student)

            print("Student deleted!")

            return

    print("Student not found.")


def save_students():

    with open("students.txt", "w") as file:

        for student in students:

            file.write(
                student["name"] + "," +
                str(student["marks"]) + "\n"
            )

    print("Data saved!")


while True:

    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Save Data")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        save_students()

    elif choice == "6":
        print("Program closed.")
        break

    else:
        print("Invalid choice.")