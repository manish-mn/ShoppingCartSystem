from AdminControl.AdminHelper.AbstractSystemAdminOperations import *
from AdminControl.Modals.Admin import Admin


class SystemAdmin(AbstractSystemAdminOperations):
    def __init__(self):
        self.list_of_Admin = []
        self.logged_in_Admin = {}

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
