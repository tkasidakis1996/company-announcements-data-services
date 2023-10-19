import os

import re

import json

class ParserCompaniesFiles():
    """A class to parse text files (refering to companies) in order to extract specific information (company's name, GEMH number,
    company's website name and the registration date of its website."""

    def __init__(self):
        """Initialize the patterns used for extracting information from text files."""

        self.name_patterns = [
            r"εταιρείας με επωνυμία «([^»]+)»",
            r"της εταιρείας με την επωνυμία «([^»]+)»",
            r"επωνυμία ([^,]+)",
            r"ΕΠΩΝΥΜΙΑ: (.+)",
            r"την επωνυμία ([^,]+) και αριθμό ΓΕΜΗ",
            r"επωνυμία ([^ ]+ .+ ΙΚΕ)",
        ]

        self.gemh_patterns = [
            r"Aριθμός ΓΕΜΗ: (\d+)",
            r"Γ\.Ε\.Μ\.Η\. (\d+)",
            r"Γ\.Ε\.Μ\.Η. (\d+)",
            r"ΓΕΜΗ\. (\d+)",
            r"ΓΕΜΗ (\d+)",
            r"Γ\.Ε\.ΜΗ\. (\d+)",
            r"Γ\.Ε\.ΜΗ (\d+)",
            r"Γ.Ε.ΜΗ. (\d+)",
        ]

        self.website_patterns = [r"Ιστοσελίδα: (\S+)", r"ιστοσελίδας ([^ ]+)"]

        self.registration_date_website_patterns = [
            r"Την (\d{1,2}-\d{1,2}-\d{4}) καταχωρήθηκε",
            r"Την (\d{1,2}/\d{1,2}/\d{4}) καταχωρήθηκε|\d{1,2}/\d{2}/(\d{4})"
        ]

    def run(self):
        """Parse text files and extract company information, then store it in a JSON file."""
        
        names_of_the_txt_files = self.get_names_of_the_txt_files()
        
        all_comapnies_info = []
        
        GEMH_numbers_appeared = []

        for txt_fname in names_of_the_txt_files:
            
            txt_file_contents = self.read_txt_file_contents(txt_fname)
            
            company_name = self.extract_company_name(txt_file_contents)
            
            GEMH = self.extract_GEMH_number(txt_file_contents)
            
            website_name = self.extract_website_name(txt_file_contents)
            
            registration_date_website = self.extract_registration_date_of_the_website(txt_file_contents)

            if GEMH in GEMH_numbers_appeared:
                continue

            GEMH_numbers_appeared.append(GEMH)
            
            info_for_one_company = {
                "Name": company_name,
                "GEMH": GEMH,
                "WebsiteName": website_name,
                "RegistrationDateWebsite": registration_date_website
            }

            all_comapnies_info.append(info_for_one_company)

        self.remove_newline_characters_from_companies_info(all_comapnies_info)
        
        self.make_all_websites_registration_date_in_the_same_format(all_comapnies_info)
        
        self.create_output_file_with_the_extracted_info_for_the_companies(all_comapnies_info)

    def get_names_of_the_txt_files(self):
        """
        Get the names of text files in the current directory.

        returns:
            list: A list of text file names.
        """

        desired_directory = os.path.dirname(os.path.abspath(__file__))
        
        txt_files_names = []

        for filename in os.listdir(desired_directory):
            
            if filename.endswith(".txt"):
                
                txt_files_names.append(filename)
        
        return txt_files_names

    def read_txt_file_contents(self, file_name):
        """
        Read the contents of a text file.

        args:
            file_name (str): The name of the text file to read.

        returns:
            str: The contents of the text file.
        """

        fd = open(file_name, "r")
        
        txt_file_contents = fd.read()
        
        fd.close()
        
        return txt_file_contents

    def extract_company_name(self, text):
        """
        Extract the company name from the given text.

        args:
            text (str): The text to search for the company name.

        returns:
            str: The extracted company name.
        """

        for name_pattern in self.name_patterns:
            
            name_match = re.search(name_pattern, text)
            
            if name_match:
                
                company_name = name_match.group(1).strip()
                
                company_name = re.split(r'και|,', company_name)[0].strip()
                
                break

        return company_name

    def extract_GEMH_number(self, text):
        """
        Extract the GEMH number from the given text.

        args:
            text (str): The text to search for the GEMH number.

        returns:
            str: The extracted GEMH number.
        """
        
        for gemh_pattern in self.gemh_patterns:
            
            gemh_match = re.search(gemh_pattern, text)
            
            if gemh_match:
                break
        
        GEMH_number = gemh_match.group(1)
        
        return GEMH_number

    def extract_website_name(self, text):
        """
        Extract the company's website name from the given text.

        args:
            text (str): The text to search for the website name.

        returns:
            str: The extracted website name or "NULL" if not found.
        """
        
        for website_pattern in self.website_patterns:
            
            website_match = re.search(website_pattern, text)
            
            if website_match:
                break
        
        if website_match:
            website_name = website_match.group(1)
        else:
            website_name = "NULL"
        
        return website_name

    def extract_registration_date_of_the_website(self, text):
        """
        Extract the registration date of the website from the given text.

        args:
            text (str): The text to search for the registration date.

        returns:
            str: The extracted registration date.
        """

        for registration_date_website_pattern in self.registration_date_website_patterns:
            
            registration_date_website_match = re.search(registration_date_website_pattern, text)
            
            if registration_date_website_match:
                break
        
        registration_date_website = registration_date_website_match.group(1)
        
        return registration_date_website

    def remove_newline_characters_from_companies_info(self, info_of_all_companies):
        """
        Remove newline characters from companies information.

        args:
            info_of_all_companies (list of dict): List of dictionaries containing companies information.
        """

        for company_info in info_of_all_companies:
            
            for key, value in company_info.items():
                
                company_info[key] = value.replace('\n', '')

    def make_all_websites_registration_date_in_the_same_format(self, info_of_all_companies):
        """
        Convert all website registration dates to the same format (dd-mm-yyyy).

        args:
            info_of_all_companies (list of dict): List of dictionaries containing companies information.
        """

        for company_info in info_of_all_companies:
            
            company_info['RegistrationDateWebsite'] = company_info['RegistrationDateWebsite'].replace('/', '-')

    def create_output_file_with_the_extracted_info_for_the_companies(self, info_of_all_companies):
        """
        Create an output JSON file with the extracted companies information.

        args:
            info_of_all_companies (list of dict): List of dictionaries containing companies information.
        """
        
        json_file_path = 'companies_info.json'
        
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(info_of_all_companies, json_file, ensure_ascii=False, indent=4)