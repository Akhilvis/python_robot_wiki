import json
from robotics import Robot

SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]
BASE_URL = "https://en.wikipedia.org/"

robot = Robot("Quandrinaut")


def introduce_yourself():
    robot.say_hello()


def greetigs():
    robot.say_goodbye()


def display_write_extracted_data(extract_data_list):
    for scientist_dict in extract_data_list:
        print("------------------------------------------------------------------")
        print(f"Name            : {scientist_dict['name']}")
        print(f"Born Date       : {scientist_dict['born_date']}")
        print(f"Died Date       : {scientist_dict['died_date']}")
        print(f"Age             : {scientist_dict['age']}")
        print(f"First Paragraph : {scientist_dict['first_paragraph']}")
        print("------------------------------------------------------------------")

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(extract_data_list, f, ensure_ascii=False, indent=4)


def open_webpage_and_crawl():
    extract_data = robot.open_webpage_and_crawl(BASE_URL, SCIENTISTS)
    display_write_extracted_data(extract_data)


def main():
    introduce_yourself()
    open_webpage_and_crawl()
    greetigs()


if __name__ == "__main__":
    main()
