"""Q16: Five subjects, each out of 100; A>=90, B>=75, C>=60, D>=40."""
def student_grade(marks):
    if len(marks) != 5: raise ValueError("Exactly five subjects required")
    if any(mark < 0 or mark > 100 for mark in marks): raise ValueError("Marks must be 0..100")
    total = 0
    for mark in marks: total += mark
    percentage = total / 5
    grade = "A" if percentage >= 90 else "B" if percentage >= 75 else "C" if percentage >= 60 else "D" if percentage >= 40 else "Fail"
    return {"total": total, "percentage": percentage, "grade": grade}
def main():
    try:
        marks = [float(input(f"Subject {i} mark: ")) for i in range(1, 6)]
        for key, value in student_grade(marks).items(): print(f"{key}: {value}")
    except ValueError as e: print("Invalid input:", e)
if __name__ == "__main__": main()
