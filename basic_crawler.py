import requests
import argparse
from selenium import webdriver
from bs4 import BeautifulSoup

class BasicCrawler:
    def __init__(self):
        pass

    # scrape page statically using beautiful soup
    def scrape_page_static(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html5lib")

        with open("output.txt", "w") as file:
            file.write(soup.prettify())

    # tbu: scrape page dynamically using selenium
    def scrape_page_dynamic(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.quit()
        pass

if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="url of the website to crawl")
    args = parser.parse_args()

    # Scrape the website
    bc = BasicCrawler()
    bc.scrape_page_static(args.url)
    print("Crawling done")