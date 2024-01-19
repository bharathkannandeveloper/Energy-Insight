# modules/user_module.py
from models.user_model import UserModel, EnergyModel
from colorama import Fore, Style
import time

class UserModule:
    @staticmethod
    def view_energy_data_summary():
        print(f"{Fore.CYAN}\nSelect a country for energy summary:{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}1. Australia{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}2. India{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}3. Canada{Style.RESET_ALL}")

        country_choice = input("Enter the number corresponding to the country: ")

        country_mapping = {
            '1': 'Australia',
            '2': 'India',
            '3': 'Canada'
        }

        selected_country = country_mapping.get(country_choice)

        if selected_country:
            energy_summary = EnergyModel.get_energy_summary(selected_country)

            # Print or process the energy summary as needed
            print(f"\n{Fore.CYAN}Energy Summary for {selected_country}:{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}For Energy Consumption:{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Total Consumption: {energy_summary[0]}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Average Consumption: {energy_summary[1]}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Min Consumption: {energy_summary[2]}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Max Consumption: {energy_summary[3]}")
            time.sleep(0.2)
            print()
            print(f"{Fore.CYAN}For Energy Production{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Total Production: {energy_summary[4]}{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Average Production: {energy_summary[5]}{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Min Production: {energy_summary[6]}{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Max Production: {energy_summary[7]}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Invalid country choice. Please try again.{Style.RESET_ALL}")
            time.sleep(0.2)

    @staticmethod
    def update_profile_information(user_name):
        print(f"\n{Fore.CYAN}Update Profile Information:{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}1. Update Password{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}2. Update Email{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}3. Update Country{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}4. Go back{Style.RESET_ALL}")
        time.sleep(0.2)

        choice = input("Enter your choice: ")

        if choice == "1":
            new_password = input("Enter your new password: ")
            UserModel.update_password(user_name, new_password)
            print(f"{Fore.GREEN}Password updated successfully!{Style.RESET_ALL}")

        elif choice == "2":
            new_email = input("Enter your new email: ")
            UserModel.update_email(user_name, new_email)
            print(f"{Fore.GREEN}Email updated successfully!{Style.RESET_ALL}")

        elif choice == "3":
            new_country = input("Enter your new country: ")
            UserModel.update_country(user_name, new_country)
            print(f"{Fore.GREEN}Country updated successfully!{Style.RESET_ALL}")

        elif choice == "4":
            print("Going back to the main menu.")

        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")

    @staticmethod
    def view_energy_data_comparison():
        print(f"\n{Fore.CYAN}Energy Data Comparison:{Style.RESET_ALL}")

        # Display the list of available countries
        available_countries = ["Australia", "India", "USA", "Canada"]
        print(f"{Fore.CYAN}Available Countries:{Style.RESET_ALL}")
        for i, country in enumerate(available_countries, start=1):
            print(f"{i}. {country}")

        # Get user input for the first country
        while True:
            try:
                choice1 = int(input("Enter the number corresponding to the first country: "))
                if 1 <= choice1 <= len(available_countries):
                    country1 = available_countries[choice1 - 1]
                    break
                else:
                    print(f"{Fore.RED}Invalid choice. Please enter a valid number.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}")

        # Get user input for the second country
        while True:
            try:
                choice2 = int(input("Enter the number corresponding to the second country: "))
                if 1 <= choice2 <= len(available_countries) and choice2 != choice1:
                    country2 = available_countries[choice2 - 1]
                    break
                else:
                    print(f"{Fore.RED}Invalid choice. Please enter a valid number different from the first choice.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}")

        # Retrieve and display energy data for the selected countries
        data_country1 = EnergyModel.get_energy_summary(country1)
        data_country2 = EnergyModel.get_energy_summary(country2)

        print(f"\n{Fore.CYAN}\nEnergy Data Comparison for {country1} and {country2}:{Style.RESET_ALL}")
        print("-" * 50)
        print(f"{Fore.CYAN}\nFor Energy Consumption:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{country1} - Total Consumption: {data_country1[0]}{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}{country2} - Total Consumption: {data_country2[0]}{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}{country1} - Average Consumption: {data_country1[1]}{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}{country2} - Average Consumption: {data_country2[1]}{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}{country1} - Min Consumption: {data_country1[2]}{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}{country2} - Min Consumption: {data_country2[2]}{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}{country1} - Max Consumption: {data_country1[3]}{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}{country2} - Max Consumption: {data_country2[3]}{Style.RESET_ALL}")
        time.sleep(0.2)

        print(f"{Fore.CYAN}\nFor Energy Production:{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}{country1} - Total Production: {data_country1[4]}{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}{country2} - Total Production: {data_country2[4]}{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}{country1} - Average Production: {data_country1[5]}{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}{country2} - Average Production: {data_country2[5]}{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}{country1} - Min Production: {data_country1[6]}{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}{country2} - Min Production: {data_country2[6]}{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}{country1} - Max Production: {data_country1[7]}{Style.RESET_ALL}")
        time.sleep(0.2)
        print(f"{Fore.YELLOW}{country2} - Max Production: {data_country2[7]}{Style.RESET_ALL}")
        time.sleep(0.2)


    def search_energy_data():
        print("\nEnergy Data Search:")

        # Get user input for the country
        country = input("Enter the country for which you want to search energy data: ")

        # Get user input for the year
        while True:
            try:
                year = int(input("Enter the year for which you want to search energy data: "))
                if year > 0:
                    break
                else:
                    print("Invalid input. Please enter a valid year.")
            except ValueError:
                print("Invalid input. Please enter a valid year.")

        # Retrieve and display energy data for the selected country and year
        data = EnergyModel.get_energy_data_by_year(country, year)

        if data:
            print(f"\n{Fore.CYAN}Energy Data for {country} in {year}:{Style.RESET_ALL}")
            print("---------------------------------------------------")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Population: {data[0]}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Coal Consumption: {data[1]}{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Coal Production: {data[2]}{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Oil Consumption: {data[3]}{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Oil Production: {data[4]}{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Gas Consumption: {data[5]}{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Gas Production: {data[6]}{Style.RESET_ALL}")

        else:
            print(f"{Fore.RED}No data found for {country} in {year}.{Style.RESET_ALL}")

    def global_energy_insights():
        print("Global Energy Insights:")

        # Fetch global energy data
        global_data = EnergyModel.get_global_energy_data()

        if global_data:
            total_consumption, average_consumption, total_production, average_production = global_data

            print(f"\n{Fore.CYAN}For Energy Consumption:{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Total Global Consumption: {total_consumption}{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Average Global Consumption: {average_consumption}{Style.RESET_ALL}")
            time.sleep(0.2)

            print(f"{Fore.YELLOW}\nFor Energy Production:{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"Total Global Production: {total_production}{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"Average Global Production: {average_production}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}No global energy data available.{Style.RESET_ALL}")


    def energy_compare_by_date_for_countries():
        # Get user input for date and countries
        year_to_compare = input("Enter the year to compare: ")
        countries_input = input("Enter the countries to compare (comma-separated): ")

        # Convert the input countries to a list
        selected_countries = [country.strip() for country in countries_input.split(',')]

        # Call the UserModel function to get the comparison results
        comparison_results = EnergyModel.energy_compare_by_date_for_countries(year_to_compare, selected_countries)

        # Display the results
        if comparison_results:
            print(f"{Fore.YELLOW}\nEnergy Comparison Results:{Style.RESET_ALL}")
            time.sleep(0.2)
            print("{:<15} {:<20} {:<20}".format("Country", "Total Consumption", "Total Production"))
            for result in comparison_results:
                country, total_consumption, total_production = result
                print("{:<15} {:<20} {:<20}".format(country, total_consumption, total_production))
        else:
            print(f"{Fore.YELLOW}No data available for the specified date and countries.{Style.RESET_ALL}")        

    @staticmethod
    def search_energy_data():
        print(f"\n{Fore.CYAN}Energy Data Search:{Style.RESET_ALL}")

        # Get user input for the country
        country = input(f"Enter the country for which you want to search energy data: ")

        # Get user input for the year
        while True:
            try:
                year = int(input("Enter the year for which you want to search energy data: "))
                if year > 0:
                    break
                else:
                    print(f"{Fore.RED}Invalid input. Please enter a valid year.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Invalid input. Please enter a valid year.{Style.RESET_ALL}")

        # Retrieve and display energy data for the selected country and year
        data = EnergyModel.get_energy_data_by_year(country, year)

        if data:
            print(f"\n{Fore.CYAN}Energy Data for {country} in {year}:{Style.RESET_ALL}")
            print("-" * 50)
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Population: {data[0]}{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Coal Consumption: {data[1]}{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Coal Production: {data[2]}{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Oil Consumption: {data[3]}{Style.RESET_ALL}")

            time.sleep(0.2)
            print(f"{Fore.YELLOW}Oil Production: {data[4]}{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Gas Consumption: {data[5]}{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Gas Production: {data[6]}{Style.RESET_ALL}")
            time.sleep(0.2)
        else:
            print(f"{Fore.RED}No data found for {country} in {year}.{Style.RESET_ALL}")

    @staticmethod
    def global_energy_insights():
        print(f"{Fore.CYAN}Global Energy Insights:{Style.RESET_ALL}")

        # Fetch global energy data
        global_data = EnergyModel.get_global_energy_data()

        if global_data:
            total_consumption, average_consumption, total_production, average_production = global_data

            print(f"\n{Fore.CYAN}For Energy Consumption:{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Total Global Consumption: {total_consumption}{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Average Global Consumption: {average_consumption}{Style.RESET_ALL}")
            time.sleep(0.2)

            print(f"\n{Fore.CYAN}For Energy Production:{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Total Global Production: {total_production}{Style.RESET_ALL}")
            time.sleep(0.2)
            print(f"{Fore.YELLOW}Average Global Production: {average_production}{Style.RESET_ALL}")
            time.sleep(0.2)
        else:
            print(f"{Fore.RED}No global energy data available.{Style.RESET_ALL}")

    @staticmethod
    def energy_compare_by_date_for_countries():
        # Get user input for date and countries
        year_to_compare = input(f"Enter the year to compare: ")
        countries_input = input(f"Enter the countries to compare (comma-separated): ")

        # Convert the input countries to a list
        selected_countries = [country.strip() for country in countries_input.split(',')]

        # Call the UserModel function to get the comparison results
        comparison_results = EnergyModel.energy_compare_by_date_for_countries(year_to_compare, selected_countries)

        # Display the results
        if comparison_results:
            print(f"\n{Fore.CYAN}Energy Comparison Results:{Style.RESET_ALL}")
            print("{:<15} {:<20} {:<20}".format("Country", "Total Consumption", "Total Production"))
            for result in comparison_results:
                country, total_consumption, total_production = result
                print("{:<15} {:<20} {:<20}".format(country, total_consumption, total_production))
        else:
            print(f"{Fore.RED}No data available for the specified date and countries.{Style.RESET_ALL}")
