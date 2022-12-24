from details import *


def pnu_system(student_info):
    print("\nWelcome to PNU student info system!!!")
    while True:
        choice = int(
            input(
                """
    .....Menu.....
        1. Add
        2. Remove
        3. Find
        4. Update
        5. Display All
        6. Exit
        Enter a number.... -> """
            )
        )

        # Add
        if choice == 1:
            add(student_info)


        # Remove
        elif choice == 2:
            remove(student_info)


        # Find
        elif choice == 3:
            find(student_info)


        # Update
        elif choice == 4:
            update(student_info)


        # Display All
        elif choice == 5:
            display_all(student_info)


        # Exit
        elif choice == 6:
            break
    print(f"\nYou have logged out!")


if __name__ == "__main__":
    student_info = list()
    pnu_system(student_info)
