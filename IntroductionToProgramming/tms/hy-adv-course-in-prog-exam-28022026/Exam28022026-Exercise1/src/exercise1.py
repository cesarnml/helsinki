# Write your solution to exercise 1 here
class User:
    def __init__(self, username: str):
        self.__username = username
        self.__checked_in = False

    def __format(self, time: int, action: str):
        # "time;username;action"
        return f"{time};{self.__username};{action}"

    def check_in(self, time: int):
        if self.__checked_in:
            raise ValueError("User has already been checked in")
        else:
            self.__checked_in = True
            return self.__format(time, "CheckIn")

    def check_out(self, time: int):
        if self.__checked_in:
            self.__checked_in = False
            return self.__format(time, "CheckOut")
        else:
            raise ValueError("User has not been checked in")

    def __str__(self):
        return self.__username
