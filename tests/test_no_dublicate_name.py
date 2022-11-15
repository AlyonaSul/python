from conftest import *

def test_no_dublicate_name(my_page: webdriver.Chrome):
    td_elements_with_name = my_page.find_elements(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/table/tbody/tr/td[1]")
    pet_names = []
    for name in td_elements_with_name:
        pet_names.append(name.text)
    assert len(pet_names) == len(set(pet_names))