# Timetable Helper

Timetable Helper is a simple Python script that generates a weekly timetable for your subjects with built‑in self‑study slots. It asks for your subject names and automatically distributes them from Monday to Saturday, keeping Sunday free from classes and reserved for self‑study.

## Features

- Takes any number of subjects as input from the user.
- Automatically distributes subjects across the week using a simple rotation.
- Separate logic for:
  - Monday and Friday: 3 morning class slots + 1 afternoon self‑study slot.
  - Tuesday, Wednesday, Thursday, Saturday: 2 morning class slots + 1 self‑study slot.
  - Sunday: no classes, only self‑study.
- Prints a clean, readable weekly timetable in the terminal.

## How It Works

1. The program asks:
   - “How many subjects do you have?”
   - Then reads that many subject names into a list.
2. It defines:
   - Days of the week: `["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]`
   - Time slots:
     - For Mon & Fri: `["8:30AM", "10:05AM", "11:35AM"]` (all used as class slots)
     - For Tue, Wed, Thu, Sat: `["8:30AM", "10:05AM", "11:35AM"]` (first two for classes, last for self study)
3. It loops through each day:
   - For Monday and Friday:
     - Assigns subjects to all three morning slots using a rotating index (`index % n`).
     - Adds a fixed self‑study slot at `1:15PM`.
   - For Tuesday, Wednesday, Thursday, Saturday:
     - Assigns two class slots (`8:30AM`, `10:05AM`) to subjects using rotation.
     - Sets `11:35AM` as a self‑study slot.
   - For Sunday:
     - No class times, only a “Self Study – No Classes” entry.
4. Finally, it prints the timetable day by day.

## Sample Output

Example for 3 subjects: `Math`, `Physics`, `English`:

