# grade management system 
def create(n):
    stu_grade= []
    for i in range(n):
        d={}
        roll = int(input("Enter roll no.: "))
        name = input("Enter name: ")
        age = input("Age: ")
        clg = input("College name: ")
        Mark={}
        Mark["math_mark"]= float(input("maths mark:"))
        Mark["phy_mark"]=float(input("physics mark:"))
        Mark["che_mark"]=float(input("chem mark:"))
        d["Roll_no."]= roll
        d["Name"]= name
        d["Age"]=age
        d["College name"]=clg
        d["Marks"]=Mark
        stu_grade.append(d)
    return stu_grade

def display(roll, data):
    f=0
    for i in data:
        if i["Roll_no."]==roll:
            f=1
            print("Role number: ", i["Roll_no."])
            print("Name: ", i["Name"])
            print("Age: ",i["Age"])
            print("College name: ", i["College name"])
            print("Maths mark: ",i["Marks"]["math_mark"])
            print("Physics mark: ",i["Marks"]["phy_mark"])
            print("Chemistry mark: ",i["Marks"]["che_mark"])
    if (f==0):
        print("NOT FOUND")
    

    # [{"roll": 23 ,"name": "Sri","Age":18,"College":"NGP","Marks":{"math":76,"physics":89,"chem":78}}]
data=[]
while True:
    print("=======MENU========\n")
    print("!.Creaste data list\n")
    print("2.Display datalist\n")
    print("3.Exit\n")

    ch=int(input("Enter choice to continue:"))
    if ch==1:
        n = int(input("Enter no. of students: "))
        data.extend(create(n)) 
    elif ch==2:
        roll=int(input("Enter roll no.: "))
        display(roll, data)
    else:
        break
    



