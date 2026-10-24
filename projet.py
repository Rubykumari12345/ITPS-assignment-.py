import json
import os

FILENAME = "students_data.json"

def load_data():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_data(students):
    with open(FILENAME, "w") as file:
        json.dump(students, file, indent=4)

def add_student(students):
    roll = input("Enter Roll Number: ")
    for s in students:
        if s["roll"] == roll:
            print("Error: Roll number already exists!")
            return

    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")
    
    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "marks": marks
    }
    students.append(student)
    save_data(students)
    print("Student added successfully!")

def view_students(students):
    if not students:
        print("No student records available.")
        return
    
    print("\n--- Student Records ---")
    for s in students:
        print(f"Roll: {s['roll']} | Name: {s['name']} | Age: {s['age']} | Marks: {s['marks']}")
    print("-------------------------")

def search_student(students):
    roll = input("Enter Roll Number to search: ")
    for s in students:
        if s["roll"] == roll:
            print("\nStudent Found:")
            print(f"Roll: {s['roll']} | Name: {s['name']} | Age: {s['age']} | Marks: {s['marks']}")
            return
    print("Student not found.")

def update_student(students):
    roll = input("Enter Roll Number to update: ")
    for s in students:
        if s["roll"] == roll:
            print("Enter new details (press enter to keep old values):")
            
            name = input(f"New Name ({s['name']}): ") or s['name']
            age = input(f"New Age ({s['age']}): ") or s['age']
            marks = input(f"New Marks ({s['marks']}): ") or s['marks']
            
            s['name'] = name
            s['age'] = age
            s['marks'] = marks
            
            save_data(students)
            print("Student updated successfully!")
            return
    print("Student not found.")

def delete_student(students):
    roll = input("Enter Roll Number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            save_data(students)
            print("Student deleted successfully!")
            return
    print("Student not found.")

def main():
    students = load_data()
    save_data(students)
    while True:
        print("\n--- Student Record Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Roll Number")
        print("4. Update Student Record")
        print("5. Delete Student Record")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            update_student(students)
        elif choice == '5':
            delete_student(students)
        elif choice == '6':
            print("Exiting program. Data saved successfully.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()