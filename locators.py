#any css selector or any id or any way that we locate the element, we must keep in one centralized location

from selenium.webdriver.common.by import By

class MainPageLocators(object): #a class for main page locator. all the main page locators must come here
    GO_BUTTON = (By.ID, "submit")

class SearchResultsPageLocators(object): #a class for search results locators. All search results locators should come here
    pass 