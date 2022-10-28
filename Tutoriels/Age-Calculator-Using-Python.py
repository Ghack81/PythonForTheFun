def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).day / 365.25)
    print("Your age is :",age)
    
#y=year m=month d=day
y=int(input("Enter your Birth year: "))
m=int(input("Enter your Birth month(1-12): "))
d=int(input("Enter your Birth date(1-31): "))
ageCalculator(y, m, d)

#Source => clcoding.com