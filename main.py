import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase): #a sample test class to show how page object works

    def setUp(self):
        print("setup")
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.python.org")

    def test_search_in_python_org(self): 
        '''Tests python.org search feature. It searches for the word "pycon" then
        verifies that some results show up.  Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty.'''
        main_page = page.MainPage(self.driver) #Load the main page. In this case the home page of python.org. 
        #checks if the word pycon is in the title 
        self.assertTrue(main_page.is_title_matches(), "python.org title doesn't match")
        #sets the text of the search testbox to "pycon"
        main_page.search_text_elememt = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty 
        self.assertTrue(search_results_page.is_results_found(), "No Results found.")

        def tearDown(self):
            self.driver.close()

    #     print("test")
    #     assert False 
    
    # def test2_example(self):
    #     print("test")
    #     assert True
    
    # def not_a_test(self):
    #     print("not a test")

    # def test_title(self):
    #     mainPage = page.MainPage()
    #     assert is_title_matches()

    # def tearDown(self):
    #     self.driver.close()

if __name__ == "__main__":
    unittest.main()