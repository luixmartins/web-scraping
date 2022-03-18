import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


option = Options()
option.headless = False
driver = webdriver.Firefox(
    executable_path=GeckoDriverManager().install(), options=option
)

driver.get("https://br.investing.com/commodities/brent-oil")

driver.quit()
