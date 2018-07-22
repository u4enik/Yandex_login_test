
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest, time

class LoginYahooTest(unittest.TestCase):

    def setUp(self):
        self.baseURL = "https://yahoo.com"
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
#        self.driver.maximize_window()

    def testLoginTest(self):
        driver = self.driver
        driver.get(self.baseURL)
        self.assertIn("Yahoo", driver.title)

    #Sign in
        sign = driver.find_element(By.ID, "uh-signin")
        sign.click()

        loginField = driver.find_element(By.ID, "login-username")
        loginField.send_keys("*****@yahoo.com")

        next = driver.find_element(By.ID, "login-signin")
        next.click()
        time.sleep(1)

        pasField = driver.find_element(By.ID, "login-passwd")
        pasField.send_keys("*****")

        next2 = driver.find_element(By.ID, "login-signin")
        next2.click()

        self.assertTrue(self.element_present(By.XPATH, "//li[@id = 'uh-profile']/button"))

        mail = driver.find_element(By.XPATH, "//a[@id='uh-mail-link']")
        mail.click()

        self.assertEqual("Inbox", driver.find_element_by_css_selector("span.rtlI_rtlI_dz_sSg.").text)
        self.assertTrue(self.element_present(By.LINK_TEXT, "Compose"))

    # New letter
        compose = driver.find_element(By.XPATH, "//a[contains(text(), 'Compose')]")
        compose.click()

        time.sleep(3)
    # Screenshot
        screen = "D:\scr\yahoo.png"
        try:
            driver.save_screenshot(screen)
            print("Screenshot saved to directory: " + screen)
        except NotADirectoryError:
            print("Not a directory")


    def element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
            print("GOOD")
        except NoSuchElementException as e:
            print("BAD")
            return False
        return True

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
