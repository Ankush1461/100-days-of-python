# Internet Speed Twitter Complaint Bot

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 150
PROMISED_UP = 50

CHROME_DRIVER_PATH = Service("C:\development\chromedriver_win32\chromedriver.exe")
TWITTER_EMAIL = "abc@gmail.com"
TWITTER_PASSWORD = "abc12345"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        go_button = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        go_button.click()
        time.sleep(60)
        self.up = self.driver.find_element(By.CLASS_NAME, 'upload-speed').text
        self.down = self.driver.find_element(By.CLASS_NAME, 'download-speed').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(2)
        email = self.driver.find_element(By.XPATH,
                                         '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH,
                                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        tweet_button = self.driver.find_element(By.XPATH,
                                                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
        tweet_button.click()
        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
