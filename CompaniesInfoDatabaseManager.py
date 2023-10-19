import mysql.connector
import json

class CompaniesInfoDatabaseManager:
    """
    A class for managing a MySQL database and storing companies' information.

    attributes:
        db_address (str): The database server address.
        user_name (str): The MySQL user's username.
        password (str): The MySQL user's password.
        initial_connection_with_the_database_system: Initial connection to the database server.
        initial_cursor: Cursor for initial database operations.
        connection_with_the_specific_database_for_the_companies: Connection to the specific company database.
        cursor_for_database_operations: Cursor for company database operations.
    """

    def __init__(self, db_address, user_name, password):
        """
        Initializes the CompaniesInfoDatabaseManager.

        args:
            db_address (str): The database server address.
            user_name (str): The MySQL user's username.
            password (str): The MySQL user's password.
        """

        self.database_address = db_address
        
        self.user_name = user_name
        
        self.password = password
        
        self.initial_connection_with_the_database_system = mysql.connector.connect(
            host=db_address, user=user_name, password=password
        )
        
        self.initial_cursor = self.initial_connection_with_the_database_system.cursor()
        
        self.connection_with_the_specific_database_for_the_companies = None
        
        self.cursor_for_database_operations = None

    def create_database(self, db_name):
        """
        Creates a new database and connects to it.

        args:
            db_name (str): The name of the database to be created and connected to.
        """

        self.initial_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        
        self.connection_with_the_specific_database_for_the_companies = mysql.connector.connect(
            host=self.database_address, user=self.user_name, password=self.password, database=db_name
        )
        
        self.cursor_for_database_operations = self.connection_with_the_specific_database_for_the_companies.cursor()
        
        self.initial_cursor.close()
        
        self.initial_connection_with_the_database_system.close()

    def run(self):
        """
        Run the database manager to create a table and save companies information.
        """

        self.create_table_for_the_companies_info()
        
        companies_info = self.read_companies_info_from_the_relative_file()
        
        self.save_companies_info_to_the_respective_table_at_the_database(companies_info)

    def create_table_for_the_companies_info(self):
        """
        Creates a table for storing companies information in the database.
        """

        self.cursor_for_database_operations.execute("CREATE TABLE Companies (GEMH VARCHAR(255) PRIMARY KEY, Name VARCHAR(255), WebsiteName VARCHAR(255), RegistrationDateWebsite VARCHAR(255))")

    def read_companies_info_from_the_relative_file(self):
        """
        Reads companies information from the respective file.

        returns:
            list: A list of dictionaries containing companies information.
        """

        file_path = 'companies_info.json'
        
        with open(file_path, 'r', encoding='utf-8') as file:
            all_companies_info = json.load(file)
        
        return all_companies_info

    def save_companies_info_to_the_respective_table_at_the_database(self, all_companies_info):
        """
        Saves companies information to the database table.

        args:
            all_companies_info (list): A list of dictionaries containing companies information.
        """

        SQL_command_for_the_data_insertion = "INSERT INTO Companies (GEMH, Name, WebsiteName, RegistrationDateWebsite) VALUES (%s, %s, %s, %s)"
        
        for company_info in all_companies_info:
            company_data_for_storage = (
                company_info["GEMH"], company_info["Name"],
                company_info["WebsiteName"], company_info["RegistrationDateWebsite"]
            )

            
            self.cursor_for_database_operations.execute(SQL_command_for_the_data_insertion, company_data_for_storage)
            
            self.connection_with_the_specific_database_for_the_companies.commit()
