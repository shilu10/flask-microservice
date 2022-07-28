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
        res = client.get("/creation-page/api/items")
        print(res.get_data())
        status_code = res.status_code 
        assert status_code in [200, 500],  "Creation page items route is not working"
    
    def test_creation_page_items_get_method_content_type(self): 
        res = client.get("/creation-page/api/items")
        content_type = res.content_type 
        assert content_type == "application/json", "Creation page items route is not returning json"

    def test_creation_page_items_get_method_return_value(self): 
        res = client.get("/creation-page/api/items")
        res = json.loads(res.get_data(as_text=True))
        assert type(res) == dict, "Return value is not dictionary!!"
    
    def test_creation_page_create_items_method_wrong_content_type(self): 
        post_data = {"data": "wrong content type"}
        content_type = "multipart/form"
        res = client.post("/creation-page/api/create-item", data = post_data, headers={'Content-Type': content_type})
        assert res.status_code == 500, "It accepts the different content type, The behaviour should'nt be that"

    def test_creation_page_create_items_method_wrong_data(self): 
        post_data = {"title": "testing", "photo": ""}
        content_type = "application/json"
        res = client.post("/creation-page/api/create-item", data = post_data, headers={'Content-Type': content_type})
        assert res.status_code == 400, "Create Method accepts the wrong data"

    def test_creation_page_single_item_get_method(self): 
        res = client.get("/creation-page/api/items/1")
        print(res.get_data())
        assert res.status_code == 200, "Single Item get method is not working"