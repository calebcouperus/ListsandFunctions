# Children list
Children_list = []


# Function for drop-off
def drop_off():
    child_name = input("Please enter your child's name: ")
    Children_list.append(child_name)
    print('Your child has been added to the roll')


# Function for Pick-up
def pick_up():
    child_name = input("Please enter your child's name: ")
    Children_list.remove(child_name)
    print('Your child has been signed out of the roll')


# Function to Print Roll
def print_roll():
    print(Children_list)


# Function to Calculate cost
def calc_cost():
    hours = input('Enter how many hours your child is in for: ')
    print(f'Cost: ${hours * 12}')


# Main Routine
choice = 0

print("-----------------------------------------------------------------------")
print("Welcome to MGS Childcare")
print("What would you like to do? Please choose one of the items below")
print("-----------------------------------------------------------------------")

while choice == 0:
    print()
    print("1 Drop off a child")
    print("2 Pick up a child")
    print("3 Calculate cost")
    print("4 Print roll")
    print("5 Exit the system")
    print()
    choice = int(input("Enter your choice (number between 1 and 5): \n"
                       ">>> "))
    print()

    if choice == 1:
        drop_off()
        choice = 0

    elif choice == 2:
        pick_up()
        choice = 0

    elif choice == 3:
        calc_cost()
        choice = 0

    elif choice == 4:
        print_roll()
        choice = 0

    else:
        print("Goodbye")
