from element import BasePageElement
from locators import MainPageLocators


class SearchTextElement(BasePageElement): '''this file gets the search text from the specified locator'''

#the locator for the search box where search string is entered

locator = "q"

class BasePage(object): #base class to initialize the base page that will be called from for all our pages



    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage): #home page action method comes here. i.e.python.org
    
    search_text_element = SearchTextElement()


    def is_title_matches(self): #this method tells us if the title of the web pages matches what we want it to match
        return "Python" in self.driver.title #if python is currently in the title of webpage the driver is currently on
    

    def click_go_button(self): #trigger the search
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()     

class SearchResultsPage(BasePage): #search results page action methods comes here
    def is_results_found(self): #probably should search for this text in the specific text 
        #element, but as far now it works
        return "No results found." not in self.driver.page_source