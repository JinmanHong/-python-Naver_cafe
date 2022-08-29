from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as sp

base_url = "https://cafe.naver.com/joonggonara"
browser = webdriver.Chrome('chromedriver.exe')
browser.get(base_url)
browser.implicitly_wait(5)  # 화면이 뜰때까지 기다린다.


menu = browser.find_element("id", "menuLink1799")
action = ActionChains(browser).move_to_element(menu).click()
action.perform()

browser.switch_to.frame('cafe_main')

soup = sp(browser.page_source, 'html.parser')

article = soup.find_all('div', attrs={"class": "article-board m-tcol-c"})[1]

list_link = []
list_title = []
titles = article.find_all('div', attrs={"class": "inner_list"})
for title in titles:
    print(title.text)
    link = title.find('a', href=True)['href']
    link = base_url + link
    list_link.append(link)
    # print(link)
    title = title.find('a', attrs={"class": "article"}).text
    title = title.strip()
    title = title.replace(",", "")
    list_title.append(title)
    # print(title)

list_name = []

names = article.find_all('td', attrs={"class": "p-nick"})
for name in names:
    name = name.text
    list_name.append(name)
    # print(name)


list_date = []
dates = article.find_all('td', attrs={"class": "td_date"})
for date in dates:
    date = date.text
    list_date.append(date)
    # print(date)

for i in range(len(list_title)):
    file = open("naver_cafe.csv", "a")
    file.write("{}, {}, {}, {} \n".format(
        list_title[i], list_link[i], list_name[i], list_date[i]))
file.close()
