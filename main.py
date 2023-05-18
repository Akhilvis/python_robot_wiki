from robotics import Robot

SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]
BASE_URL = "https://en.wikipedia.org/"

robot = Robot("Quandrinaut")


def introduce_yourself():
    robot.say_hello()


def open_webpage_and_crawl():
    extract_data_dict = robot.open_webpage_and_crawl(BASE_URL, SCIENTISTS)
    print("============================================== ")
    print(extract_data_dict)


def main():
    introduce_yourself()
    open_webpage_and_crawl()


if __name__ == "__main__":
    main()
