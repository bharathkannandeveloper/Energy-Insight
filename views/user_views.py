# views/user_views.py
from modules.user_module import UserModule
from colorama import Fore, Style
import time

def print_menu_option(option_number, option_text):
    print(f"{Fore.YELLOW}{option_number} {option_text} {Style.RESET_ALL}")

def user_menu(user_name):
    user_module = UserModule()

    while True:
        print(f"\n{Fore.CYAN}User Menu:{Style.RESET_ALL}")

        print_menu_option("1", "View Energy Data Summary")
        time.sleep(0.2)
        print_menu_option("2", "Update Profile Information")
        time.sleep(0.2)
        print_menu_option("3", "View Energy Data Comparison")
        time.sleep(0.2)
        print_menu_option("4", "View Energy Data Comparison by date")
        time.sleep(0.2)
        print_menu_option("5", "Search Energy Data")
        time.sleep(0.2)
        print_menu_option("6", "Global Energy Insights")
        time.sleep(0.2)
        print_menu_option("7", "Exit")

        choice = input(f"{Fore.WHITE}\nEnter your choice: {Style.RESET_ALL}")

        if choice == "1":
            user_module.view_energy_data_summary()
        elif choice == "2":
            user_module.update_profile_information(user_name)
        elif choice == "3":
            user_module.view_energy_data_comparison()
        elif choice == "4":
            user_module.energy_compare_by_date_for_countries()
        elif choice == "5":
            user_module.search_energy_data()
        elif choice == "6":
            user_module.global_energy_insights()
        elif choice == "7":
            print(f"{Fore.RED}Exiting User Menu.{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")
