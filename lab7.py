from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_task_1(driver):
    driver.get("https://testpages.eviltester.com/styled/dynamic-buttons-simple.html")
    start_button = driver.find_element(By.XPATH, "//button[text()='start']")
    start_button.click()
    one_button = driver.find_element(By.XPATH, "//button[text()='One']")
    one_button.click()
    time.sleep(5)
    assert driver.find_element(By.XPATH, "//button[text()='Two']").is_displayed()


def test_task_2(driver):
    driver.get("https://testpages.eviltester.com/styled/dynamic-buttons-simple.html")
    start_button = driver.find_element(By.XPATH, "//button[text()='start']")
    start_button.click()
    one_button = driver.find_element(By.XPATH, "//button[text()='One']")
    one_button.click()
    driver.implicitly_wait(10)
    assert driver.find_element(By.XPATH, "//button[text()='Two']").is_displayed()


def test_task_3(driver):
    driver.get("https://testpages.eviltester.com/styled/dynamic-buttons-simple.html")
    start_button = driver.find_element(By.XPATH, "//button[text()='start']")
    start_button.click()
    one_button = driver.find_element(By.XPATH, "//button[text()='One']")
    one_button.click()
    assert WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Two']"))
    )



