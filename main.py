import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)
        self.up = 0
        self.down = 0
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        privacy_policy_btn = self.driver.find_element(By.CSS_SELECTOR, value=".onetrust-banner-options button")
        # print(privacy_policy_btn.text, privacy_policy_btn.tag_name)
        privacy_policy_btn.click()
        time.sleep(3)
        start_btn = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        # time.sleep(1)
        start_btn.click()
        # print(start_btn.text)
        time.sleep(50)

        self.up = self.driver.find_element(By.CSS_SELECTOR, value=".upload-speed")
        self.down = self.driver.find_element(By.CSS_SELECTOR, value=".download-speed")
        print(f"Upload speed : {self.up.text}")
        print(f"Download speed : {self.down.text}")




bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
# bot.tweet_at_provider()