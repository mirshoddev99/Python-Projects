students = []

class Student():
    def __init__(self, student_id, full_name, nationality, gender, faculty, admission_year):
        self.student_id = student_id
        self.full_name = full_name
        self.nationality = nationality
        self.gender = gender
        self.faculty = faculty
        self.admission_year = admission_year
    
    def __del__(self):
        return self.student_id
    
    def __str__(self):
        return str(self.student_id)
    
    

class Undergraduate(Student):
    def __init__(self, student_id, full_name, nationality, gender, faculty, admission_year, residential_hall):
        super().__init__(student_id, full_name, nationality, gender, faculty, admission_year)
        self.residential_hall = residential_hall
    
    def show(self):
        return f"""
        Student ID: {self.student_id}
        Full Name: {self.full_name}
        Nationality: {self.nationality}
        Gender: {self.gender}
        Faculty: {self.faculty}
        Admission Year: {self.admission_year}
        Residential Hall: {self.residential_hall}"""

class Postgraduate(Student):
    def __init__(self, student_id, full_name, nationality, gender, faculty, admission_year, supervisor_name, research_topic):
        super().__init__(student_id, full_name, nationality, gender, faculty, admission_year)
        self.supervisor_name = supervisor_name
        self.research_topic = research_topic
    
    def show(self):
        return f"""
        Student ID: {self.student_id}
        Full Name: {self.full_name}
        Nationality: {self.nationality}
        Gender: {self.gender}
        Faculty: {self.faculty}
        Admission Year: {self.admission_year}
        Supervisor Name: {self.supervisor_name}
        Research Topic: {self.research_topic}"""

while True:
    choice = int(input("""
    Menu:
    1. Add
    2. Remove
    3. Find
    4. Display All
    5. Exit
    
    Enter a number... -> """))

    if choice == 1:
        choice = int(input("""
        Menu:
        1. Undergraduate
        2. Postgraduate

        Enter a number... -> """))
        if choice == 1:
            students.append(Undergraduate(input("student_id -> "), input("full_name -> "), input("nationality -> "), input("gender -> "), input("faculty -> "), input("admission_year -> "), input("residential_hall -> ")))
        elif choice == 2:
            students.append(Postgraduate(input("student_id -> "), input("full_name -> "), input("nationality -> "), input("gender -> "), input("faculty -> "), input("admission_year -> "), input("supervisor_name -> "), input("research_topic -> ")))
        else:
            print("wrong number")
        print("added")

    elif choice == 2:
        ids = str(input("Student ID -> "))
        dell = 0
        for i in students:
            if str(i) == ids:
                students.remove(i)
                dell+=1
        if dell:
            print("deleted")
        else:
            print("not")

    elif choice == 3:
        ids = str(input("Student ID -> "))
        for i in students:
            if str(i) == ids:
                print(i.show())
    elif choice == 4:
        for i in students:
            print(i.show()) 
                
    elif choice == 5:
        break