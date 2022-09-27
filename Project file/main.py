import csv
from doctor import *
from patient import *
from blooddonation import *
from pcrtest import *
print("WELCOME TO HOSPITAL MANAGEMENT PROGRAM CODE")
print("-------------------------------------------")
print()
print()
print("This gives us an insight on how a hospital database code looks like")
print("Here we can store/update/modify details of doctors working and patients admitted in the hospital")
print("This code also allows the users to book an appointment for their doctor and also giving them vairious options helping them to choose there required doctor")
print("We also have a blood donation camp registration code which can be used by the users to book appointment for giving blood")
print("In the ongoing times there is an increasing need of PCR test. Our code enables users to book an appointment for PCR test")
print()
print()
print("Lets get started!")
print()
print()
Doctor_List()
patient_list()
while True:
    print("Choose options to explore")
    print("1)Doctor")
    print("2)Patient")
    print("3)Blood Donation Camp")
    print("4)PCR test ")
    print("5)Exit")
    option=int(input("Enter option number: "))
    if option==1: 
        while True:
            print("1)Display doctor's schedule")
            print("2)Searching doctor's")
            print("3)Updating doctor's details")
            print("4)Add/remove doctor")
            print("5)Exit")
            option=int(input("Enter option number: "))
            if option==1:
                print("DISPLAYING DOCTORS SCHEDULE!")
                print("To display schedule you can select doctor by the following methods:-")
                print("1)Search doctor by name")
                print("2)Search doctors by availability")
                print("3)Search doctors by speciality")
                print("4)Exit")
                option=int(input("Enter option number: "))
                if option==1:
                    display_schedule_by_name()
                elif option==2:
                    display_schedule_by_availability()
                elif option==3:
                    display_schedule_by_speciality()
                elif option==4:
                    break
                else:
                    print("Enter valid option number")
            elif option==2:
                print("SEARCHING DOCTORS!")
                print("Search doctor by the following methods:-")
                print("1)Search doctor by name")
                print("2)Search doctor by hospital ID")
                print("3)Search doctors by availability")
                print("4)Search doctors by speciality")
                print("5)Search doctors by price per appointment")
                print("6)Exit")
                option=int(input("Enter option number: "))
                if option==1:
                    search_by_name()
                elif option==2:
                    search_by_ID()
                elif option==3:
                    search_by_availability()
                elif option==4:
                    search_by_speciality()
                elif option==5:
                    search_by_price_per_appointment()
                elif option==6:
                    break
                else:
                    print("Enter valid option number")
            elif option==3:
                print("UPDATING DOCTORS DETAILS!")
                print("Choose which detail you would like to update:-")
                print("1)Schedule")
                print("2)Availability")
                print("3)Salary")
                print("4)Price per appointment")
                print("5)Exit")
                option=int(input("Enter option number: "))
                if option==1:
                    update_detail_schedule()
                elif option==2:
                    update_detail_availability()
                elif option==3:
                    update_detail_salary()
                elif option==4:
                    update_detail_price_per_appointment()
                elif option==5:
                    break
                else:
                    print("Enter valid option number")
            elif option==4:
                print("ADDING/REMOVING A DOCTOR!")
                print("Choose from the following options to add or remove a doctor:-")
                print("1)Add a doctor")
                print("2)Remove a doctor")
                print("3)Exit")
                option=int(input("Enter option number: "))
                if option==1:
                    add_doctor()
                elif option==2:
                    remove_doctor()
                elif option==3:
                    break
                else:
                    print("Enter valid option number")
            elif option==5:
                break
            else:
                print("Enter valid option number")
    if option==2:
        while True:
            print("1)Display patient detail")
            print("2)Add patient")
            print("3)Remove patient")
            print("4)Exit")
            option=int(input("Enter option number: "))
            if option==1:
                print("DISPLAY PATIENT DETAILS!")
                print("To display patient details select patient based on the following:")
                print("1)Enter name of patient")
                print("2)Enter age of patient")
                print("3)Enter time of appointment")
                option=int(input("Enter option number:"))
                if option==1:
                    display_by_name()
                elif option==2:
                    display_by_age()
                elif option==3:
                    display_by_timing()
                elif option==4:
                    break
                else:
                    print("Enter valid option number")
            elif option==2:
                add_patient()
            elif option==3:
                rem_patient()
            elif option==4:
                break
            else:
                print("Enter valid option number")
    if option==3:
        while True:
            print("1)Book slot for blood donation")
            print("2)Exit")
            option=int(input("Enter option number: "))
            if option==1:
                donors()
                print("Your appointment has been booked")
                print("Please check your email for further details")
                print("THANK YOU!")
            elif option==2:
                break
            else:
                print("Enter valid option number")
    if option==4:
        while True:
            print("1)Book slot for PCR test")
            print("2)Exit")
            option=int(input("Enter option number: "))
            if option==1:
                pcr_test()
                print("Your appointment has been booked")
                print("Please check your email for further details")
                print("THANK YOU!")
            elif option==2:
                break
            else:
                print("Enter valid option number")
    if option==5:
        print("THANK YOU!")
        break
    else:
        print("Enter valid option number")
