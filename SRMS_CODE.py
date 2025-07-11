def add_student(student_record):
    print("-----------------Add Student-----------------------------------")
    name = input("enter student name:")
    roll_no = input("enter student roll_no:")
    marks = int(input("enter student's marks (out of 100):"))

    percentage = (marks/100)*100
    if percentage >= 33:
        status = 'pass'
    else:
        status = 'fail'

    student = {
        "name":name,
        "roll_no":roll_no,
        "marks":marks,
        "percentage":percentage,
        "status":status }
    student_record.append(student)
    print()
    print("!!!!!!!!!! successfully added ✅ Have a nice day!!!!!!!!!!! ")
#-----------------------------------------------------------------------------------------------------------------------
def view_all_student(student_record):
    """ This shows every student in the list"""
    if not student_record:
         print("there is no student record yet.")
         return
    print("\n All Students Record")
    print("------------------------------------------------------------------------------------------------------------")
# display records with the help of loop
    for stu in student_record:
        print(f"name:{stu['name']}|"
              f"roll_no:{stu['roll_no']}|"
              f"marks:{stu['marks']}\t|"
              f"percentage:{stu['percentage']:.2f}|"
              f"status:{stu['status']}")
        print("........................................................................................................")


#----------------------------------------------------------------------------------------------------------------------
# the main menu of srms
def display_menu():
    print("=============================={ STUDENT RESULT MANAGEMENT SYSTEM }=========================================")
    print("  1.Add Student\t\t")
    print("  2.View All Student\t\t")
    print("  3.Exit")
    print("===========================================================================================================")
display_menu()
#----------------------------------------------------------------------------------------------------------------------
#main function for user choice:
def main():
    student_record = [] # a list to store all the records of the students.

    while True:
        print("\nMENU:\t1.Add Student\t 2.View All Student\t\t 3.Exit:")
        print("--------------------------------------------------------------------------------------------------------")
        choice = input("enter your choice --> 1/2/3 : ")
        if choice == "1":
            add_student(student_record)
        elif choice == "2":
            view_all_student(student_record)
        elif choice == "3":
            print("exiting.....👋 , Have a nice day!")
            break
        else:
            print("Invalid choice")
# call main function to run , use __name__ buildin function to Ensures  program starts from main()
if __name__ == "__main__":
    main()






