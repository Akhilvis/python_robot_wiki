import re
import time
from datetime import datetime

from RPA.Browser.Selenium import Selenium
from selenium.webdriver.common.by import By


br = Selenium()
# # Set Mozilla Firefox user agent
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
# # br.add_custom_capability("goog:chromeOptions", {"args": ["--user-agent=" + user_agent]})

# options = br.driver.ChromeOptions()
# options.add_argument(f"--user-agent={user_agent}")

# driver = br.driver.Chrome(options=options)


class Robot:
    def __init__(self, name):
        self.name = name
        self.extract_data_dict = {}

    def say_hello(self):
        print("Hello, my name is " + self.name)

    def say_goodbye(self):
        print("Goodbye, my name is " + self.name)

    def open_webpage_and_crawl(self, webpage, scientist_list):
        br.open_available_browser(webpage)
        self.web_driver = br.driver
        time.sleep(10)

        for scientist in scientist_list:
            self.search_scientist(scientist)
            self.extract_data()
            time.sleep(6)

        print("---------------------------------------------------------")
        print(self.extract_data_dict)
        print("---------------------------------------------------------")

        br.close_all_browsers()

        return self.extract_data_dict

    def search_scientist(self, scientist_name):
        textbox_element = self.web_driver.find_element(By.ID, "searchform")
        textbox_input = textbox_element.find_element(By.TAG_NAME, "input")
        textbox_input.send_keys(scientist_name)
        textbox_input.submit()
        time.sleep(10)

    def extract_data(self):
        print("=============  extract_data ==================")
        fist_paragraph = self.web_driver.find_element(
            By.CSS_SELECTOR, "#mw-content-text > div.mw-parser-output > p:nth-child(17)"
        )
        self.extract_data_dict["fist_paragraph"] = fist_paragraph.text

        biography_element = self.web_driver.find_element(
            By.CLASS_NAME, "infobox.biography.vcard"
        )
        bio_text = biography_element.text
        born_pattern = "Born\s*(\d{1,2}\s*[A-Za-z]+\s*\d{4})"
        died_pattern = "Died\s*(\d{1,2}\s*[A-Za-z]+\s*\d{4})"

        born_match = re.search(born_pattern, bio_text)
        if born_match:
            print("Born date string format is ... ", born_match.group(1))
            born_date_string = born_match.group(1)
            born_date = self.date_string_to_object(born_date_string)
            print("Match found!", born_date)
        else:
            print("No match found.")

        died_match = re.search(died_pattern, bio_text)
        if died_match:
            died_date_string = died_match.group(1)
            died_date = self.date_string_to_object(died_date_string)
            print("Match found!", died_date)
        else:
            print("No match found.")

        print("Age is >>>>>>>>>>>>>>  ", self.calculate_age(born_date, died_date))

        self.extract_data_dict["born_date"] = born_date_string
        self.extract_data_dict["died_date"] = died_date_string

    def date_string_to_object(self, date_string):
        date_format = "%d %B %Y"
        return datetime.strptime(date_string, date_format).date()

    def calculate_age(self, birth_date, death_date):
        age = death_date.year - birth_date.year

        # Check if the birthday hasn't occurred yet in the death year
        if death_date.month < birth_date.month or (
            death_date.month == birth_date.month and death_date.day < birth_date.day
        ):
            age -= 1

        return age
