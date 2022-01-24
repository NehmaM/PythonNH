class Employee( object ):
    
    def __init__(self,Empid,Name,Salary,Address):
        self.Empid = Empid
        self.Name = Name
        self.Salary = Salary
        self.Address = Address

class Teacher( Employee ):

    def __init__(self,Empid,Name,Salary,Address,dpt,sub):
        self.department = dpt
        self.subject = sub

        Employee.__init__(self,Empid,Name,Salary,Address)

    def display(self):
        print("\nEmployee Id : ",self.Empid)
        print("Name  : ",self.Name)
        print("Salary : ",self.Salary)
        print("Address : ",self.Address)
        print("Department : ",self.department)
        print("subject : ",self.subject)
    
obj2 = Teacher(1234,'Neh',10000,'XYZ','MCA','Python')

obj2.display()

obj1 = Teacher(4567,'Sana',20000,'WXY','MBA','Ethics')

obj1.display()
