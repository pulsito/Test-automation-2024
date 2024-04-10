from selenium.webdriver.common.by import By

from BaseApp import BasePage


class DynamicButtonsLocators:
    LOCATOR_BUTTON_START = (By.ID, "button00")
    LOCATOR_BUTTON_ONE = (By.ID, "button01")
    LOCATOR_BUTTON_TWO = (By.ID, "button02")
    LOCATOR_BUTTON_THREE = (By.ID, "button03")
    LOCATOR_BUTTON_MESSAGE = (By.ID, "buttonmessage")


class SearchHelper(BasePage):
    def click_button_start(self):
        return self.find_element(DynamicButtonsLocators.LOCATOR_BUTTON_START).click()

    def click_button_one(self):
        return self.find_element(DynamicButtonsLocators.LOCATOR_BUTTON_ONE).click()

    def click_button_two(self):
        return self.find_element(DynamicButtonsLocators.LOCATOR_BUTTON_TWO).click()

    def click_button_three(self):
        return self.find_element(DynamicButtonsLocators.LOCATOR_BUTTON_THREE).click()

    def check_button_message(self):
        return self.find_element(DynamicButtonsLocators.LOCATOR_BUTTON_MESSAGE).text
