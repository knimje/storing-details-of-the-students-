#wap that stores a college and branch of a female student and mobile sem and branch of a male stadent use concept of tuple,dict,loop,and conditional statements to fetch these details based on the name entered by the user
a=int(input("Enter total number of students"))
details={}
stu = (details)

while a!=0:
    gender = input("enter gender ")
    if gender == "female":
        name=input("enter name ")
        details[name] = {"college": input("Enter mobile number: "), "branch": input("Enter branch: ")}
        print(details)
    elif gender=="male":
        name=input("enter name ")
        details[name] = {"mobile": input("Enter college: "), "semester": input("Enter semester: ")}
        print(details)
    a-=1
for i in stu:
    print(i,"\n")
search=input("enter the name to be searched ")
if search in stu:
    print(details[search])