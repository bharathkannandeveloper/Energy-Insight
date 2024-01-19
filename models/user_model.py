# user_model.py
import sqlite3

class EnergyModel:

    def energy_compare_by_date_for_countries(date_to_compare, selected_countries):
        with sqlite3.connect('C:\\Users\\bhara\\OneDrive\\Desktop\\Gokul\\EnergyInsight\\Energy_Insight_App\\databases\\energy_database.sqlite') as conn:
            cursor = conn.cursor()

            # Construct the SQL query to get the energy consumption and production for selected countries on the specified date
            query = '''
                SELECT
                    country,
                    SUM(coal_consumption) AS total_consumption,
                    SUM(coal_production) AS total_production
                FROM energy_cleaned_data
                WHERE year = ? AND country IN ({})
                GROUP BY country
            '''.format(', '.join(['?']*len(selected_countries)))

            # Execute the query with the date and selected countries as parameters
            cursor.execute(query, [date_to_compare] + selected_countries)

            # Fetch the results
            comparison_results = cursor.fetchall()

        return comparison_results

    @staticmethod
    def get_energy_summary(country):
        with sqlite3.connect('C:\\Users\\bhara\\OneDrive\\Desktop\\Gokul\\EnergyInsight\\Energy_Insight_App\\databases\\energy_database.sqlite') as conn_energy:
            cursor_energy = conn_energy.cursor()
            cursor_energy.execute('''
                 SELECT
                    COALESCE(SUM(coal_consumption), 0) AS total_consumption,
                    COALESCE(AVG(coal_consumption), 0) AS average_consumption,
                    COALESCE(MIN(coal_consumption), 0) AS min_consumption,
                    COALESCE(MAX(coal_consumption), 0) AS max_consumption,
                    COALESCE(SUM(coal_production), 0) AS total_production,
                    COALESCE(AVG(coal_production), 0) AS average_production,
                    COALESCE(MIN(coal_production), 0) AS min_production,
                    COALESCE(MAX(coal_production), 0) AS max_production             
                FROM energy_cleaned_data
                WHERE country = ?
            ''', (country,))

            energy_summary = cursor_energy.fetchone()
            return energy_summary
    
    def get_energy_data_by_year(country, year):
        with sqlite3.connect('C:\\Users\\bhara\\OneDrive\\Desktop\\Gokul\\EnergyInsight\\Energy_Insight_App\\databases\\energy_database.sqlite') as conn_energy:
            cursor_energy = conn_energy.cursor()
            cursor_energy.execute('''
                SELECT
                    population,
                    coal_consumption,
                    coal_production,
                    oil_consumption,
                    oil_production,
                    gas_consumption,
                    gas_production
                FROM energy_cleaned_data
                WHERE country = ? AND year = ?
            ''', (country, year))

            energy_data = cursor_energy.fetchone()
            return energy_data
        
    def get_global_energy_data():
        with sqlite3.connect('C:\\Users\\bhara\\OneDrive\\Desktop\\Gokul\\EnergyInsight\\Energy_Insight_App\\databases\\energy_database.sqlite') as conn_energy:
            cursor_energy = conn_energy.cursor()
            cursor_energy.execute('''
                SELECT
                    SUM(coal_consumption) AS total_consumption,
                    AVG(coal_consumption) AS average_consumption,
                    SUM(coal_production) AS total_production,
                    AVG(coal_production) AS average_production
                FROM energy_cleaned_data
            ''')

            global_data = cursor_energy.fetchone()
            return global_data    
class UserModel:
    
    @staticmethod
    def get_user_by_name(user_name,password):
        
        with sqlite3.connect('C:\\Users\\bhara\\OneDrive\\Desktop\\Gokul\\EnergyInsight\\Energy_Insight_App\\databases\\user_database.sqlite') as conn_user:
            cursor_user = conn_user.cursor()
            cursor_user.execute('''
                SELECT * FROM users
                WHERE UserName = ? AND Password = ?
            ''', (user_name, password))

        user = cursor_user.fetchone()

        return user
    
    
    
    def create_user( user_name, password, email, country):
        

        # Insert new user data
        with sqlite3.connect('C:\\Users\\bhara\\OneDrive\\Desktop\\Gokul\\EnergyInsight\\Energy_Insight_App\\databases\\user_database.sqlite') as conn_user:
            cursor_user = conn_user.cursor()

            try:
                cursor_user.execute('''
                    INSERT INTO users (UserName, Password, Email, Country)
                    VALUES (?, ?, ?, ?)
                ''', (user_name, password, email, country))
                print("\nUser registered successfully.")
            except sqlite3.IntegrityError:
                print("\nUsername already exists. Please choose a different one.")

    def update_password(user_name, new_password):
        # Update user password
        connection = sqlite3.connect('C:\\Users\\bhara\\OneDrive\\Desktop\\Gokul\\EnergyInsight\\Energy_Insight_App\\databases\\user_database.sqlite')
        cursor = connection.cursor()

        cursor.execute("UPDATE users SET Password = ? WHERE UserName = ?", (new_password, user_name))

        connection.commit()
        connection.close()

    def update_email(user_name, new_email):
        # Update user email
        connection = sqlite3.connect('C:\\Users\\bhara\\OneDrive\\Desktop\\Gokul\\EnergyInsight\\Energy_Insight_App\\databases\\user_database.sqlite')
        cursor = connection.cursor()

        cursor.execute("UPDATE users SET Email = ? WHERE UserName = ?", (new_email, user_name))

        connection.commit()
        connection.close()

    def update_country(user_name, new_country):
        # Update user country
        connection = sqlite3.connect('C:\\Users\\bhara\\OneDrive\\Desktop\\Gokul\\EnergyInsight\\Energy_Insight_App\\databases\\user_database.sqlite')
        cursor = connection.cursor()

        cursor.execute("UPDATE users SET Country = ? WHERE UserName = ?", (new_country, user_name))

        connection.commit()
        connection.close()     
     

# You may have additional methods here, such as fetching user data from the database.
