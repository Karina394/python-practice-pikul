schedule = {
    "Mon": [
        "OS and Computer Networks Administration",
        "Programming",
        "Ukrainian Language for Professional Purposes"
    ],
    "Tue": [
        "Databases in Information Systems",
        "Programming",
        "IT Law"
    ],
    "Wed": [
        "Web Resource Development",
        "Foreign Language for Professional Purposes",
        "Databases in Information Systems"
    ],
    "Thu": [
        "OS and Computer Networks Administration",
        "Programming",
        "Web Resource Development"
    ],
    "Fri": [
        "IT Law",
        "Foreign Language for Professional Purposes",
        "Databases in Information Systems"
    ]
}

print("Day | Number of classes | Subjects")

for day, subjects in schedule.items():
    print(day, "|", len(subjects), "|", ", ".join(subjects))

total_classes = sum(len(subjects) for subjects in schedule.values())
print("\nTotal classes:", total_classes)

max_day = max(schedule, key=lambda day: len(schedule[day]))
print("Day with the most classes:", max_day)

all_subjects = set()

for subjects in schedule.values():
    all_subjects.update(subjects)

print("\nAll different subjects:")
print(all_subjects)
print("Number of different subjects:", len(all_subjects))

monday = set(schedule["Mon"])
wednesday = set(schedule["Wed"])

print("\nSubjects on Monday and Wednesday:")
print(monday & wednesday)

print("Subjects on Monday but not Wednesday:")
print(monday - wednesday)

def count_subjects(schedule):
    counts = {}

    for subjects in schedule.values():
        for subject in subjects:
            counts[subject] = counts.get(subject, 0) + 1

    return counts


subject_counts = count_subjects(schedule)

print("\nSubject -> number of classes:")
for subject, count in subject_counts.items():
    print(subject, "->", count)

rating = sorted(
    subject_counts.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\nSubject rating:")

for number, (subject, count) in enumerate(rating, start=1):
    print(f"{number}. {subject} - {count}")