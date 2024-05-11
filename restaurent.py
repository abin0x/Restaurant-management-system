from menu import Menu
class Restuarent:
    def __init__(self,name):
        self.name=name
        self.employees=[] #ata amder database
        self.menu=Menu()

    def add_employee(self,employee):
        self.employees.append(employee)


    def view_employee_list(self):
        print("<----------Employee List---------->")
        for emp in self.employees:
            # print(emp.name,emp.email,emp.phone,emp.address)
            print(f"Name : {emp.name}\nEmail : {emp.email}\nPhone : {emp.phone}\nAddress : {emp.address}\n")

