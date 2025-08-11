from os import wait
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def select_date_range(start_date, end_date, driver, booking):
    # Function to extract date from element's parent ID
    def extract_date(element):
        parent_id = element.find_element(By.XPATH, "./..").get_attribute("id")
        date_str = parent_id.split("_")[-1]  # Extract date part from ID like "zabuto_calendar_1nsh_2025-05-21"
        return datetime.strptime(date_str, "%Y-%m-%d").date()

    # Function to check if the range is available in current month view
    def is_range_available():
        available_dates = driver.find_elements(By.CSS_SELECTOR, ".calendar-day-available")
        available_dates_list = []
        
        for date_element in available_dates:
            try:
                date = extract_date(date_element)
                available_dates_list.append(date)
            except:
                continue
        
        # Check if all dates in range are available
        current_date = start_date
        while current_date <= end_date:
            if current_date not in available_dates_list:
                return False
            current_date += timedelta(days=1)
        return True

    # Try to find the date range in current month
    if is_range_available():
        # Click the start date
        available_dates = driver.find_elements(By.CSS_SELECTOR, ".calendar-day-available")
        for date_element in available_dates:
            try:
                date = extract_date(date_element)
                if date == start_date:
                    date_element.click()
                    print(f"Clicked on start date: {date}")
                    booking = True
                    break
            except:
                continue
        
        if booking:
            # Click the end date
            available_dates = driver.find_elements(By.CSS_SELECTOR, ".calendar-day-available")
            for date_element in available_dates:
                try:
                    date = extract_date(date_element)
                    if date == end_date:
                        date_element.click()
                        print(f"Clicked on end date: {date}")
                        break
                except:
                    continue
    else:
        # Try to navigate to next month
        try:
            next_button = driver.find_element(By.ID, "zabuto_calendar_1otk_nav-next")
            next_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".inspection-next-btn.inspection-nav-button.pull-right")))

            next_button.click()
            print("Navigated to next month")
            # Recursively try again in next month
            return select_date_range(start_date, end_date, driver, booking)
        except :
            print(driver.page_source)
            print("No more months available or next button not found")
            booking = False
    
    return booking
