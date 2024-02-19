# Functions for Calc Fine
def calculate_fine(speed_over_limit1):
    if speed_over_limit1 < 10:
        return 30
    elif speed_over_limit1 < 15:
        return 80
    elif speed_over_limit1 < 20:
        return 120
    elif speed_over_limit1 < 25:
        return 170
    elif speed_over_limit1 < 30:
        return 230
    elif speed_over_limit1 < 35:
        return 300
    elif speed_over_limit1 < 40:
        return 400
    elif speed_over_limit1 < 45:
        return 510
    else:
        return 630


speeders = []  # List to store fines

# Main Routine
while True:
    name = input("Enter the speeder's name (type 'end' to finish input): ")
    if name.lower() == 'end':
        break
    speed_over_limit = int(input("Enter the speed over the limit in km/h: "))
    fine = calculate_fine(speed_over_limit)
    print("Fine for {} is ${}".format(name, fine))

    speeders.append(fine)

# Display summary
print("\nSummary of the day:")
total_fines = 0
for fine in speeders:
    total_fines += fine
print("Total fines collected today: ${}".format(total_fines))
