
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest, time

class LoginYandexTest(unittest.TestCase):

    def setUp(self):
        self.baseURL = "https://yandex.ru"
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
#        self.driver.maximize_window()

    def testLoginTest(self):
        driver = self.driver
        driver.get(self.baseURL)
        self.assertIn("Яндекс", driver.title)

    # Sign in
        sign = driver.find_element(By.LINK_TEXT, "Войти в почту")
        sign.click()

        loginField = driver.find_element(By.NAME, "login")
        loginField.send_keys("*****@yandex.ru")

        pasField = driver.find_element(By.NAME, "passwd")
        pasField.send_keys("*****")

        submit = driver.find_element(By.XPATH, "//button[@class = 'passport-Button' and @type = 'submit']")
        submit.click()

        self.assertEqual("*****", driver.find_element(By.CSS_SELECTOR, ".mail-User-Name").text)
        self.assertTrue(self.element_present(By.XPATH, "//span[text() = 'Входящие']"))

    # New letter
        compose = driver.find_element(By.CSS_SELECTOR, ".mail-ComposeButton-Text")
        compose.click()

        time.sleep(3)
    # Screenshot
        screen = "D:\scr\yandex.png"
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
