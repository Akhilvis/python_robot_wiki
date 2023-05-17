from robotics import Robot

SCIENTISTS = ["Albert Einstein", "Isaac Newton",
              "Marie Curie", "Charles Darwin"]
BASE_URL = "https://en.wikipedia.org/"

robot = Robot("Quandrinaut")


def introduce_yourself():
    robot.say_hello()


def open_webpage_and_crawl():
    robot.open_webpage_and_crawl(BASE_URL)


def main():
    introduce_yourself()
    open_webpage_and_crawl()


if __name__ == "__main__":
    main()
