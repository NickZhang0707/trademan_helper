from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


def auto_inspection(user_email, user_pw, bco, inspection_type, start_date, end_date, phone_number):
    chrome_binary_path = "./chrome-linux64"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_binary_path

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://onlineservices.aucklandcouncil.govt.nz/councilonline/login")
    driver.maximize_window()
    driver.implicitly_wait(10)

    try:
        # Login
        user_name_text_box = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder$txtUsername$txtUsername")
        next_button = driver.find_element(By.CSS_SELECTOR, "button")
        user_name_text_box.send_keys(user_email)
        sleep(0.5)
        next_button.click()
        driver.implicitly_wait(10)

        password_text_box = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder$txtPassword$txtPassword")
        password_text_box.send_keys(user_pw)
        sleep(0.5)
        next_button = driver.find_element(By.NAME, "btnSubmit")
        next_button.click()
        driver.implicitly_wait(10)

        # Navigate to booking page
        driver.get("https://onlineservices.aucklandcouncil.govt.nz/councilonline/inspection/consent-search?bookingType=single#/")

        bco_text_box = driver.find_element(By.NAME, "bcoReference")
        bco_text_box.send_keys(bco)
        bco_text_box.send_keys(Keys.ENTER)
        driver.implicitly_wait(10)

        driver.find_element(By.CLASS_NAME, "inspection-book-button").click()
        driver.implicitly_wait(10)

        dropdown = Select(driver.find_element(By.ID, "inspectionType"))
        dropdown.select_by_value(inspection_type)
        wait = WebDriverWait(driver, 10)
        next_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".inspection-next-btn.inspection-nav-button.pull-right")))
        next_btn.click()

        # Select date
        booking_successful = select_date_range(start_date=start_date, end_date=end_date, driver=driver)
        if not booking_successful:
            print("No available dates found in range")
            driver.quit()
            return False

        # Continue booking
        dropdown = Select(driver.find_element(By.ID, "inspectionTimeSlot"))
        dropdown.select_by_value("08:00:00-12:00:00")

        driver.find_element(By.ID, "readyNowYes").click()
        driver.find_element(By.ID, "onSiteContactOn").click()

        site_contact_input = driver.find_element(By.NAME, "siteContactNo")
        site_contact_input.send_keys(phone_number)

        next_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".inspection-next-btn.inspection-nav-button.pull-right")))
        next_btn.click()

        print("Booking submitted.")
        driver.quit()
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        driver.quit()
        return False


def select_date_range(start_date, end_date, driver):
    available_dates = driver.find_elements(By.CSS_SELECTOR, ".calendar-day-available")

    def extract_date(element):
        parent_id = element.find_element(By.XPATH, "./..").get_attribute("id")
        date_str = parent_id.split("_")[-1]
        return datetime.strptime(date_str, "%Y-%m-%d").date()

    for date_element in available_dates:
        try:
            date = extract_date(date_element)
            if start_date <= date <= end_date:
                date_element.click()
                print(f"Clicked on available date: {date}")
                return True
        except Exception as e:
            continue

    return False

user_email = "zznn49537@gmail.com"
user_pw = "CYM4sbjb!!!"
bco = "BCO10385714"
inspection_type = "ICL"
booking = False
start_date = datetime.strptime("2024-05-19", "%Y-%m-%d").date()
end_date = datetime.strptime("2025-05-19", "%Y-%m-%d").date()
phone_number = "0211365090"

while booking == False:
    
    booking = auto_inspection(user_email, user_pw, bco, inspection_type, start_date, end_date, phone_number)

