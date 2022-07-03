from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import *
import os



PROMISED_DOWN = 450
PROMISED_UP = 230
chrome_driver_path = "C:\Development/chromedriver.exe"
TWITTER_USER = "Anthony29967361"
TWITTER_EMAIL = "sanitizersmithen2@gmail.com"
TWITTER_PASSWORD = "nfxHfyFp24ZdCBQ"


class InternetSpeedTwitterBot:

    def __init__(self, driver_path, down, up):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.promised_down = down
        self.promised_up = up
        self.download_speed = 0
        self.upload_speed = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()
        sleep(45)
        self.download_speed = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.upload_speed = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)

        print(f"down: {self.download_speed}")
        print(f"up: {self.upload_speed}")

    def is_speed_bad(self):
        if self.download_speed < self.promised_down and self.upload_speed < self.promised_up:
            return True
        else:
            print("Your internet is providing great speeds!!")
            return False

    def tweet_at_provider(self):

        #logging in
        self.driver.get("https://twitter.com/login")
        sleep(2)
        enter_email = self.driver.find_element(By.CSS_SELECTOR, 'input')
        enter_email.send_keys(TWITTER_EMAIL)
        enter_email.send_keys(Keys.ENTER)

        sleep(2)
        enter_user = self.driver.find_element(By.CSS_SELECTOR, 'div input')
        enter_user.send_keys(TWITTER_USER)
        enter_user.send_keys(Keys.ENTER)

        sleep(2)
        enter_pass = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        enter_pass.send_keys(TWITTER_PASSWORD)
        enter_pass.send_keys(Keys.ENTER)

        # next = self.driver.find_element(By.CSS_SELECTOR, "div .css-18t94o4")
        # next.click()

        sleep(2)
        start_tweeting = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        start_tweeting.click()

        tweet_text = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        tweet_text.send_keys(f"Hey Internet Provider, why is my internet speed {self.download_speed}down/{self.upload_speed}up when I pay for {self.promised_down}down/{self.promised_up}up? ")
        sleep(2)

        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        tweet_button.click()





twitter_bot = InternetSpeedTwitterBot(chrome_driver_path, PROMISED_DOWN, PROMISED_UP)

twitter_bot.get_internet_speed()
if twitter_bot.is_speed_bad():
    twitter_bot.tweet_at_provider()








