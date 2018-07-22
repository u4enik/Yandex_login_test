
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import unittest, time

class LoginGmailTest(unittest.TestCase):

    def setUp(self):
        self.baseURL = "https://google.com"
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
#        self.driver.maximize_window()

    def testLoginTest(self):
        driver = self.driver
        driver.get(self.baseURL)
        self.assertIn("Google", driver.title)

    # Sign in
        sign = driver.find_element(By.ID, "gb_70")
        sign.click()

        loginField = driver.find_element(By.ID, "identifierId")
        loginField.send_keys("*****@gmail.com")

        next = driver.find_element(By.ID, "identifierNext")
        next.click()
        time.sleep(1)

        pasField = driver.find_element(By.NAME, "password")
        pasField.send_keys("*****")

        next2 = driver.find_element(By.ID, "passwordNext")
        next2.click()
        time.sleep(1)

        mail = driver.find_element(By.LINK_TEXT, "Gmail")
        mail.click()

        self.assertEqual("COMPOSE", driver.find_element(By.XPATH, "//div[@class = 'T-I J-J5-Ji T-I-KE L3']").text)
        self.assertTrue(self.element_present(By.XPATH, "//div[@class = 'T-I J-J5-Ji T-I-KE L3']"))
        #CSS .T-I J-J5-Ji T-I-KE L3
#        try:
#            element = WebDriverWait(driver, 10).until(
#                    EC.presence_of_element_located((By.XPATH,
#                                                    "//div[contains(text(), 'COMPOSE')]")))
#        except:
#            driver.quit()
    # New letter
        compose = driver.find_element(By.XPATH, "//div[contains(text(), 'COMPOSE')]")
        compose.click()

        time.sleep(3)
    # Screenshot
        screen = "D:\scr\gmail.png"
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
