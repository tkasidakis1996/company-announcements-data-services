from pydantic import BaseModel

class CompanyInfoResponse(BaseModel):
	Name : str
	GEMH : str
	WebsiteName : str
	RegistrationDateWebsite : str