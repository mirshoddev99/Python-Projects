def add(student_info):
    choose = int(
        input("""\n
        .....Menu.....
        1.Bachelor
        2.Master
        Choose the Degree.... ->  """)
    )
    if choose == 1:
        count_student = int(input("\nHow many students do you want to add:  "))
        print("Enter the following info for adding bachelor student...")
        for i in range(count_student):
            talaba = dict()
            flag = True
            cnt = 0
            while flag:
                talaba["id"] = input("\nEnter your Student ID: ")
                for dictt in student_info:
                    if dictt["id"] == talaba["id"]:
                        print("This ID number is already exists. Try to enter a different ID!")
                        break
                    else:
                        cnt += 1
                if cnt == len(student_info):
                    flag = False

            talaba["full_name"] = input("Enter your Full Name: ")
            talaba["nationality"] = input("Enter your Nationality: ")
            talaba["gender"] = input("Enter your Gender: ")
            talaba["faculty"] = input("Enter your Faculty: ")
            talaba["admission_year"] = input("Enter your Admission_year: ")
            talaba["residential_hall"] = input("Enter your Residential Hall: ")
            student_info.append(talaba)
        print(f"Added {count_student} student to the system.\n")

    if choose == 2:
        count_student = int(input("\nHow many students do you want to add:  "))
        print("Enter the following info for adding master student...")
        for i in range(count_student):
            talaba = dict()
            flag = True
            cnt = 0
            while flag:
                talaba["id"] = input("\nEnter your Student ID: ")
                for dictt in student_info:
                    if dictt["id"] == talaba["id"]:
                        print("This ID number is already exists. Try to enter a different ID!")
                        break
                    else:
                        cnt += 1
                if cnt == len(student_info):
                    flag = False

            talaba["full_name"] = input("Enter your Full Name: ")
            talaba["nationality"] = input("Enter your Nationality: ")
            talaba["gender"] = input("Enter your Gender: ")
            talaba["faculty"] = input("Enter your Faculty: ")
            talaba["admission_year"] = input("Enter your Admission year: ")
            talaba["residential_hall"] = input("Enter your Residential Hall: ")
            talaba["supervisor_name"] = input("Enter your Supervisor Name: ")
            talaba["research_topic"] = input("Enter your Research Topic: ")
            student_info.append(talaba)
        print(f"Added {count_student} students to the system.\n")


def remove(student_info):
    if student_info:
        flag = True
        while flag:
            st_id = input("\nEnter the ID number of the Student you want to delete: ")
            for index, item in enumerate(student_info):
                if item['id'] == st_id:
                    student_info.pop(index)
                    print("The student has been deleted from the system\n")
                    flag = False

            if flag:
                print("Wrong ID number!\n")

    else:
        print("\nThere is no student yet!\n")


def find(student_info):
    if student_info:
        std_id = input("\nEnter the ID number of the Student you want to find: ")
        for k in range(len(student_info)):
            if std_id == student_info[k]["id"]:
                print(f"\nThe student that you are looking for\n")
                if "supervisor_name" in student_info[k]:
                    print(
                        f"Student ID: {student_info[k]['id']}\n"
                        f"Full Name: {student_info[k]['full_name']}\n"
                        f"Nationality: {student_info[k]['nationality']}\n"
                        f"Gender: {student_info[k]['gender']}\n"
                        f"Faculty: {student_info[k]['faculty']}\n"
                        f"Admission year: {student_info[k]['admission_year']}\n"
                        f"Residential Hall: {student_info[k]['residential_hall']}\n"
                        f"SuperVisor Name: {student_info[k]['supervisor_name']}\n"
                        f"Research Topic: {student_info[k]['research_topic']}"
                    )
                    break
                else:
                    print(
                        f"Student ID: {student_info[k]['id']}\n"
                        f"Full Name: {student_info[k]['full_name']}\n"
                        f"Nationality: {student_info[k]['nationality']}\n"
                        f"Gender: {student_info[k]['gender']}\n"
                        f"Faculty: {student_info[k]['faculty']}\n"
                        f"Admission year: {student_info[k]['admission_year']}\n"
                        f"Residential Hall: {student_info[k]['residential_hall']}\n"
                    )
                    break
            elif std_id != student_info[k]["id"]:
                print("Wrong ID number!\n")
    else:
        print("\nThere is no student yet!\n")


def display_all(student_info):
    if student_info:
        print("\n...All information of the students...\n")
        for k in range(len(student_info)):
            if "supervisor_name" in student_info[k]:
                print(
                    f"Student ID: {student_info[k]['id']}\n"
                    f"Full Name: {student_info[k]['full_name']}\n"
                    f"Nationality: {student_info[k]['nationality']}\n"
                    f"Gender: {student_info[k]['gender']}\n"
                    f"Faculty: {student_info[k]['faculty']}\n"
                    f"Admission year: {student_info[k]['admission_year']}\n"
                    f"Residential Hall: {student_info[k]['residential_hall']}\n"
                    f"SuperVisor Name: {student_info[k]['supervisor_name']}\n"
                    f"Research Topic: {student_info[k]['research_topic']}\n"
                )
            else:
                print(
                    f"Student ID: {student_info[k]['id']}\n"
                    f"Full Name: {student_info[k]['full_name']}\n"
                    f"Nationality: {student_info[k]['nationality']}\n"
                    f"Gender: {student_info[k]['gender']}\n"
                    f"Faculty: {student_info[k]['faculty']}\n"
                    f"Admission year: {student_info[k]['admission_year']}\n"
                    f"Residential Hall: {student_info[k]['residential_hall']}\n"
                )
    else:
        print("\nThere is no student yet!\n")


def update(student_info):
    if student_info:
        idx = 0
        flag = True
        while idx != len(student_info):
            st_id = input("\nEnter the ID number of the Student you want to update (him\her) information: ")
            if student_info[idx]["id"] == st_id:
                while flag:
                    ask = input("\nwhich one do you want to update (him\her) info: ").lower()
                    if student_info[idx][ask]:
                        new_info = input("Enter new info you want to update: ")
                        student_info[idx][ask] = new_info
                        print(f"The student {ask} was updated successfully!\n")
                        flag = False
                    else:
                        print("KeyError. Try to again!\n")
                        continue
                break
            else:
                idx += 1
                print("Wrong ID number!\n")

    else:
        print("\nThere is no student yet!\n")


