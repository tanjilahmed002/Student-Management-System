from functions import add_student,view_student,search_student,update_student,delete_student,calculate_student_result,find_top_student

while True:
    print("=====Student Management System=====")
    print("1.Add Student")
    print("2.View Student")
    print("3.search Student")
    print("4.Update Student")
    print("5.Delete Student")
    print("6.Calculate student result")
    print("7.Find Top Student")
    print("8.Exit")
    choice=input("enter your choice and type 8 for exit the loop :")
    if choice=="1":
        add_student()
        print("add")
    elif choice=="2":
        view_student()
        print("view")
    elif choice=="3":
        search_student()
        print("search")
    elif choice=="4":
        update_student()
        print("update")
    elif choice=="5":
        delete_student()
        print("delete")
    elif choice=="6":
        calculate_student_result()
        print("calculate")
    elif choice=="7":
        find_top_student()
        print("find top student")
    elif choice=="8":
        print("exit")
        break
    else:
        print("invalid choice")