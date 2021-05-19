import pickle
from Bank import Bank
from MenuManagement import MenuManagement


def default_print():
    exist = False
    state = input("Type number:")
    if state == "1":
        MenuManagement.about_info()
        MenuManagement.static_menu()
        default_print()

    elif state == "2":
        login1 = input("Please, input login:")
        password1 = input("Please, input password:")
        if login1 == "admin" and password1 == "admin":
            print("Login as an administrator was successful!")
            while True:
                MenuManagement.admin_menu_info()
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
                    try:
                        id = int(input("Enter user id: "))
                        temp_user = temp_dict_file.pop(id)
                        print("User was successfully deleted!")

                        del temp_user
                    except:
                        print("Error occurred! Try again")

                elif state2 == "3":
                    show_info()
                elif state2 == "4":

                    break
                else:
                    print("Error occurred! Try again!")

        for obj in temp_dict_file:
            if obj.password == password1 and obj.login == login1:
                print("Login was successful!")
                while True:
                    MenuManagement.user_menu_info()
                    state1 = input()
                    if state1 == "1":
                        try:
                            amount = int(input("Enter Deposit amount: "))
                            obj.deposit(amount)
                        except:
                            print("Error occurred! Try again!")

                    elif state1 == "2":
                        try:
                            amount = int(input("Enter Withdraw amount: "))
                            obj.withdraw(amount)
                        except:
                            print("Error occurred! Try again!")

                    elif state1 == "3":
                        obj.view_balance()

                    elif state1 == "4":
                        obj.show_details()

                    elif state1 == "5":
                        break
                    else:
                        print("Error occurred! Try again!")
        MenuManagement.static_menu()
        default_print()

    elif state == "3":
        print("Session is cancelled")
    else:
        print("Error occurred! Try again!")
        MenuManagement.static_menu()
        default_print()


def show_info():
    i = 0
    for obj in config_dictionary:
        print(i, ":", obj.name, "-", obj.second_name, "|Gender:",
              obj.gender, "|Balance:", obj.balance)
        i += 1


with open('config.dictionary', 'rb') as config_dictionary_file:
    config_dictionary = pickle.load(config_dictionary_file)
temp_dict_file = config_dictionary

MenuManagement.static_menu()
default_print()
with open('config.dictionary', 'wb') as config_dictionary_file:

    pickle.dump(temp_dict_file, config_dictionary_file)
