import time
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By




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