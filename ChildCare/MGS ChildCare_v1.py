choice = 0

Child_Care_Kids = []


def drop_off():
    child_name = input(print("Enter Your Child's Name: "))
    amount_of_hours_in_daycare = int(input(print("How Many Hours Do You Want Your Child In Day Care For?: ")))
    yes_or_no = input(print(f"Your Child's Names Is {child_name} and they "
                            f"will \n"
                            f" be in childcare for "
                            f"{amount_of_hours_in_daycare} Hour \n"
                            f"You Will Have To Pay "
                            f"{amount_of_hours_in_daycare * 12} Dollars\n"
                            f" For Your Child To be In ChildCare Today Y Or "
                            f"N?: "))
    if yes_or_no.upper() == "Y":
        Child_Care_Kids.append(child_name)
        print("Thanks")
    else:
        print("No Problemo")
    choice = 0


while choice == 0:
        print("-----------------------------------------------------------------------")
        print("Welcome to MGS Childcare")
        print("What would you like to do? Please choose one of the items below")
        print("-----------------------------------------------------------------------")
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


        elif choice == 2:
            pickUp()

        elif choice == 3:
            calcCost()

        elif choice == 4:
            printRoll()

        else:
            print("Goodbye")
