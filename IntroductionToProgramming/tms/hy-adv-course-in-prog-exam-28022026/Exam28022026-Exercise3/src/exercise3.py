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


# Write your solution to exercise 2 here
class UserManager:
    def __init__(self):
        self.__users: dict[str, User] = {}
        self.log: list[str] = []
        with open("logfile.csv", "a"):
            pass
        self.load_log()

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
        self.log.clear()
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


# Write your solution to exercise 3 here
class UserInterface:
    def __init__(self, manager: UserManager):
        self.manager = manager

    def print_menu(self):
        print("0 - Exit program")
        print("1 - Check in")
        print("2 - Check out")
        print("3 - Add user")
        print("4 - View log for user")
        print("5 - View log")

    def execute(self):
        self.print_menu()
        while True:
            action = input("Choose action: ")
            if action == "0":
                print("Closing program...")
                self.manager.save_log()
                break
            elif action == "1":
                username = input("Username: ")
                time_str = input("Time: ")
                try:
                    time = int(time_str)
                    success = self.manager.check_in(username, time)
                    if success:
                        print("Checked in")
                    else:
                        print("User has already been checked in")
                except ValueError as e:
                    print(e)
            elif action == "2":
                username = input("Username: ")
                time_str = input("Time: ")
                try:
                    time = int(time_str)
                    success = self.manager.check_out(username, time)
                    if success:
                        print("Checked out")
                    else:
                        print("User has not been checked in")
                except ValueError as e:
                    print(e)
            elif action == "3":
                username = input("Username: ")
                try:
                    self.manager.add_user(username)
                    print("User creation succeeded!")
                except ValueError as e:
                    print(e)
            elif action == "4":
                username = input("Username: ")
                user_logs = []
                for entry in self.manager.log:
                    parts = entry.split(";")
                    if len(parts) >= 2 and parts[1] == username:
                        user_logs.append(entry)
                if user_logs:
                    for log in user_logs:
                        print(log)
                else:
                    print(f"No logs for user {username}")
            elif action == "5":
                if self.manager.log:
                    for log in self.manager.log:
                        print(log)
                else:
                    print("Log is empty")
            else:
                self.print_menu()
