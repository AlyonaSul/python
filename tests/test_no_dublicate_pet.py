from conftest import *

def test_no_dublicate_name(my_page: webdriver.Chrome):
    tr_elements = my_page.find_elements(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/table/tbody/tr")
    pets = []

    for tr_pet in tr_elements:
        pets.append(tr_pet.text)

    assert len(set(pets)) == len(pets)