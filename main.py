import csv
import os
from datetime import datetime

FILE = "student.csv"

# -----------------------------
# Ensure file exists
# -----------------------------
def init_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Roll", "Name", "Branch", "Semester", "Email", "Phone", "Added On"])

# -----------------------------
# Add Student
# -----------------------------
def add_student():
    print("\n--- Add Student ---")
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    semester = input("Enter Semester: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([roll, name, branch, semester, email, phone, time])

    print("\nStudent Added Successfully!\n")

# -----------------------------
# View All Students
# -----------------------------
def view_students():
    print("\n--- All Students ---\n")
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        data = list(reader)

    if len(data) <= 1:
        print("No students found.\n")
        return

    for row in data:
        print(" | ".join(row))
    print()

# -----------------------------
# Search Student by Roll
# -----------------------------
def search_student():
    roll = input("\nEnter roll to search: ")
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0] == roll:
                print("\nStudent Found:\n")
                print("Roll:", row[0])
                print("Name:", row[1])
                print("Branch:", row[2])
                print("Semester:", row[3])
                print("Email:", row[4])
                print("Phone:", row[5])
                print("Added On:", row[6])
                return
    print("\nStudent Not Found!\n")

# -----------------------------
# Delete Student
# -----------------------------
def delete_student():
    roll = input("\nEnter roll to delete: ")

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        data = list(reader)

    new_data = [data[0]]  # header

    found = False
    for row in data[1:]:
        if row[0] != roll:
            new_data.append(row)
        else:
            found = True

    if not found:
        print("\nStudent Not Found!\n")
        return

    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(new_data)

    print("\nStudent Deleted Successfully!\n")

# -----------------------------
# Update Student
# -----------------------------
def update_student():
    roll = input("\nEnter roll to update: ")

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        data = list(reader)

    updated = False
    for row in data[1:]:
        if row[0] == roll:
            print("\n--- Update Student ---")
            row[1] = input(f"Name ({row[1]}): ") or row[1]
            row[2] = input(f"Branch ({row[2]}): ") or row[2]
            row[3] = input(f"Semester ({row[3]}): ") or row[3]
            row[4] = input(f"Email ({row[4]}): ") or row[4]
            row[5] = input(f"Phone ({row[5]}): ") or row[5]
            updated = True
            break

    if not updated:
        print("\nStudent Not Found!\n")
        return

    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    print("\nStudent Updated Successfully!\n")

# -----------------------------
# Main Menu System
# -----------------------------
def main():
    init_file()

    while True:
        print("""
=========== Student Management System ===========
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("\nInvalid Choice!\n")

if __name__ == "__main__":
    main()
    