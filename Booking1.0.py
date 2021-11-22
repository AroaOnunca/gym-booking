from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from os import environ
import telegram
import telegram_send
import schedule
import time
import logging

def Booking():
    print("Welcome to the booking GYM system.")
    browser=webdriver.Chrome() 
    browser.maximize_window()
    print(browser.title)
    try:
        browser.get("https://reservesactivitats.claror.cat/activitats/index.php")
        sleep(1)
        browser.find_element(By.NAME, 'email').send_keys("user")
        sleep(1)
        browser.find_element(By.NAME, 'password').send_keys("pass")
        sleep(1)
        browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/button').click()
        sleep(2)
        browser.find_element(By.XPATH, '/html/body/button').click()
        sleep(2)
        select = Select(browser.find_element_by_name('office'))
        select.select_by_value('1')
        sleep(2)
        select = Select(browser.find_element_by_name('schedule'))
        select.select_by_value('morning')
        sleep(2)
        select = Select(browser.find_element_by_name('type'))
        select.select_by_value('8')
        sleep(2)
        select = Select(browser.find_element_by_name('space'))
        select.select_by_value('28')
        sleep(2)
        browser.find_element(By.XPATH, '//*[@id="filter"]/div[7]/div[1]/ul/li[5]/ul/li').click();
        sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/form/div[2]/button[2]').click()
        sleep(2)
        browser.save_screenshot('screenshot.png')
        booked = 1
        if booked == 1:
            with open("screenshot.png", "rb") as f:
                telegram_send.send(images=[f])
            print("Enviando telegram")
            telegram_send.send(messages=["Booked Successfully"])
            print("Booked Successfully")
    except:
        print("Booking Failed")

    finally:
        print("return")
        browser.close()
        browser.quit()
        return schedule.CancelJob

if __name__ == '__main__':
    scheduledevent = 2
    if scheduledevent == 1:
        logging.basicConfig()
        schedule_logger = logging.getLogger('schedule')
        schedule_logger.setLevel(level=logging.DEBUG)
        schedule.every().monday.at("07:15").do(Booking)
        while True:
            schedule.run_pending()
            time.sleep(1)
    elif scheduledevent == 2:
        Booking()