import time
from typing import Tuple
from xml.etree.ElementTree import Element

import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class BaseClass():

    search_button = (By.CSS_SELECTOR, "#search-btn")
    search_tab = (By.ID, "search")
    videos_list = (By.XPATH, "//a[@class='cp_link cp_result-item__link']")
    accept_all_cookies = (By.XPATH, "//div[@class='cassie-pre-banner--button--container']/button[@id='cassie_accept_all_pre_banner']")
    Play_video_button = (By.CSS_SELECTOR, ".videoPlayerActionButtons")

    def series(self, series: str) -> Tuple[str, str]:
        return (By.XPATH, f"//button[text()='({series})']")

    def episode_title(self, title: str) -> Tuple[str, str]:
        return (By.XPATH, f"//footer[@class='cp_tile__footer']/h2[contains(text(), '({title})')]")


    def click_accept_all_cookies_in_catalogue(self):
        for i, driver in enumerate(self.drivers):
            driver.implicitly_wait(5)
            driver.find_element(*self.accept_all_cookies).click()

    def click_on_search_button(self):
        for i, driver in enumerate(self.drivers):
            driver.implicitly_wait(5)
            driver.find_element(*self.search_button).click()

    def search_video_by_name(self, episode:str, season:str):
        for i, driver in enumerate(self.drivers):
            driver.implicitly_wait(10)
            driver.find_element(*self.search_tab).send_keys(episode,season)

    def click_video(self, name: str):
        for i, driver in enumerate(self.drivers):
            driver.implicitly_wait(5)
            series_list = driver.find_elements(*self.videos_list)
            for series in series_list:
                if series.get_attribute("title") == name:
                    series.click()
                    break

    def select_series(self, series: str):
        for i, driver in enumerate(self.drivers):
            driver.implicitly_wait(5)
            driver.find_element(*self.series(series)).click()

    def select_title(self, title: str):
        for i, driver in enumerate(self.drivers):
            driver.implicitly_wait(5)
            driver.find_element(*self.episode_title(title)).click()

    def click_play_video_button(self):
        for i, driver in enumerate(self.drivers):
            driver.implicitly_wait(5)
            driver.find_element(*self.Play_video_button).click()











            # driver.find_element(By.CSS_SELECTOR, "#search-btn").click()
            # driver.find_element(By.CSS_SELECTOR, "#search").send_keys("12 Monkeys")
            # time.sleep(10)


