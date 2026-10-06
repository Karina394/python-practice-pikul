grades_text = "10, 10, 11, 12, 9"

grades_list = grades_text.split(", ")
grades = [int(grade) for grade in grades_list]

average_grade = sum(grades) / len(grades)
print(f"Average grade: {average_grade:.2f}")

print("max grade:", max(grades))
print("min grade:", min(grades))

print("|".join(grades_list))

subjects_text = "Programing, Databases, English, IT Law, Ukrainian Language for Professional Purposes"
subjects = subjects_text.split(", ")

print(f"{'Number':<7}{'Subjects':<45}{'Grade':>5}")
for i in range(len(subjects)):
    print(f"{i + 1:<7}{subjects[i]:<45}{grades[i]:>5}") 

longest_subject = max(subjects, key=len)
print("Longest subject:", longest_subject)
print("Characters in longest subject:", len(longest_subject))