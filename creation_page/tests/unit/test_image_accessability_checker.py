import unittest
from server.image_accessability_checker import is_image_accessable

class ImageTest(unittest.TestCase): 
    def test_failure_check(self): 
        self.assertFalse(is_image_accessable(""), "Image can be accessed")

    def test_success_check(self): 
        self.assertTrue(is_image_accessable("https://google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Feb%2Fe4%2Fa3%2Febe4a37984a8745e78555906765df486.jpg&imgrefurl=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F553520610457129852%2F&tbnid=lBKFVUo3pH7-DM&vet=12ahUKEwi84sewxpj5AhUc_jgGHSUrAIQQxiAoAXoECAAQGQ..i&docid=mpMTXORMJblJOM&w=1080&h=1080&itg=1&q=images&ved=2ahUKEwi84sewxpj5AhUc_jgGHSUrAIQQxiAoAXoECAAQGQ"), "Image cannot be accessed")

