from AdminControl.AdminHelper.AbstractSystemAdminOperations import *
from AdminControl.AdminHelper.AbstractSystemAdminProductOperations import *
from AdminControl.Modals.Admin import Admin
from AdminControl.Modals.Product import Product


class SystemAdmin(AbstractSystemAdminOperations, AbstractSystemAdminProductInformation):
    def __init__(self):
        self.list_of_Admin = []
        self.logged_in_Admin = {}
        self.product_list = []

    def verify_admin_list(self):
        if len(self.list_of_Admin) > 0:
            return True
        else:
            print("No admin is present.")
            return False

    def verify_admin_credentials_and_log_in(self, user_name, password):
        is_admin_exist = any(
            admin.user_name.lower() == user_name.lower() for admin in self.list_of_Admin
        )
        if is_admin_exist:
            admin_details = next(
                filter(
                    lambda admin: admin.user_name.lower() == user_name.lower(),
                    self.list_of_Admin,
                )
            )
            if password == admin_details.password:
                print(f"User logged in. Welcome {admin_details.Name}")
                self.logged_in_Admin[admin_details] = True
                return self.logged_in_Admin
            else:
                print(f"Incorrect password.")
                return self.logged_in_Admin
        else:
            print("Admin does not exist")
            self.logged_in_Admin

    def add_admin(self):
        admin = Admin()
        admin.Name = input("Enter your name\n")
        admin.user_name = self.validate_user_name()
        admin.password = input("Enter your password\n")
        self.list_of_Admin.append(admin)

    def validate_user_name(self):
        user_name_exists = True
        user_name = input("Enter user name\n")
        while user_name_exists:
            if any(
                filter(lambda admin: admin.user_name == user_name, self.list_of_Admin)
            ):
                print("User name already exist.")
            else:
                user_name_exists = False
        return user_name

    def admin_menu(self):
        while True:
            print("Welcome to admin control.")
            if self.verify_admin_list():
                self.verify_admin_credentials_and_log_in(
                    input("Please enter your username.\n"),
                    input("Please enter your password.\n"),
                )
                break
            else:
                user_input = input(
                    "Looks like there are no admins in the system. Would you like to register yourself. ?\nPress y for yes and n for no\n"
                )
                if user_input.lower() == "y" or user_input.lower() == "n":
                    if user_input.lower() == "y":
                        self.add_admin()
                    else:
                        break
                else:
                    print("Invalid input.")
                    break

    def list_product_with_quantity(self):
        if any(self.product_list):
            for product in self.product_list:
                print(f"The product id is {product.product_id}")
                print(f"The product name is {product.product_name}")
                print(f"The product description is {product.product_desciption}")
                print(f"The product quantity is {product.product_quantity}")
                print(f"The product price is {product.product_price}")
                print(f"The product was modified by {product.modified_by}")
        else:
            print("No products available")

    def add_product(self):
        product = Product()
        product.product_name = input("Enter your product name")
        product.product_desciption = input("Enter your product description")
        product.product_price = input("Enter your Product price")
        product.product_quantity = input("Enter your product quantity")
        if any(self.product_list):
            print(
                "Please enter product id. Please choose a unique id. Here is the product list with ids"
            )
            self.list_product_with_quantity()
            while True:
                product_id = input()
                if any(
                    filter(
                        lambda product: product.product_id == product_id,
                        self.product_list,
                    )
                ):
                    print("Product id already exist re-enter")
                    product_id = input()
                else:
                    product.product_id = product_id
                    break
        else:
            product.product_id = 1
        product.modified_by = next(self.logged_in_Admin).Name
        self.product_list.append(product)

    def modify_product(self):
        if any(self.product_list):
            while True:
                self.list_product_with_quantity()
                product_id = input("Enter The product id which you want to modify")
                if any(filter(lambda x: x == product_id, self.product_list)):
                    product = next(filter(lambda x: x == product_id, self.product_list))
                    while True:
                        print(
                            "Please 1 to update Name\n"
                            "Press 2 to update description\n"
                            "Press 3 to update Quantity\n"
                            "Press 4 to update Price"
                        )
                        option = input()
                        match option:
                            case "1":
                                product.product_name = input("Enter the updated Name")
                                product.modified_by = next(self.logged_in_Admin).Name
                            case "2":
                                product.product_desciption = input(
                                    "Enter the updated description"
                                )
                                product.modified_by = next(self.logged_in_Admin).Name
                            case "3":
                                product.product_quantity = input(
                                    "Enter the updated quantity"
                                )
                                product.modified_by = next(self.logged_in_Admin).Name
                            case "4":
                                product.product_price = input("Enter the updated price")
                                product.modified_by = next(self.logged_in_Admin).Name
                            case _:
                                print("Invalid option")
                        break
                else:
                    print(f"No product with id {product_id} exits")
                    break

        else:
            print("No products are there to add please add product")
