class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.is_length_valid(value) and self.is_digit(value) and self.is_upper_case(value):
            self.__password = value
            return
        raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')

    def is_length_valid(self, password):
        return len(password) >= 8

    def is_upper_case(self, password):
        upper_case = [char for char in password if char.isupper()]
        return True if upper_case else False

    def is_digit(self, password):
        digit_case = [char for char in password if char.isdigit()]
        return True if digit_case else False

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*"* len(self.password)}'



correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
