class User:
    """
    generates new instances of a user.
    """
    user_list = [] #open 

    def __init__(self, username, password):
        """
        defines the properties of a user.
        """
        self.username = username
        self.password = password 