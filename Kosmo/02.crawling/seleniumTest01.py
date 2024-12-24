'''
셀레니엄을 사용하여 크롬을 실행 한다.
구글 페이지로 이동하여 검색 키워드 '북미정상회담'을 입력해 본다.
3초 동안 대기 후, 화면을 이미지로 저장한다.
브라우저를 종료한다.
'''

from selenium import webdriver

filename = 'c:/chromedriver'
driver = webdriver.Chrome(filename)
print(type(driver))

print('구글로 이동하자')
url = 'http://www.google.com'
driver.get(url) # 해당 url로 이동

search_textbox = driver.find_element_by_name('q')
word = '북미정상회담'
search_textbox.send_keys(word)  # 단어 입력
search_textbox.submit()

import time     # 시간을 제어하는 모듈
wait = 3
print(str(wait) + '동안 기다려.')
time.sleep(wait)

imagefile = 'capture.png'
driver.save_screenshot(imagefile)

wait = 3
driver.implicitly_wait(wait)

driver.quit()
print('브라우저를 종료한다.')