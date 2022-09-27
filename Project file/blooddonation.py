import csv
def donors():
    add=open("blooddonationcamp.csv","a",newline="")
    w=csv.writer(add,delimiter=",")
    L=[]
    d_fname = input("Enter the First Name of the Donor:")
    d_lname = input("Enter the Last Name of the Donor:")
    age = int(input("Enter the Age of the Donor:"))
    gender = input("Enter the Gender of the Donor:")
    d_bloodgroup = input("Enter the Donor's Blood Group:")
    d_phoneno = int(input("Enter the Donor's Phone Number:"))
    email = input("Enter the Patient's Email:")
    eligibilty=input("Eligible to donate Blood:")   
    donation_time=input("Enter the time of donation:")

    new_donors=[d_fname,d_lname,age,gender,d_bloodgroup,d_phoneno,email,eligibilty,donation_time]
    L.append(new_donors)

    for i in L:
        w.writerow(i)
    add.close()
