#Code extracted from the Código Fonte TV channel on Youtube 
#Link to the video: https://www.youtube.com/watch?v=Vxl5jUltHBo&t=509s
#Link to repository on github: https://github.com/gabrielfroes/webscraping_python_selenium

#I USED THE CODE FOR STUDIES ON COLLECTING DATA USING SELENIUM 
import pandas as pd 
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options 
import json 

url = 'https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1'
top_ranking = {}

rankings = {
    '3points': {'field': 'FG3M', 'label': '3PM'},
    'points': {'field': 'PTS', 'label': 'PTS'},
    'assistants': {'field': 'AST', 'label': 'AST'},
    'rebounds': {'field': 'REB', 'label': 'REB'},
    'steals': {'field': 'STL', 'label': 'STL'},
    'blocks': {'field': 'BLK', 'label': 'BLK'},
}

def build_rank(type):
    field, label = rankings[type]['field'], rankings[type]['label']

    driver.find_element_by_xpath(
        f"//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='{field}']"
    ).click()

    element = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
    content_page = element.get_attribute('outerHTML')

    soup = BeautifulSoup(content_page, 'html.parser')
    table = soup.find(name='table')

    data = pd.read_html(str(table))[0].head(10)
    df = data[['Unnamed: 0', 'PLAYER', 'TEAM', label]]
    df.columns = ['pos', 'player', 'team', 'total']

    return df.to_dict('records')

option = Options()
option.headless = False 
driver = webdriver.Firefox(options=option)

driver.get(url)
driver.implicitly_wait(10)

for k in rankings:
    top_ranking[k] = build_rank(k)

driver.quit()

with open('ranking_nba.json', 'w', encoding='utf-8') as jp:
    js = json.dumps(top_ranking, indent=4)
    jp.write(js)
