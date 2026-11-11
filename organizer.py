
student_details = ("Vasy", 9, "WNSS", "2026")

print("===== STUDENT DETAILS =====")
print("Name:", student_details[0])
print("Grade:", student_details[1])
print("School:", student_details[2])
print("School Year:", student_details[3])

monday_subjects = {"Math", "English", "Science", "History"}
tuesday_subjects = {"Math", "Geography", "Science", "French"}
wednesday_subjects = {"English", "Science", "Computer Studies"}

print("\n===== WEEKLY SUBJECTS =====")
print("Monday:", monday_subjects)
print("Tuesday:", tuesday_subjects)
print("Wednesday:", wednesday_subjects)

print("\n===== MODIFY SUBJECTS =====")

monday_subjects.add("Physical Education")
print("Monday after adding:", monday_subjects)

tuesday_subjects.remove("Geography")
print("Tuesday after removing:", tuesday_subjects)

wednesday_subjects.update(["Art", "French"])
print("Wednesday after updating:", wednesday_subjects)

print("\n===== SUBJECT COMPARISONS =====")

print("All subjects:", monday_subjects.union(tuesday_subjects))

print("Common subjects:", monday_subjects.intersection(tuesday_subjects))

print("Monday only:", monday_subjects.difference(tuesday_subjects))

print("Different subjects:", monday_subjects.symmetric_difference(tuesday_subjects))

print("\n===== SUBJECT SEARCH =====")
if "Math" in monday_subjects:
    print("Math is scheduled for Monday!")
else:
    print("Math is not scheduled for Monday.")

print("\n===== PLANNER COMPLETE =====")
