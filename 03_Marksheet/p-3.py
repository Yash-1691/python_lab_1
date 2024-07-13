def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 45:
        return "D"
    elif average >= 30:
        return "E"
    else:
        return "F"
def generate_marksheet(marks):
    total_marks = sum(marks)
    average = total_marks / len(marks)
    grade = calculate_grade(average)
    print("\nStudent Marksheet :\n")
    for i, mark in enumerate(marks, start=1):
        print(f"Subject {i}: {mark}")
    print(f"\nTotal Marks: {total_marks}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
def main():
    marks = []
    for _ in range(5):
        marks.append(float(input(f"Enter Marks in Subject {_+1}: ")))
    generate_marksheet(marks)
if __name__ == "__main__":
    main()