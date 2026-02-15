from UserHelper.UserRegistration import UserRegistration


class UserOperations:
    def __init__(self, user_registration_obj, list_of_products):
        self.logged_in_user = None
        self.list_of_users = user_registration_obj.list_of_users
        self.product_list = list_of_products

    def validate_login_user_name(self, input_value):
        while any(input_value != user.username for user in self.list_of_users):
            input_value = input(
                "Please enter the user name again this user name doesn't exists"
            )
        return input

    def validate_password_for_login(self, input_password, user_details):
        while input_password != user_details.password:
            input_password = input("Please enter valid password this is not matching")
        return True

    def log_in_with_user(self):
        if any(self.list_of_users):
            print("No users are present first register yourself.")
        else:
            user_name = self.validate_login_user_name(
                input("Please enter your user name.")
            )
            user_details = next(
                filter(lambda x: user_name == x.username, self.list_of_users)
            )

            if self.validate_password_for_login(
                input("Please enter your password"), user_details
            ):
                print(f"User logged in with username {user_details.username}")
                self.logged_in_user = user_details

    def list_product_with_quantity(self):
        if any(self.product_list):
            print("Following are the products available : ")
            filtered_product_list = self.get_filtered_product_list()
            if any(filtered_product_list):
                for product in filtered_product_list:
                    print(f"The product id is {product.product_id}")
                    print(f"The product name is {product.product_name}")
                    print(f"The product description is {product.product_desciption}")
                    print(f"The product quantity is {product.product_quantity}")
                    print(f"The product price is {product.product_price}")
                    print(f"The product was modified by {product.modified_by}")
            else:
                print("No products available")
        else:
            print("No products are available.")

    def get_filtered_product_list(self):
        return filter(lambda x: x.product_quantity > 0, self.product_list)

    def validate_product_id_and_quantity(self, input_product_id, input_quantity):
        while not any(
            filter(
                lambda x: x.product_id == input_product_id,
                self.get_filtered_product_list(),
            )
        ):
            input_product_id = input("Please enter valid product id")

        product_details = next(
            filter(
                lambda x: x.product_id == input_product_id,
                self.get_filtered_product_list(),
            )
        )

        while product_details.product_quantity < input_quantity:
            input_quantity = input("Please enter correct quantity.")

        return {input_product_id: input_quantity}

    def add_product_to_cart(self):
        self.list_product_with_quantity()
        product_id = input("The product id which you want to add to cart")
        quantity = input("The quantity you want to add")
        product_details_with_quantity = self.validate_product_id_and_quantity(
            product_id, quantity
        )
        product_id = next(iter(product_details_with_quantity))
        quantity = next(iter(product_details_with_quantity.values()))
        product = next(p for p in self.product_list if p.product_id == product_id)
        product.product_quantity = product.product_quantity - quantity
        self.logged_in_user.shopingCart.append(product)

    def purchase_products(self):
        if any(self.logged_in_user.shopingCart):
            for product in self.logged_in_user.shopingCart:
                print(f"The product id is {product.product_id}")
                print(f"The product name is {product.product_name}")
                print(f"The product description is {product.product_desciption}")
                print(f"The product quantity is {product.product_quantity}")
                print(f"The product price is {product.product_price}")
            user_input = input(
                "Do you want to purchase the products ?\nType y for yes n for no"
            )
            if user_input.lower() == "y":
                self.logged_in_user.OrderedProducts = self.logged_in_user.shopingCart
                self.logged_in_user.shopingCart = []
            elif user_input.lower() == "n":
                print("We will see you again once you have made up your")
            else:
                print("Wrong input see you again.")
        else:
            print("No items in cart")
