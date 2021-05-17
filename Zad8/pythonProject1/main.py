from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

url = 'https://tvn24.pl/'
url2 = 'https://www.interia.pl/'


# driverFirefox = webdriver.Firefox(executable_path='/home/asus/Pulpit/geckodriver')

# driverChrome = webdriver.Chrome(executable_path='/home/asus/Pulpit/chromedriver')

# driverOpera = webdriver.Opera(executable_path='/home/asus/Pulpit/operadriver')



def InteriaTests1to3for1():
    ##################### Test 1 Firefox
    driverFirefox = webdriver.Firefox(executable_path='/home/asus/Pulpit/geckodriver')

    driverFirefox.get(url2)
    driverFirefox.maximize_window()

    # rodo popup
    name = 'rodo-popup-agree'
    rodo = driverFirefox.find_element_by_class_name(name)
    rodo.click()

    driverFirefox.implicitly_wait(500)

    # wejscie w horoskop
    #name = 'main-links-a'
    #menu = driverFirefox.find_elements_by_class_name(name)
    #menu[2].click()
    driverFirefox.find_element_by_xpath("/html/body/header/div[1]/ul/li[3]/a").click()


    # wejscie w lwa
    #name = 'lew'
    #button = driverFirefox.find_element_by_class_name(name)
    #button.click()
    driverFirefox.find_element_by_xpath("/html/body/section/div/div/ul/li[5]/a").click()

    # wypisanie horoskopu
    #name = 'horoscope-text'
    #text = driverFirefox.find_element_by_class_name(name)
    #p = text.find_element_by_tag_name('p')
    p = driverFirefox.find_element_by_xpath("/html/body/div[22]/div/div[2]/div[1]/div/div/div[2]/p")
    print(p.text)

    driverFirefox.quit();

    ##################### Test 2 Firefox
    driverFirefox = webdriver.Firefox(executable_path='/home/asus/Pulpit/geckodriver')

    driverFirefox.get(url2)
    driverFirefox.maximize_window()
    driverFirefox.implicitly_wait(5)

    # rodo popup
    name = 'rodo-popup-agree'
    rodo = driverFirefox.find_element_by_class_name(name)
    rodo.click()

    driverFirefox.implicitly_wait(5)

    # wejscie w poczte
    #name = 'main-links-a'
    #menu = driverFirefox.find_elements_by_class_name(name)
    #menu[0].click()
    driverFirefox.find_element_by_xpath("/html/body/header/div[1]/ul/li[1]/a").click()

    # wpisanie emaila
    name = 'account-input'
    input = driverFirefox.find_elements_by_class_name(name)
    input[0].send_keys('admin@interia.pl')
    input[1].send_keys('admin')

    # login
    #name = 'btn'
    #login = driverFirefox.find_elements_by_class_name(name)
    #login[0].click()
    driverFirefox.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/form/button").click()

    # komunikat
    #name = 'form__error'
    #rodo = driverFirefox.find_element_by_class_name(name)
    alert = driverFirefox.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/form/span[1]")

    print(alert.text)

    driverFirefox.implicitly_wait(5)

    driverFirefox.quit();

    ##################### Test 3 Firefox
    driverFirefox = webdriver.Firefox(executable_path='/home/asus/Pulpit/geckodriver')

    driverFirefox.get(url2)
    driverFirefox.maximize_window()
    driverFirefox.implicitly_wait(5)

    # rodo popup
    name = 'rodo-popup-agree'
    rodo = driverFirefox.find_element_by_class_name(name)
    rodo.click()

    driverFirefox.implicitly_wait(50)

    # wejscie w serwisy
    #name = 'main-links-a'
    #menu = driverFirefox.find_elements_by_class_name(name)
    #menu[5].click()
    driverFirefox.find_element_by_xpath("/html/body/header/div[1]/ul/li[6]/a").click()

    # wejscie w wydarzenia
    #name = 'portal-menu-a'
    #menu = driverFirefox.find_elements_by_class_name(name)
    #menu[2].click()
    driverFirefox.find_element_by_xpath("/html/body/nav/div/div[1]/ul/li[3]/div/a").click()

    # wejscie w wybranie lokacji
    #name = 'weather-widget-select-btn'
    #menu = driverFirefox.find_element_by_class_name(name)
    #menu.click()
    driverFirefox.find_element_by_xpath("/html/body/div[20]/div/div/div/div/div/div[1]/div[1]").click()

    # wejscie w gdansk
    #name = 'weather-widget-city-inside'
    #menu = driverFirefox.find_elements_by_class_name(name)
    #menu[3].click()
    driverFirefox.find_element_by_xpath("/html/body/div[20]/div/div/div/div[2]/div/a[4]/span").click()

    text = driverFirefox.find_element_by_xpath("/html/body/div[20]/div/div/div/div[1]/div/div[1]/div[2]")
    print(text.text)

    driverFirefox.quit()


def Tvn24Tests1for1():
    # Test 1 Firefox
    driverFirefox = webdriver.Firefox(executable_path='/home/asus/Pulpit/geckodriver')

    driverFirefox.get(url)
    driverFirefox.maximize_window()
    driverFirefox.implicitly_wait(5)

    #sport
    driverFirefox.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/header/nav/ul/li[2]/ul/li[1]/div/ul/li[9]/div/div/a").click()

    #tenis
    driverFirefox.find_element_by_xpath("/html/body/div[2]/div/nav/div[2]/div[2]/div/ul/li[3]/a").click()

    #wimbledon
    driverFirefox.find_element_by_xpath("/html/body/div[2]/div/nav/section/div/ul/li[4]/a").click()

    #piata stona
    driverFirefox.find_element_by_xpath("/html/body/div[2]/div/section[2]/div[2]/div[2]/div/div[3]/div/div[9]/ul/li[5]/a").click()

    #pierwszy artykul na strone piatej
    data = driverFirefox.find_element_by_xpath("/html/body/div[2]/div/section[2]/div[2]/div[2]/div/div[3]/div/section[1]")

    print(data.text)

    driverFirefox.quit();


Tvn24Tests1for1()
InteriaTests1to3for1()