print("\n******************************************************")
print("*            🎓 STUDENT GRADE SYSTEM 🎓              *")
print("******************************************************\n")

def calculate_grade(percentage):
    if percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "F"
    else:
        return "Fail"
    
students = []

while True:
    print("══════════════════════════════════════════════════════")
    print("                ✨ Student Details ✨              ")
    print("══════════════════════════════════════════════════════")

    name = input("📍 Student Name: ")
    roll_num = input("📍 Roll Number: ")
    
    subjects = ["Math", "Physics", "Urdu", "English", "Computer"]
    marks ={}
    print("\n📜 Enter Obtained Marks in Given Subjects:")

    for subject in subjects:
        while True:
            try:
                marks[subject] = float(input(f"🔹 {subject} = "))
                if 0<= marks[subject] <=100:
                    break
                else:
                    print("⚠️ Marks should be between 0 and 100. Try Again.")
            except ValueError:
                print("❌ Invalid Input! Please enter Marks in Digits.")

    total_marks = sum(marks.values())
    percentage = (total_marks/(len(subjects)*100))*100
    grade = calculate_grade(percentage)

    students.append({
        "name": name,
        "roll_number": roll_num,
        "total": total_marks,
        "marks": marks,
        "percentage": percentage,
        "grade": grade
    })

    print(f"\n✅ Record of {name} inserted Successfully!")
    while True:
        more = input("Do you want to insert more records? Press 'Y' for Yes or 'N' for No: ").strip().lower()
        if more in ['y', 'n']:
            break
        else:
            print("❌ Invalid choice! Please enter 'Y' for Yes or 'N' for No.")

    if more != 'y':
        break

print("\n══════════════════════════════════════════════════")
print("                📜 Student Report Cards 📜        ")
print("══════════════════════════════════════════════════")

for student in students:
    print("\n-------------------------------------------------")
    print(f"🎓 Student Name  : {student['name']}")
    print(f"🔢 Roll Number   : {student['roll_number']}")
    print("📊 Marks Obtained:")
    for subject, mark in student['marks'].items():
        print(f"   -> {subject} : {mark}")
    print(f"📌 Total Marks   : {student['total']} / 500")
    print(f"📊 Percentage    : {student['percentage']:.2f}%")
    print(f"🎖️ Grade        : {student['grade']}")
    print("-------------------------------------------------")

print("\n🎉 Thank You for Using the Student Grade System! 🎉\n")