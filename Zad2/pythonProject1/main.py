from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

url = 'https://www.zalando.pl/'
url2 = 'https://www.interia.pl/'


# driverFirefox = webdriver.Firefox(executable_path='/home/asus/Pulpit/geckodriver')

# driverChrome = webdriver.Chrome(executable_path='/home/asus/Pulpit/chromedriver')

# driverOpera = webdriver.Opera(executable_path='/home/asus/Pulpit/operadriver')


def ZalandoTests1to3for3():
    # Test 1 Firefox
    driverFirefox = webdriver.Firefox(executable_path='/home/asus/Pulpit/geckodriver')

    driverFirefox.get(url)
    driverFirefox.maximize_window()
    driverFirefox.implicitly_wait(5)

    # wejscie w nowosci
    name = 'u-6V88'
    menu = driverFirefox.find_element_by_class_name(name)
    menu.click()

    # wejscie w damskie
    name = 'cat_link-mTK6o'
    button = driverFirefox.find_element_by_class_name(name)
    button.click()

    # wejscie w odziez
    name = 'cat_link-mTK6o'
    button = driverFirefox.find_element_by_class_name(name)
    button.click()

    # zliczenie i wypisanie produktow wyswietlonych na stronie
    name = 'qMZa55'
    elements = driverFirefox.find_elements_by_class_name(name)
    number = len(elements)
    print("Number of products on site : ")
    print(number)

    driverFirefox.quit();

    ##################### Test 2 Firefox
    driverFirefox = webdriver.Firefox(executable_path='/home/asus/Pulpit/geckodriver')

    driverFirefox.get(url)
    driverFirefox.maximize_window()
    driverFirefox.implicitly_wait(5)

    # wpisanie emaila w newssetler
    name = 'nMYklG'
    newssetler = driverFirefox.find_element_by_class_name(name)
    newssetler.send_keys("email@zalando.pl")

    # zaznaczenie radio boxa
    name = 'wXrLCE'
    button = driverFirefox.find_element_by_class_name(name)
    button.click()

    # zapisanie sie do newsetlera
    name = 'DJxzzA'
    button = driverFirefox.find_element_by_class_name(name)
    button.click()
    print("Sign in to Newssettler.")

    driverFirefox.implicitly_wait(5)

    driverFirefox.quit();

    ##################### Test 3 Firefox
    driverFirefox = webdriver.Firefox(executable_path='/home/asus/Pulpit/geckodriver')

    driverFirefox.get(url)
    driverFirefox.maximize_window()
    driverFirefox.implicitly_wait(5)

    # wejscie w nowosci
    name = 'u-6V88'
    menu = driverFirefox.find_element_by_class_name(name)
    menu.click()

    # kilkniecie w dropdown kolorow
    name = 'cat_head-3QSpK'
    select = driverFirefox.find_elements_by_class_name(name)
    select[3].click()

    # kilkniecie w kolor nr9 ( zielony )
    name = 'cat_label-3NBdm'
    color = driverFirefox.find_elements_by_class_name(name)
    color[8].click()

    # zapsanie filtrowania
    name = 'cat_save-3v2Gl'
    save = driverFirefox.find_element_by_class_name(name)
    save.click()
    print("Selected only green products.")

    driverFirefox.quit()

    ##################### Test 1 Chrome
    driverChrome = webdriver.Chrome(executable_path='/home/asus/Pulpit/chromedriver')

    driverChrome.get(url)
    driverChrome.maximize_window()
    driverChrome.implicitly_wait(5)

    # wejscie w nowosci
    name = 'u-6V88'
    menu = driverChrome.find_element_by_class_name(name)
    menu.click()

    # wejscie w damskie
    name = 'cat_link-mTK6o'
    button = driverChrome.find_element_by_class_name(name)
    button.click()

    # wejscie w odziez
    name = 'cat_link-mTK6o'
    button = driverChrome.find_element_by_class_name(name)
    button.click()

    # zliczenie i wypisanie produktow wyswietlonych na stronie
    name = 'qMZa55'
    elements = driverChrome.find_elements_by_class_name(name)
    number = len(elements)
    print("Number of products on site : ")
    print(number)

    driverChrome.quit();

    ##################### Test 2 Chrome
    driverChrome = webdriver.Chrome(executable_path='/home/asus/Pulpit/chromedriver')

    driverChrome.get(url)
    driverChrome.maximize_window()
    driverChrome.implicitly_wait(5)

    # wpisanie emaila w newssetler
    name = 'nMYklG'
    newssetler = driverChrome.find_element_by_class_name(name)
    newssetler.send_keys("email@zalando.pl")

    # zaznaczenie radio boxa
    name = 'wXrLCE'
    button = driverChrome.find_element_by_class_name(name)
    button.click()

    # zapisanie sie do newsetlera
    name = 'DJxzzA'
    button = driverChrome.find_element_by_class_name(name)
    button.click()
    print("Sign in to Newssettler.")

    driverChrome.implicitly_wait(5)

    driverChrome.quit();

    ##################### Test 3 Chrome
    driverChrome = webdriver.Chrome(executable_path='/home/asus/Pulpit/chromedriver')

    driverChrome.get(url)
    driverChrome.maximize_window()
    driverChrome.implicitly_wait(5)

    # wejscie w nowosci
    name = 'u-6V88'
    menu = driverChrome.find_element_by_class_name(name)
    menu.click()

    # kilkniecie w dropdown kolorow
    name = 'cat_head-3QSpK'
    select = driverChrome.find_elements_by_class_name(name)
    select[3].click()

    # kilkniecie w kolor nr9 ( zielony )
    name = 'cat_label-3NBdm'
    color = driverChrome.find_elements_by_class_name(name)
    color[8].click()

    # zapsanie filtrowania
    name = 'cat_save-3v2Gl'
    save = driverChrome.find_element_by_class_name(name)
    save.click()
    print("Selected only green products.")

    driverChrome.quit()

    ##################### Test 1 Opera
    driverOpera = webdriver.Opera(executable_path='/home/asus/Pulpit/operadriver')

    driverOpera.get(url)
    driverOpera.maximize_window()
    driverOpera.implicitly_wait(5)

    # wejscie w nowosci
    name = 'u-6V88'
    menu = driverOpera.find_element_by_class_name(name)
    menu.click()

    # wejscie w damskie
    name = 'cat_link-mTK6o'
    button = driverOpera.find_element_by_class_name(name)
    button.click()

    # wejscie w odziez
    name = 'cat_link-mTK6o'
    button = driverOpera.find_element_by_class_name(name)
    button.click()

    # zliczenie i wypisanie produktow wyswietlonych na stronie
    name = 'qMZa55'
    elements = driverOpera.find_elements_by_class_name(name)
    number = len(elements)
    print("Number of products on site : ")
    print(number)

    driverOpera.quit();

    ##################### Test 2 Opera
    driverOpera = webdriver.Opera(executable_path='/home/asus/Pulpit/operadriver')

    driverOpera.get(url)
    driverOpera.maximize_window()
    driverOpera.implicitly_wait(5)

    # wpisanie emaila w newssetler
    name = 'nMYklG'
    newssetler = driverOpera.find_element_by_class_name(name)
    newssetler.send_keys("email@zalando.pl")

    # zaznaczenie radio boxa
    name = 'wXrLCE'
    button = driverOpera.find_element_by_class_name(name)
    button.click()

    # zapisanie sie do newsetlera
    name = 'DJxzzA'
    button = driverOpera.find_element_by_class_name(name)
    button.click()
    print("Sign in to Newssettler.")

    driverOpera.implicitly_wait(5)

    driverOpera.quit();

    ##################### Test 3 Opera
    driverOpera = webdriver.Opera(executable_path='/home/asus/Pulpit/operadriver')

    driverOpera.get(url)
    driverOpera.maximize_window()
    driverOpera.implicitly_wait(5)

    # wejscie w nowosci
    name = 'u-6V88'
    menu = driverOpera.find_element_by_class_name(name)
    menu.click()

    # kilkniecie w dropdown kolorow
    name = 'cat_head-3QSpK'
    select = driverOpera.find_elements_by_class_name(name)
    select[3].click()

    # kilkniecie w kolor nr9 ( zielony )
    name = 'cat_label-3NBdm'
    color = driverOpera.find_elements_by_class_name(name)
    color[8].click()

    # zapsanie filtrowania
    name = 'cat_save-3v2Gl'
    save = driverOpera.find_element_by_class_name(name)
    save.click()
    print("Selected only green products.")

    driverOpera.quit()

def InteriaTests1to3for3():
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
    name = 'main-links-a'
    menu = driverFirefox.find_elements_by_class_name(name)
    menu[2].click()

    # wejscie w lwa
    name = 'lew'
    button = driverFirefox.find_element_by_class_name(name)
    button.click()

    # wypisanie horoskopu
    name = 'horoscope-text'
    text = driverFirefox.find_element_by_class_name(name)
    p = text.find_element_by_tag_name('p')
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
    name = 'main-links-a'
    menu = driverFirefox.find_elements_by_class_name(name)
    menu[0].click()

    # wpisanie emaila
    name = 'account-input'
    input = driverFirefox.find_elements_by_class_name(name)
    input[0].send_keys('admin@interia.pl')
    input[1].send_keys('admin')

    # login
    name = 'btn'
    login = driverFirefox.find_elements_by_class_name(name)
    login[0].click()

    # komunikat
    name = 'form__error'
    rodo = driverFirefox.find_element_by_class_name(name)
    print("Sprobowano sie zalogowac komunikat : ")
    print(rodo.text)

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
    name = 'main-links-a'
    menu = driverFirefox.find_elements_by_class_name(name)
    menu[5].click()

    # wejscie w wydarzenia
    name = 'portal-menu-a'
    menu = driverFirefox.find_elements_by_class_name(name)
    menu[2].click()

    # wejscie w wybranie lokacji
    name = 'weather-widget-select-btn'
    menu = driverFirefox.find_element_by_class_name(name)
    menu.click()

    # wejscie w gdansk
    name = 'weather-widget-city-inside'
    menu = driverFirefox.find_elements_by_class_name(name)
    menu[3].click()

    print("Selected Gdansk.")

    driverFirefox.quit()

    ##################### Test 1 Chrome
    driverChrome = webdriver.Chrome(executable_path='/home/asus/Pulpit/chromedriver')

    driverChrome.get(url2)
    driverChrome.maximize_window()

    # rodo popup
    name = 'rodo-popup-agree'
    rodo = driverChrome.find_element_by_class_name(name)
    rodo.click()

    # wejscie w horoskop
    name = 'main-links-a'
    menu = driverChrome.find_elements_by_class_name(name)
    menu[2].click()

    # wejscie w lwa
    name = 'lew'
    button = driverChrome.find_element_by_tag_name(name)
    button.click()

    # wypisanie horoskopu
    name = 'horoscope-text'
    text = driverChrome.find_element_by_class_name(name)
    p = text.find_element_by_tag_name('p')
    print(p.text)

    driverChrome.quit();

    ##################### Test 2 Chrome
    driverChrome = webdriver.Chrome(executable_path='/home/asus/Pulpit/chromedriver')

    driverChrome.get(url2)
    driverChrome.maximize_window()
    driverChrome.implicitly_wait(5)

    # rodo popup
    name = 'rodo-popup-agree'
    rodo = driverChrome.find_element_by_class_name(name)
    rodo.click()

    driverChrome.implicitly_wait(5)

    # wejscie w poczte
    name = 'main-links-a'
    menu = driverChrome.find_elements_by_class_name(name)
    menu[0].click()

    # wpisanie emaila
    name = 'account-input'
    input = driverChrome.find_elements_by_class_name(name)
    input[0].send_keys('admin@interia.pl')
    input[1].send_keys('admin')

    # wpisanie emaila
    name = 'btn'
    login = driverChrome.find_elements_by_class_name(name)
    login[0].click()

    # komunikat
    name = 'form__error'
    rodo = driverChrome.find_element_by_class_name(name)
    print("Sprobowano sie zalogowac komunikat : ")
    print(rodo.text)

    driverChrome.implicitly_wait(5)

    driverChrome.quit();

    ##################### Test 3 Chrome
    driverChrome = webdriver.Chrome(executable_path='/home/asus/Pulpit/chromedriver')

    driverChrome.get(url2)
    driverChrome.maximize_window()
    driverChrome.implicitly_wait(5)

    # rodo popup
    name = 'rodo-popup-agree'
    rodo = driverChrome.find_element_by_class_name(name)
    rodo.click()

    driverChrome.implicitly_wait(50)

    # wejscie w serwisy
    name = 'main-links-a'
    menu = driverChrome.find_elements_by_class_name(name)
    menu[5].click()

    # wejscie w wydarzenia
    name = 'portal-menu-a'
    menu = driverChrome.find_elements_by_class_name(name)
    menu[2].click()

    # wejscie w wybranie lokacji
    name = 'weather-widget-select-btn'
    menu = driverChrome.find_element_by_class_name(name)
    menu.click()

    # wejscie w gdansk
    name = 'weather-widget-city-inside'
    menu = driverChrome.find_elements_by_class_name(name)
    menu[3].click()

    print("Selected Gdansk.")

    driverChrome.quit()

    ##################### Test 1 Opera
    driverOpera = webdriver.Opera(executable_path='/home/asus/Pulpit/operadriver')

    driverOpera.get(url2)
    driverOpera.maximize_window()

    # rodo popup
    name = 'rodo-popup-agree'
    rodo = driverOpera.find_element_by_class_name(name)
    rodo.click()

    driverOpera.implicitly_wait(500)

    # wejscie w horoskop
    name = 'main-links-a'
    menu = driverOpera.find_elements_by_class_name(name)
    menu[2].click()

    # wejscie w lwa
    name = 'lew'
    button = driverOpera.find_element_by_class_name(name)
    button.click()

    # wypisanie horoskopu
    name = 'horoscope-text'
    text = driverOpera.find_element_by_class_name(name)
    p = text.find_element_by_tag_name('p')
    print(p.text)

    driverOpera.quit();

    ##################### Test 2 Opera
    driverOpera = webdriver.Opera(executable_path='/home/asus/Pulpit/operadriver')

    driverOpera.get(url2)
    driverOpera.maximize_window()
    driverOpera.implicitly_wait(5)

    # rodo popup
    name = 'rodo-popup-agree'
    rodo = driverOpera.find_element_by_class_name(name)
    rodo.click()

    driverOpera.implicitly_wait(5)

    # wejscie w poczte
    name = 'main-links-a'
    menu = driverOpera.find_elements_by_class_name(name)
    menu[0].click()

    # wpisanie emaila
    name = 'account-input'
    input = driverOpera.find_elements_by_class_name(name)
    input[0].send_keys('admin@interia.pl')
    input[1].send_keys('admin')

    # wpisanie emaila
    name = 'btn'
    login = driverOpera.find_elements_by_class_name(name)
    login[0].click()

    # komunikat
    name = 'form__error'
    rodo = driverOpera.find_element_by_class_name(name)
    print("Sprobowano sie zalogowac komunikat : ")
    print(rodo.text)

    driverOpera.implicitly_wait(5)

    driverOpera.quit();

    ##################### Test 3 Opera
    driverOpera = webdriver.Opera(executable_path='/home/asus/Pulpit/operadriver')

    driverOpera.get(url2)
    driverOpera.maximize_window()
    driverOpera.implicitly_wait(5)

    # rodo popup
    name = 'rodo-popup-agree'
    rodo = driverOpera.find_element_by_class_name(name)
    rodo.click()

    driverOpera.implicitly_wait(50)

    # wejscie w serwisy
    name = 'main-links-a'
    menu = driverOpera.find_elements_by_class_name(name)
    menu[5].click()

    # wejscie w wydarzenia
    name = 'portal-menu-a'
    menu = driverOpera.find_elements_by_class_name(name)
    menu[2].click()

    # wejscie w wybranie lokacji
    name = 'weather-widget-select-btn'
    menu = driverOpera.find_element_by_class_name(name)
    menu.click()

    # wejscie w gdansk
    name = 'weather-widget-city-inside'
    menu = driverOpera.find_elements_by_class_name(name)
    menu[3].click()

    print("Selected Gdansk.")
    
    driverOpera.quit()




ZalandoTests1to3for3()
InteriaTests1to3for3()