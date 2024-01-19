# main.py
from models.user_model import UserModel
from models.admin_model import AdminModel
from views.user_views import user_menu
from views.admin_views import admin_menu
import pyfiglet
from colorama import Fore, Style
from getpass import getpass
import time

def print_ascii_art(text, color=Fore.CYAN):
    banner = pyfiglet.figlet_format(text)
    print(color + banner + Style.RESET_ALL)

def styled_input(prompt, color=Fore.YELLOW):
    user_input = input(color + prompt + Style.RESET_ALL)
    return user_input

def password_input(prompt, color=Fore.YELLOW):
    password = getpass(color + prompt + Style.RESET_ALL)
    print("")  # Print an empty line for better visual separation
    return password

def user_login():
    print(Fore.CYAN + "\nUser Login" + Style.RESET_ALL)
    username = styled_input("Enter your username: ")
    password = password_input("Enter your password (hidden): ")

    user = UserModel.get_user_by_name(username, password)

    if user:
        print(Fore.GREEN + "\nLogin successful." + Style.RESET_ALL)
        time.sleep(1)
        user_menu(username)
    else:
        print(Fore.RED + "\nLogin failed. Please check your username and password." + Style.RESET_ALL)
        print("\nUser Registration:")
        user_name = styled_input("Enter your username: ")
        password = password_input("Enter your password (hidden): ")
        email = styled_input("Enter your email: ")
        country = styled_input("Enter your country: ")
        UserModel.create_user(user_name, password, email, country)

def admin_login():
    print(Fore.CYAN + "\nAdmin Login" + Style.RESET_ALL)
    adminname = styled_input("Enter your Admin name: ")
    password = password_input("Enter your password (hidden): ")

    user = AdminModel.get_admin_by_name(adminname, password)

    if user:
        print(Fore.GREEN + "\nLogin successful." + Style.RESET_ALL)
        admin_menu()
    else:
        print(Fore.RED + "\nLogin failed. Please check your username and password." + Style.RESET_ALL)
        print("Admin Registration:")
        admin_name = styled_input("Enter your Admin name: ")
        password = password_input("Enter your password (hidden): ")
        AdminModel.create_admin(admin_name, password)

def main():
    print(Fore.RED+80*"="+Style.RESET_ALL)
    print_ascii_art("Energy Insight", Fore.YELLOW)
    print(Fore.GREEN+"\t\t Project Done by < Gokul S />"+Style.RESET_ALL)
    print(Fore.RED+80*"="+Style.RESET_ALL)

    while True:
        print(Fore.CYAN + "\nMain Menu:" + Style.RESET_ALL)
        time.sleep(0.2)
        print("1. " + Fore.YELLOW + "User Login" + Style.RESET_ALL)
        time.sleep(0.2)
        print("2. " + Fore.YELLOW + "Admin Login" + Style.RESET_ALL)
        time.sleep(0.2)
        print("3. " + Fore.YELLOW + "User Registration" + Style.RESET_ALL)
        time.sleep(0.2)
        print("4. " + Fore.YELLOW + "Admin Registration" + Style.RESET_ALL)
        time.sleep(0.2)
        print("5. " + Fore.RED + "Exit" + Style.RESET_ALL)
        

        choice = styled_input("\nEnter your choice: ")

        if choice == '1':
            user_login()
        elif choice == '2':
            admin_login()
        elif choice == '3':
            print("User Registration:")
            user_name = styled_input("Enter your username: ")
            password = password_input("Enter your password (hidden): ")
            email = styled_input("Enter your email: ")
            country = styled_input("Enter your country: ")
            UserModel.create_user(user_name, password, email, country)
        elif choice == '4':
            print("Admin Registration:")
            admin_name = styled_input("Enter your Admin name: ")
            password = password_input("Enter your password (hidden): ")
            AdminModel.create_admin(admin_name, password)
        elif choice == '5':
            print(Fore.RED + "Exiting the application. Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
