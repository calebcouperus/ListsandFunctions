def record_absences():
    absences = []
    while True:
        name = input("Enter employee name (or $ to end): ")
        if name == '$':
            break
        days_absent = int(input("Enter number of days absent: "))
        absences.append((name, days_absent))
    return absences


def calculate_average(absences):
    total_days = sum(days for _, days in absences)
    return total_days / max(len(absences), 1)  # Prevent division by zero


def main():
    print("Enter employee names and days absent. Enter $ to end.")
    absences = record_absences()

    if not absences:
        print("No data entered.")
        return

    average = calculate_average(absences)
    print("Average number of days absent per year:", average)

    most_absent = max(absences, key=lambda x: x[1], default=("None", 0))
    print("Employee with most days absent:", most_absent[0])

    never_absent = [name for name, days in absences if days == 0]
    if never_absent:
        print("Employees who were never absent:", never_absent)
    else:
        print("All employees had absences.")

    above_average = [(name, days) for name, days in absences if days > average]
    if above_average:
        print("Employees with absences above average:")
        for name, days in above_average:
            print(name, "-", days, "days")
    else:
        print("No employees with absences above average.")


if __name__ == "__main__":
    main()
