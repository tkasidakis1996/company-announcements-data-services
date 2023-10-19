import requests

RESTful_API_network_address = input("Enter network address of the RESTful_API : ")


BASE_URL = "http://"+RESTful_API_network_address+":8000"  # Replace with the base URL of your running FastAPI application

# Test case to fetch company info for an existing GEMH
def test_get_existing_company_info():

    EXISTING_GEMH = "922301000"
    
    response = requests.get(f"{BASE_URL}/company/{EXISTING_GEMH}")
    
    assert response.status_code == 200
    
    data = response.json()
    
    assert data == {
        "Name": "ΖΩΗ ΛΕΥΚΟΦΡΥΔΟΥ ΙΔΙΩΤΙΚΗ ΚΕΦΑΛΑΙΟΥΧΙΚΗ ΕΤΑΙΡΙΑ",
        "GEMH": "922301000",
        "WebsiteName": "www.dimoprasiou.gr",
        "RegistrationDateWebsite": "21-03-2017"
    }

# Test case to handle non-existing GEMH
def test_get_non_existing_company_info():
    
    NON_EXISTING_GEMH = "123456789"
    
    response = requests.get(f"{BASE_URL}/company/{NON_EXISTING_GEMH}")
    
    assert response.status_code == 404
    
    data = response.json()
    
    assert data == {"detail": "Company not found"}
