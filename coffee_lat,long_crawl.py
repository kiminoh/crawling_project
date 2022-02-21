from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests; from urllib.parse import urlparse
def address_to_latitude(address):
    global lat
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query='+address
    rest_api_key = ''
    header = {'Authorization': 'KakaoAK' + rest_api_key }
    result = requests.get(urlparse(url).geturl(), headers=header)

    json_obj = result.json()
    for document in json_obj['documents']:
        lat = document['y']
    return lat

def address_to_longtitude(address):
    global long
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    rest_api_key = ''
    header = {'Authorization': 'KakaoAK' + rest_api_key}
    result = requests.get(urlparse(url).geturl(), headers=header)

    json_obj = result.json()
    for document in json_obj['documents']:
         long = document['x']
    return long

find =  input('검색할 정보를 입력하세요 : ')
time.sleep(10)

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('lang=ko_KR')
chromedriver_path = 'C:/dev_python/Webdriver/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(chromedriver_path, options=options)

url = "https://m.map.naver.com/"
driver.get(url)
action = ActionChains(driver)

time.sleep(4)
driver.find_element(By.CLASS_NAME, 'Nbox_input_text').click()
driver.find_element(By.CLASS_NAME, 'Nbox_input_text._search_input').send_keys(find)
driver.find_element(By.XPATH, '//*[@id="ct"]/div[1]/div[1]/form/div/div[2]/div/span[2]/button[2]').click()

time.sleep(4)
replys =driver.find_elements(By.XPATH, '//*[@id="ct"]/div[2]/ul/li')

results = []
for index, reply in enumerate(replys):
        name = reply.find_element_by_css_selector('div.item_tit').text
        address =reply.find_element_by_css_selector('div.wrap_item').text.split('\n')[2]
        latitude = address_to_latitude(address)
        longtitude = address_to_longtitude(address)
        results.append((name, address, latitude, longtitude))

print(results)
