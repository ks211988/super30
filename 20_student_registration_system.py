"""Q20: Full student CRUD system; records stored in a dictionary keyed by ID."""
def validate_student(student_id, name, marks):
    if not student_id.strip() or not name.strip(): raise ValueError("ID and name are required")
    if not 0 <= marks <= 100: raise ValueError("Marks must be 0..100")
def add_student(students, student_id, name, marks):
    validate_student(student_id, name, marks)
    if student_id in students: raise ValueError("Student ID already exists")
    students[student_id] = {"name": name, "marks": marks}
def view_students(students):
    return [(student_id, info["name"], info["marks"]) for student_id, info in students.items()]
def search_student(students, student_id): return students.get(student_id)
def update_student(students, student_id, name, marks):
    if student_id not in students: raise ValueError("Student not found")
    validate_student(student_id, name, marks)
    students[student_id] = {"name": name, "marks": marks}
def delete_student(students, student_id):
    if student_id not in students: return False
    del students[student_id]
    return True
def class_average(students):
    if not students: return None
    total = 0
    for record in students.values(): total += record["marks"]
    return total / len(students)
def top_student(students):
    if not students: return None
    best_id = None
    best_record = None
    for student_id, record in students.items():
        if best_record is None or record["marks"] > best_record["marks"]:
            best_id, best_record = student_id, record
    return best_id, best_record.copy()
def ask_details():
    student_id = input("ID: ").strip()
    name = input("Name: ").strip()
    marks = float(input("Marks (0-100): "))
    return student_id, name, marks
def main():
    students = {}
    while True:
        print("\n1 Add  2 View all  3 Search  4 Update  5 Delete  6 Average  7 Top student  8 Exit")
        choice = input("Choose: ").strip()
        if choice == "8": print("Goodbye!"); break
        try:
            if choice == "1":
                add_student(students, *ask_details()); print("Student added")
            elif choice == "2":
                for student_id, name, marks in view_students(students): print(f"{student_id}: {name}, {marks:g}")
                if not students: print("No students")
            elif choice == "3":
                print(search_student(students, input("Search ID: ").strip()) or "Not found")
            elif choice == "4":
                student_id, name, marks = ask_details()
                update_student(students, student_id, name, marks); print("Updated")
            elif choice == "5":
                print("Deleted" if delete_student(students, input("Delete ID: ").strip()) else "Not found")
            elif choice == "6":
                avg = class_average(students)
                print(f"Class average: {avg:.2f}" if avg is not None else "No students")
            elif choice == "7":
                best = top_student(students)
                print(f"Top student: {best[0]} - {best[1]['name']} ({best[1]['marks']:g})" if best else "No students")
            else: print("Invalid option")
        except ValueError as e: print("Invalid input:", e)
if __name__ == "__main__": main()
