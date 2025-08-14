
# function to add employees
def add_emp(a,l):
    b={}
    ID=int(input("Enter EMP_ID of EMP : "))
    x=input("Enter Name of EMP : ")
    b.update({"Name":x})
    x=input("Enter Dept of EMP : ")
    b.update({"Dept":x})
    x=input("Enter Job of EMP : ")
    b.update({"Job":x})
    l.append(ID)
    a.update({ID:b})

#function to display all employees
def display(a,list):
    for i in list:
        print("EMP_ID     : ",i)
        print("Name       : ",a[i]["Name"])
        print("Department : ",a[i]["Dept"])
        print("job        : ",a[i]["Job"])
        print("----------------------------")

#function to remove employee by ID
def remove(a,l):
    x=int(input("Enter EMP_ID to delete : "))
    for i in l:
        if (i==x):
            del   a[i]
            print("Deleted successfully ")

#function to find employees
def find(a,l):
    x=input("Enter Dept of EMP : ")
    y=input("Enter job of EMP : ")
    for i in l:
        if (a[i]["Dept"]==x) and (a[i]["Job"]==y):
            print("EMP_ID     : ",i)
            print("Name       : ",a[i]["Name"])
            print("Department : ",a[i]["Dept"])
            print("job        : ",a[i]["Job"])

#function to update employees information
def update(a,l):
    ID=int(input("Enter EMP_ID to update Data : "))
    print(a[ID])
    print("which thing you want to replace : ")
    print("1. Name")
    print("2. Dept")
    print("3. Job")
    y=int(input("choice : "))
    if(y==1):
        del a[ID]["Name"]
        z=input("Enter New Name : ")
        a[ID].update({"Name":z})
        print("Name updated successfully")
    elif(y==2):
        del a[ID]["Dept"]
        z=input("Enter New Dept : ")
        a[ID].update({"Dept":z})
        print("Dept updated successfully")
    elif(y==3):
        del a[ID]["Job"]
        z=input("Enter New Job : ")
        a[ID].update({"Job":z})
        print("Job updated successfully")
    else:
        print("wrong choice ")

#main function
EMP ={}
List =[]
again="y"
while (again=="y"):
    print("1. Add Employees")
    print("2. Find EMP by Dept and Job")
    print("3. Remove EMP")
    print("4. Update EMP information")
    print("5. Display All EMP")
    print("6. Exit")
    a=int(input("choice : "))
    if(a==1):
        add_emp(EMP,List)
    elif(a==2):
        find(EMP,List)
    elif(a==3):
        remove(EMP,List)
    elif(a==4):
        update(EMP,List)
    elif(a==5):
        display(EMP,List)
    elif(a==6):
        break
    else:
        print ("wrong choice")
    again=input("Do you want to try again y/n : ")
print("--------End program--------")   