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

def test_view_account_details(setup):
    driver = setup
    driver.get("http://your-fintech-application-url/account")
    
    assert "Account Details" in driver.page_source

def test_update_account_details(setup):
    driver = setup
    driver.get("http://your-fintech-application-url/account")
    driver.find_element_by_id("email").clear()
    driver.find_element_by_id("email").send_keys("newemail@example.com")
    driver.find_element_by_id("submit").click()
    
    assert "Account updated successfully" in driver.page_source
