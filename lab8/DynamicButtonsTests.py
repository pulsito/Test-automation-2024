from DynamicButtonsPages import SearchHelper
from selenium import webdriver
import pytest

class TestsDynamicButtons:
    def test_all_buttons(self, driver):
        page = SearchHelper(driver)
        page.go_to_site()
        page.click_button_start()
        page.click_button_one()
        page.click_button_two()
        page.click_button_three()
        msg = page.check_button_message()
        print(msg)
        assert page.check_button_message() == "All Buttons Clicked"
