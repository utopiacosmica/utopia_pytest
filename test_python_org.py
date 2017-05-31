from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep as sleep


chromeOptions = webdriver.ChromeOptions()
prefs = {
"download.default_directory" : "/Users/utopia/Desktop",
"download.prompt_for_download": False,
"download.directory_upgrade": True,
"safebrowsing.enabled": True
}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "driver_mac/chromedriver"
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
driver.maximize_window()


def test_python_org_download36():
        driver.get('https://www.python.org/')
        element = driver.find_element_by_link_text('Downloads')
        element.click()
        driver.implicitly_wait(5)
        driver.get('https://www.python.org/ftp/python/3.6.1/python-3.6.1-macosx10.6.pkg')
        sleep(10)
        driver.close()
