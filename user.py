class User:
    """
    a class that generates new instances of users
    """
    pass

    user_list = []

    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        
    def save_user_details(self):
        """
        save_user method saves new user objects into user_list
        """
        User.user_list.append(self)