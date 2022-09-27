import csv
def patient_list():
    a=open("patient.csv","w",newline="")
    r = csv.writer(a, delimiter=",")
    L=[["101","Suresh","Khan","18","Male","0501891414","Headache","Stable","Dr.Ramesh Kumar","9:30-10:30"],
       ["102","Abhinav","AnilKumar","17","Male","0566376561","Eye Check-up","Stable","Dr.Lilly Mayson","11:00-11:30"],
       ["103","Arav","Krishna","21","Male","0548952648","Mental Issue","Stable","Dr.Smriti Singh","15:30-16:00"],
       ["104","Swathi","Ramachandran","31","Female","0506876248","Menopause","Stable","Dr.Natasha Lyonne","16:30-17:00"],
       ["105","Nuza","Ahmed","26","Female","0557694681","Skin Infection","Stable","Dr.Stephen Fleming","12-12:30"],
       ["106","Aditya","Reddy","26","Male","0509892678","Body Check-up","Stable","Dr.Kane Willson","14:00-14:30"],
       ["107","Ahmed","Abbasi","39","Male","0548926526","Diabetes","Stable","Dr.Jimmy Parker","10:00-10:30"],
       ["108","Jahnvi","Singh","45","Female","0569735481","Car Accident","Unstable","Dr.Ellyse Perry","Emergency"],
       ["109","Isabelle","Joy","10","Female","0567395486","Fever","Stable","Dr.Sneha Gupta","17:00-17:30"],
       ["110","Ayush","Balaji","55","Male","0506974201","Heart Attack","Unstable","Dr.Scott Bond","Emergency"]]


    for i in L:
        r.writerow(i)
    a.close()

def display_by_name():
    a=open("patient.csv","r")
    r=csv.reader(a)
    name=input("Enter patient first name: ")
    flag=0
    for i in r:
        if i[1]==name:
            print("Patient ID : ",i[0])
            print("First Name : ",i[1])
            print("Last Name  : ",i[2])
            print("Age : ",i[3])
            print("Gender : ",i[4])
            print("Phone number : ",i[5])
            print("Disease suffering from : ",i[6])
            print("Condition (Critical/Stable) : ",i[7])
            print("Doctor's name : ",i[8])
            print("Time of appointment: ",i[9])
            flag=1
            print()
    if flag!=1:
        print("Patient not found")
        print()
    a.close()

def display_by_age():
    a=open("patient.csv","r")
    r=csv.reader(a)
    age=input("Enter patient age: ")
    flag=0
    for i in r:
        if i[3]==age:
            print("Patient ID : ",i[0])
            print("First Name : ",i[1])
            print("Last Name  : ",i[2])
            print("Age : ",i[3])
            print("Gender : ",i[4])
            print("Phone number : ",i[5])
            print("Disease suffering from : ",i[6])
            print("Condition (Critical/Stable) : ",i[7])
            print("Doctor's name : ",i[8])
            print("Time of appointment: ",i[9])
            flag=1
            print()
    if flag!=1:
        print("Patient not found")
        print()
    a.close()

def display_by_timing():
    a=open("patient.csv","r")
    r=csv.reader(a)
    time=input("Enter patient appointment time: ")
    flag=0
    for i in r:
        if i[9]==time:
            print("Patient ID : ",i[0])
            print("First Name : ",i[1])
            print("Last Name  : ",i[2])
            print("Age : ",i[3])
            print("Gender : ",i[4])
            print("Phone number : ",i[5])
            print("Disease suffering from : ",i[6])
            print("Condition (Critical/Stable) : ",i[7])
            print("Doctor's name : ",i[8])
            print("Time of appointment: ",i[9])
            flag=1
            print()
    if flag!=1:
        print("Patient not found")
        print()
    a.close()

def add_patient():
    add=open("patient.csv","a",newline="")
    w=csv.writer(add,delimiter=",")
    L=[]
    p_no=int(input("Patient NO:"))
    p_fname=input("Enter the First Name of the Patient:")
    p_lname=input("Enter the Last Name of the Patient:")
    age=int(input("Enter the Age of the Patient:"))
    gender=input("Enter the Gender of the Patient:")
    p_phoneno=int(input("Enter the Patient's Phone no:"))
    problem=input("Enter the the Disease/Disorder of the Patient:")
    condition=input("Enter the Stability of the Patients:")
    D_name=input("Enter the Name of the Doctor:")
    visiting_time=input("Enter the visiting hours:")


    new_patient=[p_no,p_fname,p_lname,age,gender,p_phoneno,problem,condition,D_name,visiting_time]
    L.append(new_patient)

    for i in L:
        w.writerow(i)
    add.close()

def rem_patient():
    rem=open("patient.csv","r")
    r=csv.reader(rem)
    flag=0
    new_plist=[]
    p_fname=input("Enter the First Name of the Patient to be deleted:")
    p_lname=input("Enter the Last Name of the Patient to be deleted:")
    for i in r:
        if i[1]!=p_fname and i[2]!=p_lname:
            new_plist.append(i)
        else:
            flag=1
    if flag==0:
        print("Patient not found.")
    else:
        rem=open("patient.csv","w",newline="")
        w=csv.writer(rem)
        w.writerows(new_plist)
        rem.close()
        print("Patient has been REMOVED.")
