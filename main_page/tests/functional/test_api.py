import sys, os, json
import unittest
from main import app


client = app.test_client()


class ApiTesting(unittest.TestCase): 
    def test_home_page_success_status_code(self): 
        res = client.get("/")
        status_code = res.status_code
        assert status_code == 404, "Home page is accessable"

    def test_creation_page_items_get_method_status_code(self): 
        res = client.get("/main-page/api/items")
        status_code = res.status_code 
        assert status_code in [200, 500],  "Creation page items route is not working"
    
    def test_creation_page_items_get_method_content_type(self): 
        res = client.get("/main-page/api/items")
        content_type = res.content_type 
        assert content_type == "application/json", "Creation page items route is not returning json"

    def test_creation_page_items_get_method_return_value(self): 
        res = client.get("/main-page/api/items")
        res = json.loads(res.get_data(as_text=True))
        assert type(res) == dict, "Return value is not dictionary!!"


    