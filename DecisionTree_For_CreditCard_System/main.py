
//Consider :

//Age : 0 - 60 years
//educational background : ssc,hsc,graduation.post graduation
//annual_income : Preferred in Lakhs

//Program :

def Check_credit(age,eduction_background,annual_income):
    if age>=60:
        print("Bad")
    if age>=24:
        if eduction_background=='graduation' or eduction_background=='postgraduation':
            if annual_income>=700000:
                print("Excellent")
            elif annual_income>=500000:
                print("Good")
            elif annual_income>=300000:
                print("Average")
            else:
                print("Bad")
        elif eduction_background=='hsc':
            if annual_income>=500000:
                print("Good")
            elif annual_income>=300000:
                print("Average")
            else:
                print("Bad")
        elif eduction_background=='ssc':
            if annual_income>=300000:
                print("Average")
            else:
                print("Bad")
    elif age>=21:
        if eduction_background=='graduation':
            if annual_income>=700000:
                print("Excellent")
            elif annual_income>=500000:
                print("Good")
            elif annual_income>=300000:
                print("Average")
            else:
                print("Bad")
        elif eduction_background=='hsc':
            if annual_income>=500000:
                print("Good")
            elif annual_income>=300000:
                print("Average")
            else:
                print("Bad")
        elif eduction_background=='ssc':
            if annual_income>=300000:
                print("Average")
            else:
                print("Bad")
    elif age>=18:
        if eduction_background=='hsc':
            if annual_income>=500000:
                print("Good")
            elif annual_income>=300000:
                print("Average")
            else:
                print("Bad")
        elif eduction_background=='ssc':
            if annual_income>=300000:
                print("Average")
            else:
                print("Bad")
    else:
        print("Bad")
age=int(input("Enter your age "))
education_background=input("Enter your Education Qualification (ssc,hsc,graduation,postgraduation)")
annual_income=float(input("Enter your annual income in Lakhs (LPA)"))
Check_credit(age,education_background,annual_income)
