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
     
       
def test_view_reports(setup):
    driver = setup
    driver.get("http://your-fintech-application-url/reports")
    
    assert "Reports" in driver.page_source

def test_generate_report(setup):
    driver = setup
    driver.get("http://your-fintech-application-url/reports")
    driver.find_element_by_id("generate").click()
    
    assert "Report generated successfully" in driver.page_source
