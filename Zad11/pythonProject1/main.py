from selenium import webdriver
import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

logging.basicConfig(format='%(asctime)s %(message)s', filename='test_hm.log', encoding='utf-8', level=logging.DEBUG)

url = 'https://tvn24.pl/'
url2 = 'https://www.interia.pl/'


# driverFirefox = webdriver.Firefox(executable_path='/home/asus/Pulpit/geckodriver')

# driverChrome = webdriver.Chrome(executable_path='/home/asus/Pulpit/chromedriver')

# driverOpera = webdriver.Opera(executable_path='/home/asus/Pulpit/operadriver')



def InteriaTests1to3for1():
    ##################### Test 1 Firefox
    driverFirefox = webdriver.Firefox(executable_path='/home/asus/Pulpit/geckodriver')

    logging.info("Interia Test 1 Firefox Start")

    driverFirefox.find_element_by_xpath("/html/body/header/div[1]/ul/li[3]/a").click()
    logging.info("Interia Test 1 Step 1")

    # wejscie w lwa
    #name = 'lew'
    #button = driverFirefox.find_element_by_class_name(name)
    #button.click()
    driverFirefox.find_element_by_xpath("/html/body/section/div/div/ul/li[5]/a").click()
    logging.info("Interia Test 1 Step 2")

    # wypisanie horoskopu
    #name = 'horoscope-text'
    #text = driverFirefox.find_element_by_class_name(name)
    #p = text.find_element_by_tag_name('p')
    p = driverFirefox.find_element_by_xpath("/html/body/div[22]/div/div[2]/div[1]/div/div/div[2]/p")

    if p.text:
        logging.error('Interia Test 1 Firefox Data Fail')

    print(p.text)

    driverFirefox.quit();

    logging.info("Interia Test 1 Firefox End")

    ##################### Test 2 Firefox
    driverFirefox = webdriver.Firefox(executable_path='/home/asus/Pulpit/geckodriver')

    logging.info("Interia Test 2 Firefox Start")

    driverFirefox.get(url2)
    driverFirefox.maximize_window()
    driverFirefox.implicitly_wait(5)

    # rodo popup
    name = 'rodo-popup-agree'
    rodo = driverFirefox.find_element_by_class_name(name)
    rodo.click()
    logging.info("Interia Test 2 Step 1")

    driverFirefox.implicitly_wait(5)

    # wejscie w poczte
    #name = 'main-links-a'
    #menu = driverFirefox.find_elements_by_class_name(name)
    #menu[0].click()
    driverFirefox.find_element_by_xpath("/html/body/header/div[1]/ul/li[1]/a").click()
    logging.info("Interia Test 2 Step 2")

    # wpisanie emaila
    name = 'account-input'
    input = driverFirefox.find_elements_by_class_name(name)
    input[0].send_keys('admin@interia.pl')
    input[1].send_keys('admin')
    logging.info("Interia Test 2 Step 3")

    # login
    #name = 'btn'
    #login = driverFirefox.find_elements_by_class_name(name)
    #login[0].click()
    driverFirefox.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/form/button").click()
    logging.info("Interia Test 2 Step 4")

    # komunikat
    #name = 'form__error'
    #rodo = driverFirefox.find_element_by_class_name(name)
    alert = driverFirefox.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/form/span[1]")

    if alert.text:
        logging.error('Interia Test 2 Firefox Data Fail')

    print(alert.text)

    driverFirefox.implicitly_wait(5)

    driverFirefox.quit();

    logging.info("Interia Test 2 Firefox End")

    ##################### Test 3 Firefox
    driverFirefox = webdriver.Firefox(executable_path='/home/asus/Pulpit/geckodriver')

    logging.info("Interia Test 3 Firefox Start")

    driverFirefox.get(url2)
    driverFirefox.maximize_window()
    driverFirefox.implicitly_wait(5)

    # rodo popup
    name = 'rodo-popup-agree'
    rodo = driverFirefox.find_element_by_class_name(name)
    rodo.click()
    logging.info("Interia Test 3 Step 1")


    driverFirefox.implicitly_wait(50)

    # wejscie w serwisy
    #name = 'main-links-a'
    #menu = driverFirefox.find_elements_by_class_name(name)
    #menu[5].click()
    driverFirefox.find_element_by_xpath("/html/body/header/div[1]/ul/li[6]/a").click()
    logging.info("Interia Test 3 Step 2")

    # wejscie w wydarzenia
    #name = 'portal-menu-a'
    #menu = driverFirefox.find_elements_by_class_name(name)
    #menu[2].click()
    driverFirefox.find_element_by_xpath("/html/body/nav/div/div[1]/ul/li[3]/div/a").click()
    logging.info("Interia Test 3 Step 3")

    # wejscie w wybranie lokacji
    #name = 'weather-widget-select-btn'
    #menu = driverFirefox.find_element_by_class_name(name)
    #menu.click()
    driverFirefox.find_element_by_xpath("/html/body/div[20]/div/div/div/div/div/div[1]/div[1]").click()
    logging.info("Interia Test 3 Step 4")

    # wejscie w gdansk
    #name = 'weather-widget-city-inside'
    #menu = driverFirefox.find_elements_by_class_name(name)
    #menu[3].click()
    driverFirefox.find_element_by_xpath("/html/body/div[20]/div/div/div/div[2]/div/a[4]/span").click()
    logging.info("Interia Test 3 Step 5")

    text = driverFirefox.find_element_by_xpath("/html/body/div[20]/div/div/div/div[1]/div/div[1]/div[2]")

    if text.text:
        logging.error('Interia Test 3 Firefox Data Fail')

    print(text.text)

    driverFirefox.quit()

    logging.info("Interia Test 3 Firefox End")

def Tvn24Tests1for1():
    # Test 1 Firefox
    driverFirefox = webdriver.Firefox(executable_path='/home/asus/Pulpit/geckodriver')

    logging.info("Tvn24 Test 1 Firefox Start")

    driverFirefox.get(url)
    driverFirefox.maximize_window()
    driverFirefox.implicitly_wait(5)

    #sport
    driverFirefox.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/header/nav/ul/li[2]/ul/li[1]/div/ul/li[9]/div/div/a").click()
    logging.info("Tvn24 Test 1 Step 1")


    #tenis
    driverFirefox.find_element_by_xpath("/html/body/div[2]/div/nav/div[2]/div[2]/div/ul/li[3]/a").click()
    logging.info("Tvn24 Test 1 Step 2")

    #wimbledon
    driverFirefox.find_element_by_xpath("/html/body/div[2]/div/nav/section/div/ul/li[4]/a").click()
    logging.info("Tvn24 Test 1 Step 3")

    #piata stona
    driverFirefox.find_element_by_xpath("/html/body/div[2]/div/section[2]/div[2]/div[2]/div/div[3]/div/div[9]/ul/li[5]/a").click()
    logging.info("Tvn24 Test 1 Step 4")

    #pierwszy artykul na strone piatej
    data = driverFirefox.find_element_by_xpath("/html/body/div[2]/div/section[2]/div[2]/div[2]/div/div[3]/div/section[1]")

    if data.text:
        logging.error('Tvn24 Test 1 Firefox Data Fail')

    print(data.text)

    driverFirefox.quit();

    logging.info("Tvn24 Test 1 Firefox End")

Tvn24Tests1for1()
InteriaTests1to3for1()