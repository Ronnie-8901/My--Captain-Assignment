import csv

def write_into_csv(info_list):
    with open("student_info.csv", "a", newline = "")as csv_file:
        writer =  csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact_No", "Email_ID"])

        writer.writerow(info_list)
if __name__ == "__main__":
    condition = True
    student_num = 1

    while(condition):
        student_info = input("Enter Stuedent Information of Student #{} in shown manner(Name Age Contact_No Email_ID):- ".format(student_num))

        print("Entered Information:- ",student_info)

        student_list = student_info.split(" ")

        print("Entered splitup Information :- ", student_list)

        print("\n Entered Student Information:-\n Name:-{}\n Age:- {}\n Contact_No:- {}\n Email_ID:- {}\n ".format(student_list[0],student_list[1],student_list[2],student_list[3]))

        check = input("Is the information is correct? (yes/no)")
        if check == "yes":
            write_into_csv(student_list)

            condition_check = input("Do you wannt to enter any other student information(yes/no)? ")
            if condition_check == "yes":
                condition = True
                student_num += 1
            elif condition_check == "no":
                condition = False
            else:
                condition = False
        elif check == "no":
            print("\n Re-enter the Value, Please!")
