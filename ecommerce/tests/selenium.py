import pytest
from requests import options

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    """
    provides a selenium webdriver instance
    """
    driver = webdriver.Chrome(
        executable_path="/Users/roger/projects/e-commerce/django_tut_2/ecommerce/dashboard/tests/chromedriver"
    )

    options = Options()
    options.headless = False
    """headless allows test to be viewed"""
    browser = webdriver.Chrome(chrome_options=options)
    yield browser
    browser.close()
