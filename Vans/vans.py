# Areli Tirado
# Vans Automation Framework
# 04/12/22

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class VansAutomation(unittest.TestCase):
    CHROMEDRIVER = "/Users/arelitirado/Automation/Vans/chromedriver"
    URL="https://www.vans.com/en-us"

    def setUp(self):
        self.driver = webdriver.Chrome(self.CHROMEDRIVER)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver.get(self.URL)

    def test_social_media_instagram_icon(self):
        self.driver.find_element(By.CLASS_NAME, 'icon-instagram').click()
        assert "Vans" or "Instagram" in self.driver.title

    def test_titles_in_footer(self):
        webElements = self.driver.find_elements(By.CLASS_NAME, 'vf-footer-column-row__title')
        for element in webElements:
            assert "Email" or "Address" or "Hours" in element
    
    def test_details_button_functionality(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CLASS_NAME, 'vf-promo-bar__container').click()
        assert "FREE SHIPPING ON ORDERS:" in self.driver.page_source

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
