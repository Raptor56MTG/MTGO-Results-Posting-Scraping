from selenium import webdriver
from bs4 import BeautifulSoup


def scrape(url):
    """Grabs the data from the MTGO league posting using BS4."""

    # grab the data from the challenge page using selenium + bs4
    browser = webdriver.Chrome(executable_path="./chromedriver.exe")
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, "html.parser")

    # store usernames in a text file
    usernames = soup.find_all("p", class_="decklist-player")
    with open("usernames.txt", "w") as f:
        for i, username in enumerate(usernames):
            f.write(f"{i + 1}. {username.text.split()[0]}\n")

    # store decklists in a text file
    decklists = soup.find_all(class_="decklist-sort-group decklist-sort-type")
    with open("decklists.txt", "w") as f:
        for decklist in decklists:
            maindeck = decklist.find(class_="decklist-category-columns").find_all(
                                     class_="decklist-category-card")
            for card in maindeck:
                f.write(f"{card.text}\n")
            f.write("\n")
            sideboard = decklist.find(
                    class_="decklist-category-list decklist-sideboard decklist-category-columns").find_all(
                    class_="decklist-category-card")
            for card in sideboard:
                f.write(f"{card.text}\n")
            f.write("\n")
