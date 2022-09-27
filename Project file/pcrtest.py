import csv
def pcr_test():
    add=open("pcrtest.csv","a",newline="")
    w=csv.writer(add,delimiter=",")
    L=[]
    p_fname = input("Enter the First Name of the Patient:")
    p_lname = input("Enter the Last Name of the Patient:")
    age = int(input("Enter the Age of the Patient:"))
    gender = input("Enter the Gender of the Patient:")
    p_phoneno = int(input("Enter the Patient's Phone Number:"))
    email = input("Enter the Patient's Email:")
    test_time=input("Enter the time of test:")

    new_patients=[p_fname,p_lname,age,gender,p_phoneno,email,test_time]
    L.append(new_patients)

    for i in L:
        w.writerow(i)
    add.close()
