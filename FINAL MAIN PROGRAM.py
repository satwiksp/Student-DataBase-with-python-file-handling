import csv
student = ['Roll', 'Name', 'Age','Attendance','Phone','Marks']
database= 'database.csv'
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                                                                              WELCOME TO STUDENT DATABASE")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def add_student():
    print("----------------------------------")
    print("Add Student Information")
    print("----------------------------------")
    global student
    global database

    student_data = []
    for field in student:
        if field=="Attendance":
            value = input("Enter attendance of last 30days : ")
        else:
            value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(database, "a",newline='') as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return


def view_students():
    global student
    global database

    print("                                                                 ---STUDENT RECORDS---")

    with open(database, "r") as f:
        reader = csv.reader(f)
        print("\n-----------------------------------------------------------------------------------------------------------------------------------------------")
        for x in student:
            #to adjust gap between header elements
            if x=="Roll":
                print(x, end='\t   ')
            if x=="Name":
                print(x, end='\t      ')
            if x=="Age":
                print(x, end='\t   ')
            if x=="Attendance":
                print(x, end='\t     ')
            if x=="Phone":
                print(x, end='\t                         ')
            if x=="Marks":
                print(x, end='\t                                     ')
        print("\n-----------------------------------------------------------------------------------------------------------------------------------------------")
#to adjust gaps in records
        for row in reader:
            for item in row:
                if item==row[0]:
                    print(item, end="	  ")
                if item==row[1]:
                    print(item, end="	       ")
                if item==row[2]:
                    print(item, end="	    ")
                if item==row[3]:
                    print("      ",item, end="	                   ")
                if item==row[4]:
                    print(item, end="	            ")
                if item==row[5]:
                    print(item, end="	                ")
            print("\n")

    input("Press any key to continue")


def search_student():
    global student
    global database

    print("--- Search Student ---")
    roll = input("Enter roll no. to search: ")
    with open(database, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    print("----- Student Found -----")
                    print("Roll: ", row[0])
                    print("Name: ", row[1])
                    print("Age: ", row[2])
                    print("Attendance: ", row[3])
                    print("Phone: ", row[4])
                    print("Score: ", row[5])
                    break
        else:
            print("Roll No. not found in our database")
    input("Press any key to continue")

def atper():
    global student
    global database
    stuperat=[]
    with open(database, "r")as f:
        reader2 = csv.reader(f)
        for row in reader2:
            if len(row) > 0:
                if 22.5<= float(row[3]):
                    stuperat.append(row[1])
        print()
        print("Students with attendance above 75% are")
        print(stuperat)

def clsavg():
    global student
    global database
    av=0
    avp=0
    count=0
    with open(database, "r")as f:
        reader3 = csv.reader(f)
        for row in reader3:
            if len(row) > 0:
                count+=1
                for num in row:
                    if num==row[5]:
                        av=av+float(num)
    avp=(av/count)
    print()
    print("The class average is",avp)
        
    
def update_student():
    global student
    global database

    print("--- Update Student ---")
    roll = input("Enter roll no. to update: ")
    index_student = None
    updated_data = []
    with open(database, "r") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for field in student:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1


    # Check if the record is found or not
    if index_student is not None:
        with open(database, "w") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Roll no. ", roll, "updated successfully")
    else:
        print("Roll No. not found in our database")

    input("Press any key to continue")


def delete_student():
    global student
    global database

    print("--- Delete Student ---")
    roll = input("Enter roll no. to delete: ")
    student_found = False
    updated_data = []
    with open(database, "r") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(database, "w") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Roll no. ", roll, "deleted successfully")
    else:
        print("Roll No. not found in our database")

    input("Press any key to continue")

while True:
    print()
    print("______________________________________________________________________________________________________________________________________")
    print()
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Students with 75% attendance")
    print("7. Class average")
    print("6. Quit")

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice=='6':
        atper()
    elif choice=='7':
        clsavg()
    else:
        break

print("---------------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                                               THANK YOU")
print("---------------------------------------------------------------------------------------------------------------------------------------------------")
