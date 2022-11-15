from conftest import *

def test_all_pets(my_page):
    text = my_page.find_element(By.XPATH, "/html/body/div[1]/div/div[1]").text
    startIndex = text.find("Питомцев:") + 9
    endIndex = text.find("Друзей") - 1
    petsSizeInUserStat = int(text[startIndex:endIndex])  
    petSize = len(my_page.find_element(By.XPATH, "//*[@id=\"all_my_pets\"]/table/tbody").find_elements(By.TAG_NAME, "tr"))
    assert petSize == petsSizeInUserStat