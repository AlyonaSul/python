# from ctypes import sizeof
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    service = Service(executable_path=ChromeDriverManager().install())
    pytest.driver = webdriver.Chrome(service=service, options=chrome_options)
    pytest.driver.implicitly_wait(3)
    yield
    pytest.driver.quit()

@pytest.fixture
def my_page():
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    #    Вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys('al57@mail.com')
    #    Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys('12323')
    #    Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    
    
    wait = WebDriverWait(pytest.driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#navbarNav > ul > li:nth-child(1) > a")) )  # явные ожидания
    navbar_link_to_my_pets = pytest.driver.find_element(By.CSS_SELECTOR, "#navbarNav > ul > li:nth-child(1) > a")
    pytest.driver.execute_script("arguments[0].click();", navbar_link_to_my_pets)
    return pytest.driver

# Написать тест, который проверяет, что на странице со списком питомцев пользователя:

# V 1.Присутствуют все питомцы.
# V 2.Хотя бы у половины питомцев есть фото.
# 3.У всех питомцев есть имя, возраст и порода.
# 4.У всех питомцев разные имена.
# 5.В списке нет повторяющихся питомцев. (Сложное задание).

# Подсказки: 
# 1.Количество питомцев взято из статистики пользователя.
# 2.Количество питомцев с фото тоже можно посчитать, взяв статистику пользователя.
# 3.Необходимо собрать в массив имена питомцев.
# 4.Повторяющиеся питомцы — это питомцы, у которых одинаковое имя, порода и возраст.
