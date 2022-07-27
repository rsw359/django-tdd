import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@pytest.mark.selenium
def test_dashboard_admin_login(live_server, chrome_browser_instance):

  browser = chrome_browser_instance

  browser.get(("%s%s" % (live_server.url, "/admin/login/")))

  user_name = browser.find_element(By.NAME, "username")#finds input element on the page, find by inspecting
  user_password = browser.find_element(By.NAME, "password")#finds input element on the page, find by inspecting
  submit = browser.find_element(By.XPATH, '//input[@value="Log in"]')  #this element is a button

  user_name.send_keys("admin")
  user_password.send_keys("admin")
  submit.send_keys(Keys.RETURN)

  assert "Site administration" in browser.page_source
