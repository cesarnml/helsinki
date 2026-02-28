# Write your solution to exercise 2 here
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


class UserManager:
    def __init__(self):
        self.__users: dict[str, User] = {}
        self.log: list[str] = []
        with open("logfile.csv", "a"):
            pass

    def add_user(self, username: str):
        if username in self.__users:
            raise ValueError("User already exists")
        else:
            self.__users[username] = User(username)

    def check_in(self, username: str, time: int):
        if username in self.__users:
            user = self.__users[username]
            try:
                log_entry = user.check_in(time)
                self.log.append(log_entry)
                return True
            except ValueError:
                return False
        else:
            raise ValueError("Invalid username")

    def check_out(self, username: str, time: int):
        if username in self.__users:
            user = self.__users[username]
            try:
                log_entry = user.check_out(time)
                self.log.append(log_entry)
                return True
            except ValueError:
                return False
        else:
            raise ValueError("Invalid username")

    def load_log(self) -> None:
        with open("logfile.csv", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                time_str, username, action = line.split(";")
                time = int(time_str)

                if username not in self.__users:
                    self.add_user(username)

                if action == "CheckIn":
                    self.check_in(username, time)
                elif action == "CheckOut":
                    self.check_out(username, time)

    def save_log(self) -> None:
        with open("logfile.csv", "w") as file:
            for event in self.log:
                file.write(f"{event}\n")

    def __str__(self) -> str:
        return "\n".join(self.log)
