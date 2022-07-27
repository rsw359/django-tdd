import pytest
from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def chrome_browser_instance(request):
  """
  provide a selenium webdriver instance
  """

  options = Options()
  options.headless = False 
  """headless = True allows test to be viewed"""
  browser = webdriver.Chrome(chrome_options=options)
  yield browser
  browser.close()