import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User

# @pytest.mark.selenium
# def test_create_new_admin_user(create_admin_user):
#   assert create_admin_user.__str__() == "tester"

@pytest.mark.selenium
def test_dashboard_admin_login(live_server, db_fixture_setup, chrome_browser_instance):

  i = User.objects.get(id=1)
  print(i.password)

  browser = chrome_browser_instance

  browser.get(("%s%s" % (live_server.url, "/admin/login/")))

  user_name = browser.find_element(By.NAME, "username")#finds input element on the page, find by inspecting
  user_password = browser.find_element(By.NAME, "password")#finds input element on the page, find by inspecting
  submit = browser.find_element(By.XPATH, '//input[@value="Log in"]')  #this element is a button

  user_name.send_keys("tester")
  user_password.send_keys("password")
  submit.send_keys(Keys.RETURN)

  assert "Site administration" in browser.page_source
