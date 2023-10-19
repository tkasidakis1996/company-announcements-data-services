from fastapi import FastAPI, HTTPException
import uvicorn

from models.response_models import CompanyInfoResponse

from DatabaseAdapter import DatabaseAdapter

from exceptions.CompanyNotFoundException import CompanyNotFoundException

class RESTful_API():
    """
    RESTful API class for retrieving company information based on GEMH number.
    """

    def __init__(self, database):
        """
        Initialize the RESTful_API object.

        args:
            database (DatabaseAdapter): An instance of DatabaseAdapter for connecting to the database.
        """

        self.app = FastAPI()
        
        self.database = database

        self.app.add_api_route(
            path="/company/{gemh_number}",
            endpoint=self.get_company_info,
            methods=["GET"],
            response_model=CompanyInfoResponse,
            name="get_company_info",
        )

    def run(self):
        """
        Start the FastAPI server to run the RESTful API.
        """

        uvicorn.run(self.app, host="0.0.0.0", port=8000)

    def get_company_info(self, gemh_number: str):
        """
        Retrieve company information for a given GEMH number.

        args:
            gemh_number (str): The GEMH number of the company.

        returns:
            CompanyInfoResponse: The company information response.
        
        raises:
            HTTPException: If the company is not found, a 404 error is raised.
        """
        try:
            company_data = self.database.get_company_info(gemh_number)
        
        except CompanyNotFoundException:
            raise HTTPException(status_code=404, detail="Company not found")

        response = CompanyInfoResponse(
            Name=company_data["Name"],
            GEMH=company_data["GEMH"],
            WebsiteName=company_data["WebsiteName"],
            RegistrationDateWebsite=company_data["RegistrationDateWebsite"],
        )

        return response
