medical = input("did you have a medical cause Y or N: ")

attendance = int(input("enter the attendance of the student: "))

if medical == 'Y' or medical == "y":
    print ("You are allowed")
else:
    if attendance>=75:
        print ("Allowed")
    else:
        print ("Not allowed")