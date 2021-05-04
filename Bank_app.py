import pickle


class User():
    def __init__(self, name, second_name, age, gender, login, password):
        self.name = name
        self.second_name = second_name
        self.age = age
        self.gender = gender
        self.login = login
        self.password = password

    def show_details(self):
        print("Personal Details:")
        print("")
        print("Name: ", self.name)
        print("Second Name:", self.second_name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)


class Bank(User):
    def __init__(self, name, second_name, age, gender, login, password):
        super().__init__(name, second_name, age, gender, login, password)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance+self.amount
        print("Account balance has beeen updated: ", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print(
                "Error! Given number is bigger then your balance! Balance Available:", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated: ", self.balance)

    def view_balance(self):
        print("Account balance: ", self.balance)


users = []

i = 0


def default_print():
    exist = False
    print("********BANK MANAGEMENT SYSTEM*********")
    print("*------1:About-------------------------*")
    print("*------2:Login------------------------*")
    print("*------3:Exit-------------------------*")
    print("***************************************")
    state = input("Type number:")
    if state == "1":
        print("___________________________________________________________")
        print("App was created by Maksym Severyn, It-12sp.")
        print("This program shows how a simple banking system works.")
        print("To use it, follow text guide, that appears in the console.")
        print("___________________________________________________________")
        default_print()

    elif state == "2":
        login1 = input("Please, input login:")
        password1 = input("Please, input password:")
        if login1 == "admin" and password1 == "admin":
            while True:
                admin_menu_info()
                state2 = input()
                if state2 == "1":
                    name = input("Name: ")
                    second_name = input("Second Name: ")
                    age = input("Enter age: ")
                    gender = input("Enter gender: ")
                    login = input("Enter login: ")
                    password = input("Enter password: ")
                    variable = input("Id: ")
                    variable = Bank(name, second_name, age,
                                    gender, login, password)

                    for obj in temp_dict_file:
                        if obj.name == variable.name and obj.password == variable.password and obj.login == variable.login:
                            print("Item already exist")
                            exist = True
                    if exist == False:
                        temp_dict_file.append(variable)
                elif state2 == "2":
                    show_info()
                    id = int(input("Enter user id: "))
                    temp_user = temp_dict_file.pop(id)
                    print("User was successfully deleted!")

                    del temp_user

                elif state2 == "3":
                    show_info()
                elif state2 == "4":
                    break

        for obj in temp_dict_file:
            if obj.password == password1 and obj.login == login1:
                print("Login was successful!")
                while True:
                    user_menu_info()
                    state1 = input()
                    if state1 == "1":
                        amount = int(input("Enter Deposit amount: "))
                        obj.deposit(amount)

                    elif state1 == "2":
                        amount = int(input("Enter Withdraw amount: "))
                        obj.withdraw(amount)

                    elif state1 == "3":
                        obj.view_balance()

                    elif state1 == "4":
                        break

        default_print()

    elif state == "3":
        print("Session is cancelled")


def user_menu_info():
    print("1:Deposit")
    print("2:Withdraw")
    print("3:View Balance")
    print("4:Exit")


def admin_menu_info():
    print("1:Create")
    print("2:Delete")
    print("3:Show users information")
    print("4:Exit")


def show_info():
    i = 0
    for obj in config_dictionary:
        print(i, ":", obj.name, "-", obj.second_name, "|Gender:",
              obj.gender, "|Balance:", obj.balance)
        i += 1
        #i = 0
        # for obj in temp_dict_file:
        #    print(i, ":", obj.name, obj.age, obj.gender)
        #  i += 1


with open('config.dictionary', 'rb') as config_dictionary_file:
    config_dictionary = pickle.load(config_dictionary_file)
temp_dict_file = config_dictionary


default_print()
with open('config.dictionary', 'wb') as config_dictionary_file:

    pickle.dump(temp_dict_file, config_dictionary_file)


# for obj in config_dictionary:
  #  print(obj.name, obj.gender, obj.balance)
