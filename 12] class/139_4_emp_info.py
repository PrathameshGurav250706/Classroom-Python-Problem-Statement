# Implement program to display information of 4 employee having class attribut  as company name, employee name, id, employee salary using class and object
class emp:
    company_name="abc"
    def input(self):
        self.name=input("Enter name :")
        self.id=int(input("Enter id :"))
        self.salary=int(input('Enter salary :'))
        
        
    def display(self):
        print("Employee Name : ",self.name)
        print("Employee Id :",self.id)
        print("Employee Salary :",self.salary)
        print("Employee Company Name :",self.company_name)
        print("-----------------------------")
        

employees=[]
for i in range(4):
    print("Enter details of employee",i+1)
    s=emp()
    s.input()
    employees.append(s)

print("\nEmployee details ")
for i in employees:
    i.display()