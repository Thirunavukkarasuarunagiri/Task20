from selenium import webdriver
import os
import time
import requests

# Function to create a folder
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

driver = webdriver.Chrome()

driver.get("https://www.labour.gov.in/")

# Task 1: Go to the Menu "Documents" and download the Monthly Progress Report
documents_menu = driver.find_element_by_xpath("//a[contains(text(), 'Documents')]")
documents_menu.click()
monthly_progress_report_link = driver.find_element_by_xpath("//a[contains(text(), 'Monthly Progress Report')]")
report_url = monthly_progress_report_link.get_attribute("href")
report_filename = "Monthly_Progress_Report.pdf"
response = requests.get(report_url)
with open(report_filename, "wb") as report_file:
    report_file.write(response.content)

# Task 2: Go to the Menu "Media" and download 10 photos from the "Photo Gallery" sub-menu
media_menu = driver.find_element_by_xpath("//a[contains(text(), 'Media')]")
media_menu.click()
photo_gallery_submenu = driver.find_element_by_xpath("//a[contains(text(), 'Photo Gallery')]")
photo_gallery_submenu.click()


folder_name = "Labour_Department_Photos"
create_folder(folder_name)


photo_links = driver.find_elements_by_xpath("//div[@class='photo-inner']/a")
for i, photo_link in enumerate(photo_links[:10], start=1):
    photo_url = photo_link.get_attribute("href")
    response = requests.get(photo_url)
    photo_filename = os.path.join(folder_name, f"photo_{i}.jpg")
    with open(photo_filename, "wb") as photo_file:
        photo_file.write(response.content)


driver.quit()