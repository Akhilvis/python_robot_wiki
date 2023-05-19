import re
import time
from datetime import datetime

from RPA.Browser.Selenium import Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

br = Selenium()


class Robot:
    def __init__(self, name):
        self.name = name
        self.extract_data_list = []

    def say_hello(self):
        print(
            f"""
            Hello, my name is  {self.name}.
            I am an robotic process automation system, 
            trying to help you to extract values informations from the web.
            I am going to the following steps for the successfull extraction of scientist informations...
            1. open the browser, naviagte to the base url 'https://en.wikipedia.org/wiki/Main_Page'
            2. Search each scientist name in the top search bar and clicking search button
            3. Crawl through the entire page 
            4. Fiding the first paragraph using CSS Selectors
            5. Finding the biography data, regex matching to get born and died dates
            6. Finding age using born and died age objects
            7. Displaying all the data in a readable format.
            8. Writing data to a file in json format.
            Note: Added some implicit wait for suceccfull rendering of elements between each scroll ,
            please be patient.
            """
        )
        time.sleep(22)

    def say_goodbye(self):
        print("Bye Bye, Have a good day...")

    def open_webpage_and_crawl(self, webpage, scientist_list):
        br.open_available_browser(webpage)
        self.web_driver = br.driver
        self.wait = WebDriverWait(self.web_driver, 10)

        for scientist in scientist_list:
            self.temp_scientist_dict = {}
            self.temp_scientist_dict["name"] = scientist
            self.search_scientist(scientist)
            self.extract_data()
            self.extract_data_list.append(self.temp_scientist_dict)

        br.close_all_browsers()

        return self.extract_data_list

    def search_scientist(self, scientist_name):
        time.sleep(6)
        textbox_element = self.wait.until(
            EC.presence_of_element_located((By.ID, "searchform"))
        )

        textbox_input = textbox_element.find_element(By.TAG_NAME, "input")
        textbox_input.send_keys(scientist_name)

        submit_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#searchform > div > button"))
        )
        submit_button.click()

    def extract_data(self):
        self.find_fist_paragraph()
        self.find_age_data()

    def find_fist_paragraph(self):
        fist_paragraph = self.web_driver.find_element(
            By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[2]'
        )
        if not fist_paragraph.text:
            fist_paragraph = self.web_driver.find_element(
                By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[3]'
            )

        self.temp_scientist_dict["first_paragraph"] = fist_paragraph.text

    def find_age_data(self):
        biography_element = self.web_driver.find_element(
            By.CLASS_NAME, "infobox.biography.vcard"
        )
        bio_text = biography_element.text

        born_pattern_regex = re.compile("Born\s*.*?\s*(\d{1,2}\s*[A-Za-z]+\s*\d{4})")
        died_pattern_regex = re.compile("Died\s*.*?\s*(\d{1,2}\s*[A-Za-z]+\s*\d{4})")

        born_match = born_pattern_regex.search(bio_text)
        if born_match:
            born_date_string = born_match.group(1)
            born_date = self.date_string_to_object(born_date_string)

        died_match = died_pattern_regex.search(bio_text)
        if died_match:
            died_date_string = died_match.group(1)
            died_date = self.date_string_to_object(died_date_string)

        self.temp_scientist_dict["born_date"] = born_date_string
        self.temp_scientist_dict["died_date"] = died_date_string
        self.temp_scientist_dict["age"] = (
            self.calculate_age(born_date, died_date)
            if born_match and died_match
            else "Not Available"
        )

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
