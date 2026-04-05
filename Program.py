from AdminControl.AdminHelper.SystemAdmin import SystemAdmin
from UserHelper.UserOperations import UserOperations
from UserHelper.UserRegistration import UserRegistration

def main():
    system_admin = SystemAdmin()
    user_registration = UserRegistration()
    user_operations = UserOperations(user_registration, system_admin.product_list)

    while True:
        print("Welcome to Shopping Cart System")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            system_admin.admin_menu()
        elif choice == "2":
            user_operations.user_menu()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()