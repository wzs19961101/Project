import selenium
from selenium import webdriver
import time
from selenium.webdriver.support import ui

wait_time = 180

# 1.input
hero = input('input the hero:')
position = input('input the position:')

# 2.website
url = f'https://euw.op.gg/champion/{hero}/statistics/{position}/matchup#'

# 3.open it
#set language as English
options = webdriver.ChromeOptions()
options.add_argument('lang=en_US')
browser = webdriver.Chrome(chrome_options= options)

#browser = webdriver.Chrome()
# browser.maximize_window() # 
browser.get(url)
browser.implicitly_wait(10)

# find button
wait = ui.WebDriverWait(browser, wait_time)
try:
    wait.until(lambda driver: driver.find_elements_by_xpath("//div[@class='champion-matchup-list__champion']//span[1]"))
    buttons = browser.find_elements_by_xpath("//div[@class='champion-matchup-list__champion']//span[1]")
except Exception as error1:
    buttons = browser.find_elements_by_xpath("//div[@class='champion-matchup-list__champion']//span[1]")
    time.sleep(10)

# loop all button
print('hero    win rate')
for button in buttons:
    # click button
    browser.execute_script("arguments[0].click();", button)
    # to find the left part of the table
    wait = ui.WebDriverWait(browser, wait_time)
    try:
        wait.until(
            lambda driver: driver.find_elements_by_xpath("//table[@class='champion-matchup-table']//td[1]"))
        col = browser.find_elements_by_xpath("//table[@class='champion-matchup-table']//td[1]")
    except Exception as error1:
        browser.execute_script("arguments[0].click();", button)
        col = browser.find_elements_by_xpath("//table[@class='champion-matchup-table']//td[1]")
        time.sleep(10)
    #print(button.text, col[0].text, col[6].text)
    print(button.text, col[5].text)
