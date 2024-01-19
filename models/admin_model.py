import sqlite3

class AdminModel:
    @staticmethod
    def get_all_user():
        with sqlite3.connect('C:\\Users\\bhara\\OneDrive\\Desktop\\Gokul\\EnergyInsight\\Energy_Insight_App\\databases\\user_database.sqlite') as conn_user:
            cursor_user = conn_user.cursor()
            cursor_user.execute('SELECT * FROM users')
            users = cursor_user.fetchall()

        return users

    @staticmethod
    def delete_user(user_name):
        connection = sqlite3.connect('C:\\Users\\bhara\\OneDrive\\Desktop\\Gokul\\EnergyInsight\\Energy_Insight_App\\databases\\user_database.sqlite')
        cursor = connection.cursor()

        try:
            cursor.execute("DELETE FROM users WHERE UserName = ?", (user_name,))
            connection.commit()
            print(f"User {user_name} deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting user: {e}")
        finally:
            connection.close()

    @staticmethod
    def get_user_by_name(user_name):
        with sqlite3.connect('C:\\Users\\bhara\\OneDrive\\Desktop\\Gokul\\EnergyInsight\\Energy_Insight_App\\databases\\user_database.sqlite') as conn_user:
            cursor_user = conn_user.cursor()
            cursor_user.execute("SELECT * FROM users WHERE UserName = ?", (user_name,))
            user_data = cursor_user.fetchone()
            return user_data

    @staticmethod
    def get_admin_by_name(admin_name, password):
        with sqlite3.connect('C:\\Users\\bhara\\OneDrive\\Desktop\\Gokul\\EnergyInsight\\Energy_Insight_App\\databases\\admin_database.sqlite') as conn_admin:
            cursor_admin = conn_admin.cursor()
            cursor_admin.execute("SELECT * FROM admins WHERE admin_name = ? AND password = ?", (admin_name, password))

        user = cursor_admin.fetchone()
        return user
    
    @staticmethod
    def create_admin(admin_name, password):
        # Insert new admin data
        with sqlite3.connect('C:\\Users\\bhara\\OneDrive\\Desktop\\Gokul\\EnergyInsight\\Energy_Insight_App\\databases\\admin_database.sqlite') as conn_admin:
            cursor_admin = conn_admin.cursor()

            try:
                cursor_admin.execute("INSERT INTO admins (admin_name, password) VALUES (?, ?)", (admin_name, password))
                print("\nAdmin registered successfully.")
            except sqlite3.IntegrityError:
                print("\nAdmin already exists. Please choose a different one.")
