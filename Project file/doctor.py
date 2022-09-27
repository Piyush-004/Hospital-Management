import csv

def Doctor_List():
    a=open("doctor.csv","w",newline="")
    r=csv.writer(a,delimiter=",")
    L=[["10234","Dr.Ramesh Kumar",34,"Male","Available","General","Booked","Booked","Free","Booked","Free","Free","Free","Booked","Free","Booked","Free","Booked","Booked","Free","Free",
        150,11,45000],
       ["10235","Dr.Tom Billy",28,"Male","Available","Surgeon","Free","Free","Free","Booked","Booked","Booked","Free","Free","Free","Booked","Booked","Free","Free","Booked","Booked",
        250,7,55000],
       ["10236","Dr.Sneha Gupta",31,"Female","Available","Pediatrician","Free","Free","Booked","Booked","Booked","Free","Free","Booked","Free","Booked","Free","Free","Booked","Booked","Booked",
        100,4,30000],
       ["10237","Dr.Rajeev Mehra",43,"Male","Available","Orthodontist","Free","Free","Free","Free","Booked","Free","Free","Booked","Booked","Free","Free","Free","Booked","Booked","Free",
        125,10,35000],
       ["10238","Dr.Stephen Fleming",48,"Male","Available","Dermatologists","Free","Booked","Booked","Free","Free","Free","Booked","Free","Free","Booked","Free","Booked","Free","Free","Free",
        145,15,40000],
       ["10239","Dr.Lilly Mayson",26,"Female","Available","Ophthalmologists","Free","Booked","Free","Free","Free","Free","Free","Booked","Booked","Free","Booked","Booked","Booked","Free","Booked",
        100,3,30000],
       ["10240","Dr.Natasha Lyonne",34,"Female","Available","Gynecologists","Free","Free","Booked","Free","Booked","Booked","Booked","Free","Free","Free","Free","Free","Booked","Free","Booked",
        175,5,50000],
       ["10241","Dr.Scott Bond",38,"Male","Available","Cardiologists","Booked","Booked","Booked","Free","Free","Free","Booked","Booked","Free","Free","Free","Free","Booked","Booked","Booked",
        100,8,38000],
       ["10242","Dr.Ellyse Perry",30,"Female","Available","Surgeon","Free","Free","Booked","Free","Booked","Booked","Free","Free","Booked","Booked","Free","Booked","Booked","Free","Free",
        250,1,55000],
       ["10243","Dr.Jimmy Parker",32,"Male","Available","Endocrinologists","Free","Free","Free","Booked","Booked","Free","Free","Free","Booked","Free","Free","Booked","Free","Free","Free",
        100,4,25000],
       ["10244","Dr.Kane Willson",35,"Male","Available","General","Booked","Free","Booked","Free","Booked","Booked","Booked","Booked","Booked","Free","Booked","Booked","Free","Free","Booked",
        200,5,45000],
       ["10245","Dr.Smriti Singh",33,"Female","Available","Psychiatrist","Free","Booked","Free","Free","Booked","Free","Free","Booked","Booked","Free","Free","Booked","Free","Free","Booked",
        300,4,60000]]
    for i in L:
        r.writerow(i)
    a.close()


def display_schedule_by_name():
    a=open("doctor.csv","r")
    r=csv.reader(a)
    name=input("Enter doctors name: ")
    flag=0
    for i in r:
        if i[1]==name:
            flag=1
            print("9:00-9:30 = ", i[6])
            print("9:30-10:00 = ", i[7])
            print("10:00-10:30 = ", i[8])
            print("10:30-11:00 = ", i[9])
            print("11:00-11:30 = ", i[10])
            print("11:30-12:00 = ", i[11])
            print("12:00-12:30 = ", i[12])
            print("12:30-13:00 = ", i[13])
            print("14:00-14:30 = ", i[14])
            print("14:30-15:00 = ", i[15])
            print("15:00-15:30 = ", i[16])
            print("15:30-16:00 = ", i[17])
            print("16:00-16:30 = ", i[18])
            print("16:30-17:00 = ", i[19])
            print("17:00-17:30 = ", i[20])
            
            print()
    if flag!=1:
        print("Doctor not found")
        print()
    a.close()

def display_schedule_by_availability():
    a=open("doctor.csv","r")
    r=csv.reader(a)
    flag=0
    for i in r:
        if i[4]=="Available":
            print("9:00-9:30 = ", i[6])
            print("9:30-10:00 = ", i[7])
            print("10:00-10:30 = ", i[8])
            print("10:30-11:00 = ", i[9])
            print("11:00-11:30 = ", i[10])
            print("11:30-12:00 = ", i[11])
            print("12:00-12:30 = ", i[12])
            print("12:30-13:00 = ", i[13])
            print("14:00-14:30 = ", i[14])
            print("14:30-15:00 = ", i[15])
            print("15:00-15:30 = ", i[16])
            print("15:30-16:00 = ", i[17])
            print("16:00-16:30 = ", i[18])
            print("16:30-17:00 = ", i[19])
            print("17:00-17:30 = ", i[20])
            flag=1
            print()
    if flag!=1:
        print("Doctor not found")
        print()
    a.close()

def display_schedule_by_speciality():
    a=open("doctor.csv","r")
    r=csv.reader(a)
    special=input("Enter speciality of doctor: ")
    flag=0
    for i in r:
        if i[5]==special:
            print("9:00-9:30 = ", i[6])
            print("9:30-10:00 = ", i[7])
            print("10:00-10:30 = ", i[8])
            print("10:30-11:00 = ", i[9])
            print("11:00-11:30 = ", i[10])
            print("11:30-12:00 = ", i[11])
            print("12:00-12:30 = ", i[12])
            print("12:30-13:00 = ", i[13])
            print("14:00-14:30 = ", i[14])
            print("14:30-15:00 = ", i[15])
            print("15:00-15:30 = ", i[16])
            print("15:30-16:00 = ", i[17])
            print("16:00-16:30 = ", i[18])
            print("16:30-17:00 = ", i[19])
            print("17:00-17:30 = ", i[20])
            flag=1
            print()
    if flag!=1:
        print("Doctor not found")
        print()
    a.close()

def search_by_name():
    a=open("doctor.csv","r")
    r=csv.reader(a)
    name=input("Enter doctors name: ")
    flag=0
    for i in r:
        if i[1]==name:
            print("ID : ",i[0])
            print("Name : ",i[1])
            print("Age : ",i[2])
            print("Gender : ",i[3])
            print("Availability : ",i[4])
            print("Speciality : ",i[5])
            print("Price per appointment : ",i[21])
            print("Years worked : ",i[22])
            print("Salary : ",i[23])
            flag=1
            print()
    if flag!=1:
        print("Doctor not found")
        print()
    a.close()

def search_by_ID():
    a=open("doctor.csv","r")
    r=csv.reader(a)
    ID=input("Enter doctors id: ")
    flag=0
    for i in r:
        if i[0]==ID:
            print("ID : ",i[0])
            print("Name : ",i[1])
            print("Age : ",i[2])
            print("Gender : ",i[3])
            print("Availability : ",i[4])
            print("Speciality : ",i[5])
            print("Price per appointment : ",i[21])
            print("Years worked : ",i[22])
            print("Salary : ",i[23])
            flag=1
            print()
    if flag!=1:
        print("Doctor not found")
        print()
    a.close()

def search_by_availability():
    a=open("doctor.csv","r")
    r=csv.reader(a)
    flag=0
    for i in r:
        if i[4]=="Available":
            print("ID : ",i[0])
            print("Name : ",i[1])
            print("Age : ",i[2])
            print("Gender : ",i[3])
            print("Availability : ",i[4])
            print("Speciality : ",i[5])
            print("Price per appointment : ",i[21])
            print("Years worked : ",i[22])
            print("Salary : ",i[23])
            flag=1
            print()
    if flag!=1:
        print("Doctor not found")
        print()
    a.close()

def search_by_speciality():
    a=open("doctor.csv","r")
    r=csv.reader(a)
    special=input("Enter doctors speciality: ")
    flag=0
    for i in r:
        if i[5]==special:
            print("ID : ",i[0])
            print("Name : ",i[1])
            print("Age : ",i[2])
            print("Gender : ",i[3])
            print("Availability : ",i[4])
            print("Speciality : ",i[5])
            print("Price per appointment : ",i[21])
            print("Years worked : ",i[22])
            print("Salary : ",i[23])
            flag=1
            print()
    if flag!=1:
        print("Doctor not found")
        print()
    a.close()

def search_by_price_per_appointment():
    a=open("doctor.csv","r")
    r=csv.reader(a)
    print("Enter the price range of price per appointment to search for a doctor")
    lower=input("Enter the lowest price limit: ")
    higher=input("Enter the highest price limit: ")
    flag=0
    for i in r:
        if i[7]<=higher and i[7]>=lower:
            print("ID : ",i[0])
            print("Name : ",i[1])
            print("Age : ",i[2])
            print("Gender : ",i[3])
            print("Availability : ",i[4])
            print("Speciality : ",i[5])
            print("Price per appointment : ",i[21])
            print("Years worked : ",i[22])
            print("Salary : ",i[23])
            flag=1
            print()
    if flag!=1:
        print("Doctor not found")
        print()
    a.close()

def update_detail_schedule():
    a=open("doctor.csv","r")
    r=csv.reader(a)
    ID=input("Enter ID of doctor whose details is being updated: ")
    flag=0
    new_list=[]
    print("Select the timing to change detail:-")
    print("1) 9:00-9:30 ")
    print("2) 9:30-10:00 ")
    print("3) 10:00-10:30 ")
    print("4) 10:30-11:00 ")
    print("5) 11:00-11:30 ")
    print("6) 11:30-12:00 ")
    print("7) 12:00-12:30 ")
    print("8) 12:30-13:00 ")
    print("9) 14:00-14:30 ")
    print("10) 14:30-15:00 ")
    print("11) 15:00-15:30 ")
    print("12) 15:30-16:00 ")
    print("13) 16:00-16:30 ")
    print("14) 16:30-17:00 ")
    print("15) 17:00-17:30 ")
    option=int(input("Enter option number: "))
    if option==1:
        for i in r:
            if i[0]==ID:
                i[6]=input("Enter Free/Booked: ")
                flag=1
            new_list.append(i)
        if flag==0:
            print("Doctor not found")
            a.close()
        else:
            a=open("doctor.csv","w",newline="")
            w=csv.writer(a)
            w.writerows(new_list)
            a.close()
    if option==2:
        for i in r:
            if i[0]==ID:
                i[7]=input("Enter Free/Booked: ")
                flag=1
            new_list.append(i)
        if flag==0:
            print("Doctor not found")
            a.close()
        else:
            a=open("doctor.csv","w",newline="")
            w=csv.writer(a)
            w.writerows(new_list)
            a.close()
    if option==3:
        for i in r:
            if i[0]==ID:
                i[8]=input("Enter Free/Booked: ")
                flag=1
            new_list.append(i)
        if flag==0:
            print("Doctor not found")
            a.close()
        else:
            a=open("doctor.csv","w",newline="")
            w=csv.writer(a)
            w.writerows(new_list)
            a.close()
    if option==4:
        for i in r:
            if i[0]==ID:
                i[9]=input("Enter Free/Booked: ")
                flag=1
            new_list.append(i)
        if flag==0:
            print("Doctor not found")
            a.close()
        else:
            a=open("doctor.csv","w",newline="")
            w=csv.writer(a)
            w.writerows(new_list)
            a.close()
    if option==5:
        for i in r:
            if i[0]==ID:
                i[10]=input("Enter Free/Booked: ")
                flag=1
            new_list.append(i)
        if flag==0:
            print("Doctor not found")
            a.close()
        else:
            a=open("doctor.csv","w",newline="")
            w=csv.writer(a)
            w.writerows(new_list)
            a.close()
    if option==6:
        for i in r:
            if i[0]==ID:
                i[11]=input("Enter Free/Booked: ")
                flag=1
            new_list.append(i)
        if flag==0:
            print("Doctor not found")
            a.close()
        else:
            a=open("doctor.csv","w",newline="")
            w=csv.writer(a)
            w.writerows(new_list)
            a.close()
    if option==7:
        for i in r:
            if i[0]==ID:
                i[12]=input("Enter Free/Booked: ")
                flag=1
            new_list.append(i)
        if flag==0:
            print("Doctor not found")
            a.close()
        else:
            a=open("doctor.csv","w",newline="")
            w=csv.writer(a)
            w.writerows(new_list)
            a.close()
    if option==8:
        for i in r:
            if i[0]==ID:
                i[13]=input("Enter Free/Booked: ")
                flag=1
            new_list.append(i)
        if flag==0:
            print("Doctor not found")
            a.close()
        else:
            a=open("doctor.csv","w",newline="")
            w=csv.writer(a)
            w.writerows(new_list)
            a.close()
    if option==9:
        for i in r:
            if i[0]==ID:
                i[14]=input("Enter Free/Booked: ")
                flag=1
            new_list.append(i)
        if flag==0:
            print("Doctor not found")
            a.close()
        else:
            a=open("doctor.csv","w",newline="")
            w=csv.writer(a)
            w.writerows(new_list)
            a.close()
    if option==10:
        for i in r:
            if i[0]==ID:
                i[15]=input("Enter Free/Booked: ")
                flag=1
            new_list.append(i)
        if flag==0:
            print("Doctor not found")
            a.close()
        else:
            a=open("doctor.csv","w",newline="")
            w=csv.writer(a)
            w.writerows(new_list)
            a.close()
    if option==11:
        for i in r:
            if i[0]==ID:
                i[16]=input("Enter Free/Booked: ")
                flag=1
            new_list.append(i)
        if flag==0:
            print("Doctor not found")
            a.close()
        else:
            a=open("doctor.csv","w",newline="")
            w=csv.writer(a)
            w.writerows(new_list)
            a.close()
    if option==12:
        for i in r:
            if i[0]==ID:
                i[17]=input("Enter Free/Booked: ")
                flag=1
            new_list.append(i)
        if flag==0:
            print("Doctor not found")
            a.close()
        else:
            a=open("doctor.csv","w",newline="")
            w=csv.writer(a)
            w.writerows(new_list)
            a.close()
    if option==13:
        for i in r:
            if i[0]==ID:
                i[18]=input("Enter Free/Booked: ")
                flag=1
            new_list.append(i)
        if flag==0:
            print("Doctor not found")
            a.close()
        else:
            a=open("doctor.csv","w",newline="")
            w=csv.writer(a)
            w.writerows(new_list)
            a.close()
    if option==14:
        for i in r:
            if i[0]==ID:
                i[19]=input("Enter Free/Booked: ")
                flag=1
            new_list.append(i)
        if flag==0:
            print("Doctor not found")
            a.close()
        else:
            a=open("doctor.csv","w",newline="")
            w=csv.writer(a)
            w.writerows(new_list)
            a.close()
    if option==15:
        for i in r:
            if i[0]==ID:
                i[20]=input("Enter Free/Booked: ")
                flag=1
            new_list.append(i)
        if flag==0:
            print("Doctor not found")
            a.close()
        else:
            a=open("doctor.csv","w",newline="")
            w=csv.writer(a)
            w.writerows(new_list)
            a.close()

def update_detail_availability():
    a=open("doctor.csv","r")
    r=csv.reader(a)
    ID=input("Enter ID of doctor whose details is being updated: ")
    flag=0
    new_list=[]
    for i in r:
        if i[0]==ID:
            i[4]=input("Enter Available/Not Available: ")
            flag=1
        new_list.append(i)
    if flag==0:
        print("Doctor not found")
        a.close()
    else:
        a=open("doctor.csv","w",newline="")
        w=csv.writer(a)
        w.writerows(new_list)
        a.close()

def update_detail_salary():
    a=open("doctor.csv","r")
    r=csv.reader(a)
    ID=input("Enter ID of doctor whose details is being updated: ")
    flag=0
    new_list=[]
    for i in r:
        if i[0]==ID:
            i[23]=int(input("Enter salary: "))
            flag=1
        new_list.append(i)
    if flag==0:
        print("Doctor not found")
        a.close()
    else:
        a=open("doctor.csv","w",newline="")
        w=csv.writer(a)
        w.writerows(new_list)
        a.close()

def update_detail_price_per_appointment():
    a=open("doctor.csv","r")
    r=csv.reader(a)
    ID=input("Enter ID of doctor whose details is being updated: ")
    flag=0
    new_list=[]
    for i in r:
        if i[0]==ID:
            i[22]=int(input("Enter price per appointment: "))
            flag=1
        new_list.append(i)
    if flag==0:
        print("Doctor not found")
        a.close()
    else:
        a=open("doctor.csv","w",newline="")
        w=csv.writer(a)
        w.writerows(new_list)
        a.close()

def add_doctor():
    a=open("doctor.csv","a",newline="")
    w=csv.writer(a,delimiter=",")
    L=[]
    ID=int(input("ID : "))
    name=input("Name : ")
    age=int(input("Age : "))
    gender=input("Gender : ")
    availability=input("Availability : ")
    special=input("Speciality : ")
    t1=input("9:00-9:30 = ")
    t2=input("9:30-10:00 = ")
    t3=input("10:00-10:30 = ")
    t4=input("10:30-11:00 = ")
    t5=input("11:00-11:30 = ")
    t6=input("11:30-12:00 = ")
    t7=input("12:00-12:30 = ")
    t8=input("12:30-13:00 = ")
    t9=input("14:00-14:30 = ")
    t10=input("14:30-15:00 = ")
    t11=input("15:00-15:30 = ")
    t12=input("15:30-16:00 = ")
    t13=input("16:00-16:30 = ")
    t14=input("16:30-17:00 = ")
    t15=input("17:00-17:30 = ")
    ppa=int(input("Price per appointment : "))
    year=int(input("Years worked : "))
    salary=int(input("Salary : "))

    new=[ID,name,age,gender,availability,special,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,ppa,year,salary]
    L.append(new)

    for i in L:
        w.writerow(i)
    a.close()

def remove_doctor():
    a=open("doctor.csv","r")
    r=csv.reader(a)
    flag=0
    new_list=[]
    ID=int(input("Enter ID of doctor you want to delete: "))
    for i in r:
        if i[0]!=ID:
            new_list.append(i)
        else:
            flag=1
    if flag==0:
        print("Doctor not found")
    else:
        a=open("doctor.csv","w",newline="")
        w=csv.writer(a)
        w.writerows(new_list)
        a.close()
        print("Doctor of ID ",ID," has been removed ")
