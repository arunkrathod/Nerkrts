import time

import pytest
from selenium.webdriver.common.by import By

from utility.BaseClass import BaseClass


class TestCaseone(BaseClass):

    def test_case_one(self, web_name, season_number, episode_title):
        base_function = BaseClass()
        base_function.click_accept_all_cookies_in_catalogue()
        base_function.click_on_search_button()
        base_function.search_video_by_name(web_name)
        base_function.click_video(web_name)
        base_function.select_series(season_number)
        base_function.episode_title(episode_title)
        base_function.Play_video_button()