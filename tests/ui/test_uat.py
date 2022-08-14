from selenium import webdriver
import time
import unittest

class TestBrowser(unittest.TestCase): 
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    port = 4444
    driver = webdriver.Remote(
            command_executor=f'http://localhost:{port}/wd/hub',
            options=options
        )   
        
    def test_home_page(self): 
        TestBrowser.driver.get("http://localhost:3001/")
        add_product_link = TestBrowser.driver.find_element_by_class_name("navbar-brand")
        assert add_product_link.text == "Add Product", "[+]Cannot able to get the Home Page"
    
    def test_products_panel_page(self): 
        TestBrowser.driver.get("http://localhost:3001/products-panel")
      #  a_tag = TestBrowser.driver.find_element_by_class_name("navbar-brand")
       # a_tag.click()
        time.sleep(10)
        home_link = TestBrowser.driver.find_element_by_class_name("navbar-brand")
        assert home_link.text == "Home", "[+]Product Page is not accessable"

    def test_creating_product_with_data(self): 
        TestBrowser.driver.get("http://localhost:3001/products-panel")
        time.sleep(10)
        number_of_rows_before = len(TestBrowser.driver.find_elements_by_class_name("tr"))
        add_button = TestBrowser.driver.find_element_by_class_name("btn")
        add_button.click()
        time.sleep(10)
        title_input = TestBrowser.driver.find_element_by_name("title")
        title_input.send_keys("Product1")
        time.sleep(10)
        image_input = TestBrowser.driver.find_element_by_name("image")
        image_input.send_keys("data:image/jpeg;base64,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")
        time.sleep(10)
        submit_button = TestBrowser.driver.find_element_by_class_name("submitButton")
        submit_button.click()
        time.sleep(10)
        number_of_rows_after = len(TestBrowser.driver.find_elements_by_class_name("tr"))
        assert number_of_rows_before + 1 == number_of_rows_after, "[+]Product creation is not working as excepted"
    
    def test_create_product_without_data(self):
        TestBrowser.driver.get("http://localhost:3001/products-panel")
        time.sleep(10)
        prod_add_button = TestBrowser.driver.find_element_by_class_name("btn")
        prod_add_button.click() 
        time.sleep(10)
        title_input = TestBrowser.driver.find_element_by_name("title")
        image_input = TestBrowser.driver.find_element_by_name("image")
        submit_button = TestBrowser.driver.find_element_by_class_name("submitButton")
        submit_button.click()
        time.sleep(10)
        assert TestBrowser.driver.find_element_by_name("title"), "[+]Server Accepts the Input without any data"

    def test_data_consistency(self): 
        TestBrowser.driver.get("http://localhost:3001/products-panel")
        time.sleep(10)
        number_of_rows_before = len(TestBrowser.driver.find_elements_by_class_name("tr"))
        add_button = TestBrowser.driver.find_element_by_class_name("btn")
        add_button.click()
        time.sleep(10)
        title_input = TestBrowser.driver.find_element_by_name("title")
        title_input.send_keys("Product1")
        time.sleep(10)
        image_input = TestBrowser.driver.find_element_by_name("image")
        image_input.send_keys("data:image/jpeg;base64,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")
        time.sleep(10)
        submit_button = TestBrowser.driver.find_element_by_class_name("submitButton")
        submit_button.click()
        time.sleep(10)
        number_of_rows_after = len(TestBrowser.driver.find_elements_by_class_name("tr"))
        #assert number_of_rows_before + 1 == number_of_rows_after, "[+]Product creation is not working as excepted"
        TestBrowser.driver.get("http://localhost:3001/")
        time.sleep(10)
        product_cols = len(TestBrowser.driver.find_elements_by_class_name("col-md-4"))
        assert product_cols == number_of_rows_after, "[+]Added Product in the product-panel, is not added in main page"

    def test_product_deletion(self): 
        TestBrowser.driver.get("http://localhost:3001/products-panel")
        time.sleep(10)
        number_of_rows_before = len(TestBrowser.driver.find_elements_by_class_name("tr"))
        del_button = TestBrowser.driver.find_element_by_class_name("deleteButton")
        first_pro_del_button = None
        if type(del_button) == list: 
            first_pro_del_button = del_button[0]
        else: 
            first_pro_del_button = del_button
        first_pro_del_button.click()
        time.sleep(10)
        alert = TestBrowser.driver.switch_to.alert.accept()
        time.sleep(10)
        number_of_rows_after = len(TestBrowser.driver.find_elements_by_class_name("tr"))
        assert number_of_rows_after == number_of_rows_before - 1, "[+]Deletion of the Product is not working"

 #   def test_edit_product_with_data(self): 
  #      TestBrowser.driver.get("http://localhost:3001/products-panel")
   #     time.sleep(10)
    #    add_button = TestBrowser.driver.find_element_by_class_name("btn")
     #   add_button.click()
      #  time.sleep(10)
       # title_input = TestBrowser.driver.find_element_by_name("title")
      #  title_input.send_keys("Product_for_edit_with_data")
       # time.sleep(10)
       # image_input = TestBrowser.driver.find_element_by_name("image")
       # image_input.send_keys("data:image/jpeg;base64,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")
       # time.sleep(10)
       # submit_button = TestBrowser.driver.find_element_by_class_name("submitButton")
       # submit_button.click()
       # time.sleep(10)
       # no_of_rows = len(TestBrowser.driver.find_elements_by_class_name("tr"))
       # time.sleep(10)
       # title_of_first_product_before = TestBrowser.driver.find_element_by_xpath(f'//table/tbody/tr[{no_of_rows}]/td[3]').text
       # edit_button = TestBrowser.driver.find_element_by_class_name("editButton")
       # edit_button.click()
        # time.sleep(10)
        # title_input = TestBrowser.driver.find_element_by_name("title")
        # title_input.send_keys("Product_title_changed")
        # time.sleep(10)
        # save_btn = TestBrowser.driver.find_element_by_class_name("SaveButtonInEdit")
        # save_btn.click()
        # time.sleep(10)
        # title_of_first_product_after = TestBrowser.driver.find_element_by_xpath(f'//table/tbody/tr[{no_of_rows}]/td[3]').text
        # assert title_of_first_product_before != title_of_first_product_after and title_of_first_product_after == "Product_title_changed", "There is an error in Product details editing"
    
    def test_product_like_check(self): 
        TestBrowser.driver.get("http://20.219.112.96:3001/")
        time.sleep(10)
        first_prod_number_of_likes_before = TestBrowser.driver.find_element_by_class_name("text-muted")
        if type(first_prod_number_of_likes_before) == list:
            first_prod_number_of_likes_before = first_prod_number_of_likes_before[0]/text
        else: 
            first_prod_number_of_likes_before = first_prod_number_of_likes_before.text

        like_button = TestBrowser.driver.find_element_by_class_name("likeButton")
        like_button.click()
        time.sleep(10)
        first_prod_number_of_likes_after = first_prod_number_of_likes_before = TestBrowser.driver.find_element_by_class_name("text-muted")         
        if type(first_prod_number_of_likes_after) == list:
            first_prod_number_of_likes_after = first_prod_number_of_likes_after[0].text
        else: 
            first_prod_number_of_likes_after = first_prod_number_of_likes_after.text
        TestBrowser.driver.get("http://20.219.112.96:3001/products-panel")
        time.sleep(10)
        first_prod_likes_in_productspanels_page = TestBrowser.driver.find_element_by_xpath('//table/tbody/tr/td[4]').text
        if type(first_prod_likes_in_productspanels_page) == list:
            first_prod_likes_in_productspanels_page = first_prod_likes_in_productspanels_page[0]
        else: 
            first_prod_likes_in_productspanels_page = first_prod_likes_in_productspanels_page
        assert first_prod_likes_in_productspanels_page == first_prod_number_of_likes_after.split(" ")[0], "[+]Liking a product is not affecting"


    def test_tear_down(self): 
        TestBrowser.driver.close()
        TestBrowser.driver.quit()
    

