from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from bs4 import BeautifulSoup
from time import sleep


options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('lang=ko_KR')
chromedriver_path = 'C:/dev_python/Webdriver/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(chromedriver_path, options=options)  # chromedriver 열기


def main():
    global driver, menu_wb

    driver.implicitly_wait(4)  # 렌더링 될때까지 기다린다 4초
    driver.get('https://map.kakao.com/')  # 주소 가져오기

    search('강남구 커피')

    driver.quit()
    print("finish")


def search(place):
    global driver

    search_area = driver.find_element(By.XPATH,'//*[@id="search.keyword.query"]')
    search_area.send_keys(place)  # 검색어 입력
    driver.find_element(By.XPATH,'// *[ @ id = "search.keyword.submit"]').send_keys(Keys.ENTER)  # Enter로 검색
    sleep(1)

    # 검색된 정보가 있는 경우에만 탐색
    # 1번 페이지 place list 읽기
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    place_lists = soup.select('.placelist > .PlaceItem') # 검색된 장소 목록

    # 검색된 첫 페이지 장소 목록 크롤링하기
    crawling(place_lists)
    search_area.clear()

def crawling(placeLists):
    for i, place in enumerate(placeLists):
        menuInfos = getMenuInfo(i)
        print(menuInfos)

def getMenuInfo(i):
    # 상세페이지로 가서 메뉴찾기
    detail_page_xpath = '//*[@id="info.search.place.list"]/li[' + str(i + 1) + ']/div[5]/div[4]/a[1]'
    driver.find_element(By.XPATH, detail_page_xpath).send_keys(Keys.ENTER)
    driver.switch_to.window(driver.window_handles[-1])  # 상세정보 탭으로 변환
    sleep(1)




if __name__ == "__main__":
    main()

