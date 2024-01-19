# admin_module.py
from models.admin_model import AdminModel
from colorama import Fore, Style
import time

class AdminModule:
    @staticmethod
    def view_all_users():
        # Retrieve and display all users from the database
        all_users = AdminModel.get_all_user()

        if all_users:
            print(f"\n{Fore.CYAN}All Users:{Style.RESET_ALL}")
            print("{:<10} {:<20} {:<30} {:<15}".format("User ID", "User Name", "Email", "Country"))
            print("-" * 75)
            for user_info in all_users:
                print("{:<10} {:<20} {:<30} {:<15}".format(*user_info[:4]))  # Extract the first 4 elements
        else:
            print(f"{Fore.YELLOW}No users available.{Style.RESET_ALL}")

    @staticmethod
    def remove_user():
        user_name = input(f"{Fore.YELLOW}Enter the username of the user you want to remove: {Style.RESET_ALL}")
        user_data = AdminModel.get_user_by_name(user_name)

        if user_data:
            print(f"\n{Fore.CYAN}User Details:{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"User ID: {user_data[0]}")
            time.sleep(0.2)
            print(f"Username: {user_data[1]}")
            time.sleep(0.2)
            print(f"Password: {user_data[2]}")
            time.sleep(0.2)
            print(f"Email: {user_data[3]}")
            time.sleep(0.2)
            print(f"Country: {user_data[4]}")

            confirmation = input(f"\n{Fore.YELLOW}Are you sure you want to remove this user? (yes/no): {Style.RESET_ALL}").lower()

            if confirmation == "yes":
                AdminModel.delete_user(user_name)
                print(f"{Fore.GREEN}User {user_name} removed successfully!{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}User removal canceled.{Style.RESET_ALL}")

        else:
            print(f"{Fore.YELLOW}No user found with the username: {user_name}{Style.RESET_ALL}")
