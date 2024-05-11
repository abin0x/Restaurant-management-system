from food_item import FoodItem
from menu import Menu
from User import Customer,Admin,Employee
from restaurent import Restuarent
from oders import Order


mares=Restuarent("mama restuarent") 
def customer_menu():
    name=input("Enter Your Name : ")
    email=input("Enter Your Email : ")
    phone=input("Enter Your Phone : ")
    address=input("Enter Your Address : ")
    customer=Customer(name=name,email=email,phone=phone,address=address)


    while True:
        print(f"Welcome {customer.name}!!")
        print("1. View Menu")
        print("2. Add To Cart Item")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")

        ch=int(input("Enter Your Choice : "))
        if ch==1:
            customer.view_menu(mares)

        elif ch==2:
            item_name=input("Enter Item name : ")
            item_quantity=int(input("Enter Item Quantity : "))
            customer.add_to_cart(mares,item_name,item_quantity)

        elif ch==3:
            customer.view_cart()

        elif ch==4:
            customer.pay_bill()
        elif ch==5:
            break
        else:
            print("Invalid Index")    


def admin_menu():
    name=input("Enter Your Name : ")
    email=input("Enter Your Email : ")
    phone=input("Enter Your Phone : ")
    address=input("Enter Your Address : ")
    admin=Admin(name=name,email=email,phone=phone,address=address)


    while True:
        print(f"Welcome {admin.name}!!")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Items")
        print("5. Exit")

        ch=int(input("Enter Your Choice : "))
        if ch==1:
            item_name=input("Enter item name : ")
            item_price=int(input("Enter item price : "))
            item_quantity=int(input("Enter item quantity : "))
            item=FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(mares,item)

        elif ch==2:
            name=input("Enter employee Name : ")
            email=input("Enter employee Email : ")
            phone=input("Enter employee Phone : ")
            address=input("Enter employee Address : ")
            age=input("Enter employee age : ")
            salary=input("Enter employee salary : ")
            designation=input("Enter employee designation : ")
            employee=Employee(name, phone, email, address,age,designation,salary)
            admin.add_employee(mares,employee)

        elif ch==3:
            admin.view_employee_list(mares)

        elif ch==4:
            admin.view_menu(mares)
        elif ch==5:
            item_name=input("Enter item name : ")
            admin.remove_item(mares,item_name)
        elif ch==6:
            break
        else:
            print("Invalid Index")   

while True:
    print("Welcome!!")
    print("1.Customer")
    print("2.Admin")
    print("3.Exit")
    ch=int(input("Enter your choice : "))
    if ch==1:
        customer_menu()
    elif ch==2:
        admin_menu()
    elif ch==3:
        break
    else:
        print("Invalid Index")

