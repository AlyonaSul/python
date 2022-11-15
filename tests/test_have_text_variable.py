from conftest import *

def test_have_text_variable(my_page: webdriver.Chrome):
    tbody = my_page.find_elements(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/table/tbody/tr/td")

    for pet_data in tbody:
        assert pet_data.text.strip() != ''