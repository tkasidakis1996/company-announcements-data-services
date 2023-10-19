import logging

from DatabaseAdapter import DatabaseAdapter

from RESTful_API import RESTful_API


if __name__ == "__main__":

    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    logging.basicConfig(format=log_format, level=logging.DEBUG)

    print(80 * "-")
    
    database_address = input("Enter the network address of the database: ")
    
    print(80 * "-")

    user = input("Enter name of the user (for example root): ")

    print(80 * "-")
    
    password = input("Enter password in order to connect with the database: ")
    
    print(80 * "-")

    database_name = input("Enter the name of the database: ")

    print(80 * "-")

    print("")

    database = DatabaseAdapter(database_address, user, password, database_name)

    logging.info("Successfully connected with the database")

    print("")

    restful_api = RESTful_API(database)
    
    restful_api.run()
