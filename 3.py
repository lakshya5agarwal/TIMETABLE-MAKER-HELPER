print("=== Timetable Helper ===")

# How many subjects?
n = int(input("How many subjects do you have? "))

# Take subject names
subjects = []
for i in range(n):
    subjects.append(input(f"Enter subject #{i+1} name: "))

# Days of week
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Time slots
two_slots = ["8:30AM", "10:05AM", "11:35AM"]       # for Tue, Wed, Thu, Sat (2 classes + 1 self study)
three_slots = ["8:30AM", "10:05AM", "11:35AM"]     # for Mon & Fri (3 classes)
self_study_label = "Self Study"

timetable = {}
index = 0

for day in days:
    timetable[day] = []

    if day == "Sun":
        # No classes on Sunday
        timetable[day].append(("Self Study", "No Classes"))
        continue

    # Monday and Friday "8:30AM", "10:05AM"
    if day in ["Mon", "Fri"]:
        for slot in three_slots:
            timetable[day].append((slot, subjects[index % n]))
            index += 1
        # Add self study at end
        timetable[day].append(("1:15PM", self_study_label))
    
    else:
        # Other days → 2 classes + 1 self study
        timetable[day].append((two_slots[0], subjects[index % n]))
        index += 1

        timetable[day].append((two_slots[1], subjects[index % n]))
        index += 1

        timetable[day].append((two_slots[2], self_study_label))

# Print timetable
print("\n===== WEEKLY TIMETABLE =====\n")
for day in days:
    print(day + ":")
    for time, sub in timetable[day]:
        print(f"  {time} - {sub}")
    print()