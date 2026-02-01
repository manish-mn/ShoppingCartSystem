from AdminControl.Modals import User


class UserRegistration:
    def __init__(self):
        self.list_of_users = []

    def add_user(self):
        print(
            "Welcome to our shopping app. Please provide details to register yourself as a user :"
        )
        user = User()
        user.name = self.check_null_empty(input("Please enter your name")).lower()
        user.username = self.validate_user_user_name(
            self.check_null_empty(input("Please enter your user id"))
        ).lower()
        user.email = self.validate_user_email(
            self.check_null_empty(input("Please enter your user email"))
        ).lower()
        user.phoneNo = self.check_null_empty(
            input("Please enter your phone number")
        ).lower()
        user.password = self.check_null_empty(
            input("Please enter your phone number")
        ).lower()
        user.userId = len(self.list_of_users) + 1
        self.list_of_users.append(user)
        print(f"User added successfully with user id - {user.userId}")

    def validate_user_creds(self, cred_type, input):
        match cred_type:
            case "email":
                return self.validate_user_email(input)
            case "username":
                return self.validate_user_user_name(input)

    def validate_user_email(self, input_value):
        while any(
            input_value.lower() == user.email.lower() for user in self.list_of_users
        ):
            input_value = input("Please enter the email this email already exists")
        return input_value

    def validate_user_user_name(self, input_value):
        while any(
            input_value.lower() == user.username.lower() for user in self.list_of_users
        ):
            input_value = input(
                "Please enter the user name again this user name already exists"
            )
        return input

    def check_null_empty(self, input_value):
        while not input_value:
            input_value = input("Please enter value in empty value is not supported")
        return input_value

    def log_in_with_user(self):
        pass
