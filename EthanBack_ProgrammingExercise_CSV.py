import csv

def record_scores():
    # Prompt the user for number of students to record
    num_students = int(input("\nHow many students would you like to record for? "))

    # Open CSV file in write mode and create writer object
    with open("student_grades.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header row
        writer.writerow(["first name", "last name", "Exam 1", "Exam 2", "Exam 3"])

        # Loop through each student and get their information
        for i in range(num_students):
            first_name = input("\nFirst name: ")
            last_name = input("Last name: ")
            exam_1 = int(input("Exam 1: "))
            exam_2 = int(input("Exam 2: "))
            exam_3 = int(input("Exam 3: "))

            # Write student row to CSV
            writer.writerow([first_name, last_name, exam_1, exam_2, exam_3])
        print("\nStudent information recorded to student_grades.csv")

def read_scores():

    with open("student_grades.csv", mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)


    header = rows[0]
    # This cycles though printing every given element within a list on the csv file
    print(f"{header[0]:<15} {header[1]:<15} {header[2]:<8} {header[3]:<8} {header[4]:<8}")
    #This just prints a separation line made of dashes
    print("-" * 60)

    for student in rows[1:]:
        print(f"{student[0]:<15} {student[1]:<15} {student[2]:<8} {student[3]:<8} {student[4]:<8}")

def main():
    #This is just a mini menu that prompts the user for what they want to use
    while True:
        print("Press 1 to record student grades")
        print("Press 2 to read scores")
        print("Press 3 to exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            record_scores()
        elif choice == "2":
            read_scores()
        elif choice == "3":
            break

if __name__ == '__main__':
    main()