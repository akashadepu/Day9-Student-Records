
# 🎓 Student Records Management Using Python Lists — Day 9

## 📌 Project Overview
This project is a beginner-friendly Python program that stores student names and marks in lists. It displays student records, searches for a student, identifies the highest and lowest scores, and sorts students by marks.

## 🎯 Objectives
- Practice Python lists and list methods.
- Understand loops and conditional statements.
- Search for student records.
- Find the highest and lowest marks.
- Sort students by marks while keeping names matched to their scores.

## 🛠️ Technologies Used
- Python 3
- Visual Studio Code

## ✨ Features
- **Add Student Records:** Accept names and marks for three students.
- **Display Records:** Print each student's name and marks.
- **Search Student:** Find a student by name.
- **Highest Score:** Identify the student with the highest marks.
- **Lowest Score:** Identify the student with the lowest marks.
- **Sort Records:** Display students from lowest to highest marks.

## 📂 Project Structure
```text
Day9-Student-Records/
├── student_records.py
└── README.md
```

## 💻 Source Code
```python
names = []
marks = []

# Add 3 students
for i in range(3):
    name = input("Enter student name: ")
    mark = int(input("Enter student marks (0-100): "))

    names.append(name)
    marks.append(mark)

# Display all student records
print("\nStudent Records:")

for i in range(len(names)):
    print(f"{names[i]} - {marks[i]}")

# Search for a student
search_name = input("\nEnter student name to search: ")

if search_name in names:
    index = names.index(search_name)
    print(f"{search_name} scored {marks[index]} marks.")
else:
    print("Student not found.")

# Find highest and lowest marks
highest = max(marks)
lowest = min(marks)

highest_index = marks.index(highest)
lowest_index = marks.index(lowest)

print(f"\nHighest scorer: {names[highest_index]} - {highest}")
print(f"Lowest scorer: {names[lowest_index]} - {lowest}")

# Sort students by marks (lowest to highest)
print("\nStudents sorted by marks:")

sorted_indices = sorted(range(len(marks)), key=lambda i: marks[i])

for i in sorted_indices:
    print(f"{names[i]} - {marks[i]}")
```

## ⚙️ How It Works
1. Two empty lists store student names and marks.
2. A `for` loop accepts three student records.
3. `append()` stores each name and mark.
4. Another loop displays all records.
5. `in` and `index()` search for a student.
6. `max()` and `min()` find the highest and lowest marks.
7. `sorted()` arranges student indexes by marks.
8. The final loop displays the sorted records.

## ▶️ How to Run
1. Install Python 3.
2. Save the code as `student_records.py`.
3. Open a terminal in the project folder.
4. Run:

```bash
python student_records.py
```

On Windows, you can also use:

```bash
py student_records.py
```

## 🧪 Sample Output
```text
Student Records:
Akash - 90
Ramesh - 80
Suresh - 70

Enter student name to search: Ramesh
Ramesh scored 80 marks.

Highest scorer: Akash - 90
Lowest scorer: Suresh - 70

Students sorted by marks:
Suresh - 70
Ramesh - 80
Akash - 90
```

## 📚 Concepts Learned
- Python lists
- `append()`
- `for` loops and `range()`
- `len()`
- `in` and `index()`
- `max()` and `min()`
- `sorted()`
- Lambda expressions for sorting

## ⚠️ Limitations
- The program accepts exactly three students.
- Marks are not validated to ensure they are between 0 and 100.
- Student searches are case-sensitive.
- Records are not saved permanently after the program closes.
- If multiple students have the same highest or lowest marks, only the first matching student is displayed.

## 🚀 Future Improvements
- Allow the user to enter any number of students.
- Validate marks and handle invalid input.
- Support case-insensitive searches.
- Save student records to a file.
- Display all students who share the highest or lowest score.

## 👨‍💻 Author
**Akash Adepu**

Python Programming Internship — Day 9

---
⭐ Built to practice Python list processing through hands-on coding.
