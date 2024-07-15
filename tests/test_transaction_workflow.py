import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get("http://your-fintech-application-url/login")
    driver.find_element_by_id("username").send_keys("user")
    driver.find_element_by_id("password").send_keys("password")
    driver.find_element_by_id("login").click()
    yield driver
    driver.quit()

def test_valid_transaction(setup):
    driver = setup
    driver.get("http://your-fintech-application-url/transaction")
    driver.find_element_by_id("amount").send_keys("100")
    driver.find_element_by_id("submit").click()
    
    assert "Transaction successful" in driver.page_source

def test_invalid_transaction(setup):
    driver = setup
    driver.get("http://your-fintech-application-url/transaction")
    driver.find_element_by_id("amount").send_keys("-100")
    driver.find_element_by_id("submit").click()
    
    assert "Invalid transaction" in driver.page_source
