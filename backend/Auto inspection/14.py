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

def auto_inspection(user_email, user_pw, bco, inspection_type, start_date, end_date, phone_number, booking):

    try:

        chrome_binary_path = "./chrome-linux64"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.binary_location = chrome_binary_path
        # Open a website
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://onlineservices.aucklandcouncil.govt.nz/councilonline/login")
        # driver.maximize_window()

        driver.implicitly_wait(20)

        # Login
        user_name_text_box = driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder$txtUsername$txtUsername")
        next_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
        driver.implicitly_wait(10)
        user_name_text_box.send_keys(user_email)
        sleep(0.5)
        next_button.click()
        driver.implicitly_wait(20)

        password_text_box = driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder$txtPassword$txtPassword")
        password_text_box.send_keys(user_pw)
        sleep(0.5)
        next_button = driver.find_element(by=By.NAME, value="btnSubmit")
        next_button.click()
        # Wait for the page to load
        driver.implicitly_wait(20)

        driver.get("https://onlineservices.aucklandcouncil.govt.nz/councilonline/inspection/consent-search?bookingType=single#/")

        # Find the text box
        bco_text_box = driver.find_element(by=By.NAME, value="bcoReference")
        bco_text_box.send_keys(bco)
        bco_text_box.send_keys(Keys.ENTER)
        driver.implicitly_wait(20)
        
        driver.find_element(By.CLASS_NAME, "inspection-book-button").click()
        driver.implicitly_wait(20)

        #Select inspection type
        dropdown = Select(driver.find_element(By.ID, "inspectionType"))
        dropdown.select_by_value("OTHERS")
        dropdown = Select(driver.find_element(By.ID, "otherInspectionType"))
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
            on_site_contact_text_box = driver.find_element(By.ID, "onSiteContactOn")
            on_site_contact_text_box.click()

            # Enter the on-site contact number
            on_site_contact_number_text_box = driver.find_element(By.NAME, "siteContactNo")
            on_site_contact_number_text_box.send_keys(phone_number)

            wait = WebDriverWait(driver, 10)
            next_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".inspection-next-btn.inspection-nav-button.pull-right")))
            next_btn.click()
        #Select date
        ############################################
        
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
    except Exception as e:
        print(f"An error occurred: {e}")
        driver.quit()
        return False

def select_date_cloest(driver):

    # Find all available date elements
    available_dates = driver.find_elements(By.CSS_SELECTOR, ".calendar-day-available")

    # Function to extract date from element's parent ID
    def extract_date(element):
        parent_id = element.find_element(By.XPATH, "./..").get_attribute("id")
        date_str = parent_id.split("_")[-1]  # Extract date part from ID like "zabuto_calendar_1nsh_2025-05-21"
        return datetime.strptime(date_str, "%Y-%m-%d").date()

    # Get today's date
    today = datetime.now().date()

    # Find the closest available date (today or future)
    closest_date = None
    min_diff = float('inf')

    for date_element in available_dates:
        try:
            date = extract_date(date_element)
            diff = (date - today).days
            if diff >= 0 and diff < min_diff:
                min_diff = diff
                closest_date = date_element
        except:
            continue

    # Click the closest available date
    if closest_date:
        closest_date.click()
        print(f"Clicked on the closest available date: {extract_date(closest_date)}")
    else:
        print("No available dates found in the future")

    return closest_date

def select_date_range(start_date, end_date, driver, booking):

    # Find all available date elements
    available_dates = driver.find_elements(By.CSS_SELECTOR, ".calendar-day-available")

    # Function to extract date from element's parent ID
    def extract_date(element):
        parent_id = element.find_element(By.XPATH, "./..").get_attribute("id")
        date_str = parent_id.split("_")[-1]  # Extract date part from ID like "zabuto_calendar_1nsh_2025-05-21"
        return datetime.strptime(date_str, "%Y-%m-%d").date()

    # Find the closest available date (today or future)
    closest_date = None
    booking=booking
    for date_element in available_dates:
        try:
            date = extract_date(date_element)
            diff_s = (date - start_date).days
            diff_e = (date -end_date).days
            if diff_s >= 0 and diff_e < 0:
                closest_date = date_element
                booking = True
                break
        except:
            continue

    # Click the closest available date
    if closest_date:
        closest_date.click()
        print(f"Clicked on the closest available date: {extract_date(closest_date)}")
        booking = True
    else:
        print("No available dates found in the future")
        booking = False
    return booking

# Example usage
# Define the parameters

# Call the function with the desired parameters




# user_email = "1391492370@qq.com"
# user_pw = "Yiming@0411"

user_email = "zznn49537@gmail.com"
user_pw = "CYM4sbjb!!!"
bco = "BCO10394518"
inspection_type = "IME"
booking = False
start_date = datetime.strptime("2025-05-30", "%Y-%m-%d").date()
end_date = datetime.strptime("2025-06-2", "%Y-%m-%d").date()
phone_number = "0211189701"

count = 0
while True:
    try:
        booking = auto_inspection(user_email, user_pw, bco, inspection_type, start_date, end_date, phone_number, booking)
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

