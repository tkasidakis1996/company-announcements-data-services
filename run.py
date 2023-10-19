import logging

from ParserCompaniesFiles import ParserCompaniesFiles

from CompaniesInfoDatabaseManager import CompaniesInfoDatabaseManager

if __name__ == "__main__":

	log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    logging.basicConfig(format=log_format, level=logging.DEBUG)

	parser = ParserCompaniesFiles()

	parser.run()

	logging.info("Output file (companies_info.json) created successfully")

	print(80*"-")

	database_address = input("Enter the network address of the database : ")

	print(80*"-")

	user = input("Enter name of the user (for example root) : ")

	print(80*"-")

	password = input("Enter password in order to connect with the database : ")

	print(80*"-")
	
	db_manager_for_companies_data = CompaniesInfoDatabaseManager(database_address, user, password)

	print(80*"-")

	logging.info("Successfully connected with the database")

	print(80*"-")

	database_name = input("Enter a name for the database in order to be created : ")

	db_manager_for_companies_data.create_database(database_name)

	logging.info("After the creation of the database with the desired name, a table will be created.")
	
	logging.info("The table will be called [Companies].")

	logging.info("The data from the companies_info.json will be parsed and will be stored appropriately to the Companies table")

	db_manager_for_companies_data.run()

	logging.info("Data saved successfully to the database")



