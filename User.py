
from abc import ABC
from oders import Order
class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart=Order()

    def view_menu(self,restuarent):
        restuarent.menu.show_menu()

    def add_to_cart(self,restuarent,item_name,quantity):
        item=restuarent.menu.find_item(item_name)
        print(f"Sorry,You want to {item.quantity} {item.name}")
        if item:
            if quantity>item.quantity:
                print("But Item Quantity is very high!!!")
            else:
                item.quantity=quantity
                self.cart.add_item(item)
                print("Item Added!!")

        else:
            print("Item not found")

    def view_cart(self):
        print("****View Cart****")
        print("Name\tPrice\tQuantity\t")
        print("----\t-----\t--------")  
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t {item.price}\t   {quantity}")
        print(f"Total Price : {self.cart.total_price}")

    def pay_bill(self):
        print(f"Total {self.cart.total_price} paid successfully")
        self.cart.clear()

class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address)        
        self.age=age
        self.designation=designation
        self.salary=salary


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        # self.employees=[] #ata amder database


    def add_employee(self,restuarent,employee):
        restuarent.add_employee(employee)
 
    def view_employee_list(self,restuarent):
       restuarent.view_employee_list()

    def add_new_item(self,restuarent,item):
        restuarent.menu.add_menu_item(item) 

    def remove_item(self,restuarent,item):
        restuarent.menu.remove_item(item) 


    def view_menu(self,restuarent):
        restuarent.menu.show_menu()        


        