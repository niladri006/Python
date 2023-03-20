from selenium import webdriver
import time
import random

driver = webdriver.Chrome("D:\\Python\\chromedriver.exe")

viedos = [
    'https://www.youtube.com/watch?v=LEog5IRZH2Q',
    'https://www.youtube.com/watch?v=ITqcdeaKFQM',
    'https://www.youtube.com/watch?v=mTR8KnBWmmg',
    'https://www.youtube.com/watch?v=mCSZG-a0cDA'
]

for i in range(1000):
    print("Runing the viedo for {} time".format(i))
    random_viedo = random.randint(0, 8)
    driver.get(viedos[random_viedo])
    sleep_time = random.randint(31, 60)
    time.sleep(sleep_time)

driver.quit()
