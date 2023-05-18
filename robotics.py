import re
import time
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

    def say_hello(self):
        print("Hello, my name is " + self.name)

    def say_goodbye(self):
        print("Goodbye, my name is " + self.name)

    def open_webpage_and_crawl(self, webpage):
        br.open_available_browser(webpage)
        time.sleep(10)

        web_driver = br.driver
        textbox_element = web_driver.find_element(By.ID, "searchform")
        textbox_input = textbox_element.find_element(By.TAG_NAME, "input")
        textbox_input.send_keys("Albert Einstein")
        textbox_input.submit()

        time.sleep(10)

        biography_element = web_driver.find_element(
            By.CLASS_NAME, "infobox.biography.vcard"
        )
        bio_text = biography_element.text
        print(bio_text)
        born_pattern = "Born\s*(\d{1,2}\s*[A-Za-z]+\s*\d{4})"
        died_pattern = "Died\s*(\d{1,2}\s*[A-Za-z]+\s*\d{4})"

        born_match = re.match(born_pattern, bio_text)
        if born_match:
            print("Match found!", born_match)
        else:
            print("No match found.")

        br.close_all_browsers()
