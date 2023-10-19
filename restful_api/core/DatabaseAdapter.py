import mysql.connector

from exceptions.CompanyNotFoundException import CompanyNotFoundException

class DatabaseAdapter:
    """
    DatabaseAdapter class for connecting to and querying a MySQL database.
    """

    def __init__(self, database_address, user_name, password, database_name):
        """
        Initialize the DatabaseAdapter.

        args:
            database_address (str): The network address of the database.
            user_name (str): The username for the database connection.
            password (str): The password for the database connection.
            database_name (str): The name of the database to connect to.
        """

        self.database_connection = mysql.connector.connect(
            host=database_address,
            user=user_name,
            password=password,
            database=database_name
        )

        self.cursor_for_the_database_operations = self.database_connection.cursor(dictionary=True)

    def get_company_info(self, GEMH):
        """
        Retrieve company information based on the GEMH number.

        args:
            GEMH (str): The GEMH number of the company to retrieve.

        returns:
            dict: A dictionary containing the company information.

        raises:
            CompanyNotFoundException: If the company with the provided GEMH number is not found.
        """

        SQL_command_for_loading_company_data_based_on_GEMH = "SELECT * FROM Companies WHERE GEMH = %s"

        self.cursor_for_the_database_operations.execute(SQL_command_for_loading_company_data_based_on_GEMH, (GEMH,))

        # Fetch the result
        info_of_a_company_from_the_database = self.cursor_for_the_database_operations.fetchall()

        if info_of_a_company_from_the_database == []:
            raise CompanyNotFoundException("Company with this GEMH number doesn't exist")

        data_of_a_company = info_of_a_company_from_the_database[0]

        return data_of_a_company
