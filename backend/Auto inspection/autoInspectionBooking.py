from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from playsound import playsound
import os
import pygame
from datetime import timedelta
from select_date_range import select_date_range

def auto_inspection(user_email, user_pw, bco, inspection_type, start_date, end_date, name, email, phone_number, booking):

    chrome_binary_path = "./chrome-linux64"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.binary_location = chrome_binary_path
    # Open a website
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://onlineservices.aucklandcouncil.govt.nz/councilonline/login")
    # driver.maximize_window()

    driver.implicitly_wait(1000)

    # Login
    user_name_text_box = driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder$txtUsername$txtUsername")
    next_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    driver.implicitly_wait(100)
    user_name_text_box.send_keys(user_email)
    driver.implicitly_wait(1000)
    next_button.click()
    driver.implicitly_wait(100)

    password_text_box = driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder$txtPassword$txtPassword")
    password_text_box.send_keys(user_pw)
    sleep(0.5)
    next_button = driver.find_element(by=By.NAME, value="btnSubmit")
    next_button.click()
    # Wait for the page to load
    driver.implicitly_wait(100)

    driver.get("https://onlineservices.aucklandcouncil.govt.nz/councilonline/inspection/consent-search?bookingType=single#/")

    # Find the text box
    bco_text_box = driver.find_element(by=By.NAME, value="bcoReference")
    bco_text_box.send_keys(bco)
    bco_text_box.send_keys(Keys.ENTER)
    driver.implicitly_wait(10)
    
    driver.find_element(By.CLASS_NAME, "inspection-book-button").click()
    driver.implicitly_wait(10)

    #Select inspection type
    dropdown = Select(driver.find_element(By.ID, "inspectionType"))
    dropdown.select_by_value(inspection_type)
    wait = WebDriverWait(driver, 10)
    next_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".inspection-next-btn.inspection-nav-button.pull-right")))
    next_btn.click()
    

    ############################################
    booking = select_date_range(start_date=start_date, end_date=end_date ,driver=driver, booking=booking)
    if booking == False:
        print("No available dates found in the future")
        sleep(1)
        driver.quit()
        return
    else:
        booking = True
                #Enter info
        # Find the <select> element
        dropdown = Select(driver.find_element(By.ID, "inspectionTimeSlot"))


        # Select time slot by value
        try:
            dropdown.select_by_value("08:00:00-12:00:00")
        except:
            dropdown.select_by_value("12:00:00-16:00:00")
        #Early two days
        yes_radio = driver.find_element(By.ID, "readyNowYes")
        yes_radio.click()

        #On site contact
        on_site_contact_text_box = driver.find_element(By.ID, "onSiteContactOff")
        on_site_contact_text_box.click()

        # Enter the on-site contact number
        on_site_contact_name_text_box = driver.find_element(By.NAME, "siteContactName")
        on_site_contact_name_text_box.send_keys(name)
        on_site_contact_number_text_box = driver.find_element(By.NAME, "siteContactNo")
        on_site_contact_number_text_box.send_keys(phone_number)
        on_site_contact_email_text_box = driver.find_element(By.NAME, "siteContactEmail")
        on_site_contact_email_text_box.send_keys(email)
        # Click the next button

        wait = WebDriverWait(driver, 10)
        next_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".inspection-next-btn.inspection-nav-button.pull-right")))
        next_btn.click()

    
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load music file (better for long audio)
    pygame.mixer.music.load('./train-horn-337875.mp3')  # Replace with your file

    # Play music in a loop (-1 means infinite loop)
    pygame.mixer.music.play(-1)

    # Keep the program running (press Ctrl+C to stop)
    try:
        while True:
            pygame.time.wait(1000)
    except KeyboardInterrupt:
        pygame.mixer.music.stop()



    sleep(50)
    return booking


if __name__ == "__main__":
    user_email = "1391492370@qq.com"   
    user_pw = "Yiming@0411"
    bco = "BCO10385714"
    inspection_type = "IPB"
    booking = False
    start_date = datetime.strptime("2025-06-02", "%Y-%m-%d").date()
    end_date = datetime.strptime("2025-06-06", "%Y-%m-%d").date()
    phone_number = "0211365090"
    name = "Yiming"
    email = "1391492370@qq.com"

    count = 0
    while True:
        try:
            booking = auto_inspection(user_email, user_pw, bco, inspection_type, start_date, end_date, name, email, phone_number, booking)
            if booking == True:
                print("Booking successful")
                break
            else:
                print("Booking failed, retrying...")
                count += 1
                print(f"Retry count: {count}")
                sleep(10)  
        except Exception as e:
            print(f"An error occurred: {e}")
            count += 1
            print(f"Retry count: {count}")
            sleep(10)
    # auto_inspection(user_email, user_pw, bco, inspection_type, start_date, end_date, phone_number, booking)
    # auto_inspection(user_email, user_pw, bco, inspection_type, start_date, end_date, phone_number, booking)
    # auto_inspection(user_email, user_pw, bco, inspection_type, start_date, end_date, phone_number, booking)
    # auto_inspection(user_email, user_pw, bco, inspection_type, start_date, end_date, phone_number, booking)
    # auto_inspection(user_email, user_pw, bco, inspection_type, start_date, end_date, phone_number, booking)