# views/admin_views.py
from modules.admin_module import AdminModule
from modules.user_module import UserModel, UserModule
from colorama import Fore, Style
import time

def print_menu_option(option_number, option_text):
    print(f"{Fore.YELLOW}{option_number} {option_text} {Style.RESET_ALL}")

def admin_menu():
    admin_module = AdminModule()

    while True:
        print(f"\n{Fore.CYAN}Admin Menu:{Style.RESET_ALL}")
        time.sleep(0.2)
        print_menu_option("1", "Remove User")
        time.sleep(0.2)
        print_menu_option("2", "Add New User")
        time.sleep(0.2)
        print_menu_option("3", "View Energy Data Comparison by date")
        time.sleep(0.2)
        print_menu_option("4", "Get Users")
        time.sleep(0.2)
        print_menu_option("5", "Search Energy Data")
        time.sleep(0.2)
        print_menu_option("6", "Exit")

        choice = input(f"{Fore.WHITE}\nEnter your choice: {Style.RESET_ALL}")

        if choice == "1":
            admin_module.remove_user()
        elif choice == "2":
            print(f"{Fore.YELLOW}Adding User:{Style.RESET_ALL}")
            user_name = input("Enter the username: ")
            password = input("Enter the password: ")
            email = input("Enter the email: ")
            country = input("Enter the country: ")
            UserModel.create_user(user_name, password, email, country)
        elif choice == "3":
            UserModule.energy_compare_by_date_for_countries()
        elif choice == "4":
            admin_module.view_all_users()
        elif choice == "5":
            UserModule.search_energy_data()
        elif choice == "6":
            print(f"{Fore.RED}Exiting Admin Menu.{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")
