"""Q9: Summarize marks (pass threshold = 40)."""
def analyze_marks(marks):
    if not marks: raise ValueError("At least one mark is required")
    if any(mark < 0 or mark > 100 for mark in marks): raise ValueError("Marks must be 0..100")
    highest = lowest = marks[0]
    total = passed = failed = 0
    for mark in marks:
        total += mark
        if mark > highest: highest = mark
        if mark < lowest: lowest = mark
        if mark >= 40: passed += 1
        else: failed += 1
    return dict(highest=highest, lowest=lowest, average=total / len(marks), passed=passed, failed=failed)
def main():
    try:
        marks = [float(x) for x in input("Student marks (space-separated): ").split()]
        for key, value in analyze_marks(marks).items(): print(f"{key}: {value:g}")
    except ValueError as e: print("Invalid input:", e)
if __name__ == "__main__": main()
