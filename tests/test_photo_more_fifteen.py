from conftest import *

def test_photo_more_fifteen(my_page: webdriver.Chrome):
    tbody = my_page.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/table/tbody")
    images = tbody.find_elements(By.TAG_NAME, "img")
    counter = 0
    for i in range(len(images)):
        if images[i].get_attribute("src") != '':
            counter += 1
    assert counter >= (len(images) / 2)