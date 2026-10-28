names = []
marks = []


for i in range(3):
    name = input("Enter student name: ")
    mark = int(input("Enter student marks (0-100): "))

    names.append(name)
    marks.append(mark)


print("\nStudent Records:")

for i in range(len(names)):
    print(f"{names[i]} - {marks[i]}")


search_name = input("\nEnter student name to search: ")

if search_name in names:
    index = names.index(search_name)
    print(f"{search_name} scored {marks[index]} marks.")
else:
    print("Student not found.")


highest = max(marks)
lowest = min(marks)

highest_index = marks.index(highest)
lowest_index = marks.index(lowest)

print(f"\nHighest scorer: {names[highest_index]} - {highest}")
print(f"Lowest scorer: {names[lowest_index]} - {lowest}")


print("\nStudents sorted by marks:")

sorted_indices = sorted(range(len(marks)), key=lambda i: marks[i])

for i in sorted_indices:
    print(f"{names[i]} - {marks[i]}")