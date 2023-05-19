from robotics import Robot

SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]
BASE_URL = "https://en.wikipedia.org/"

robot = Robot("Quandrinaut")


def introduce_yourself():
    robot.say_hello()


def greetigs():
    robot.say_goodbye()


def open_webpage_and_crawl():
    extract_data_list = robot.open_webpage_and_crawl(BASE_URL, SCIENTISTS)
    for scientist_dict in extract_data_list:
        print("------------------------------------------------------------------")
        print(f"Name            : {scientist_dict['name']}")
        print(f"Born Date       : {scientist_dict['born_date']}")
        print(f"Died Date       : {scientist_dict['died_date']}")
        print(f"Age             : {scientist_dict['age']}")
        print(f"First Paragraph : {scientist_dict['first_paragraph']}")
        print("------------------------------------------------------------------")


def main():
    introduce_yourself()
    open_webpage_and_crawl()
    greetigs()


if __name__ == "__main__":
    main()
