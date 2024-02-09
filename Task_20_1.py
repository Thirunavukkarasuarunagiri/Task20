from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.cowin.gov.in/")

# Find and click on the "FAQ" anchor tag
faq_link = driver.find_element_by_xpath("//a[contains(text(), 'FAQ')]")
faq_link.click()

# Find and click on the "Partners" anchor tag
partners_link = driver.find_element_by_xpath("//a[contains(text(), 'Partners')]")
partners_link.click()

window_handles = driver.window_handles

# Task 2: Fetch and display the IDs of the opened windows
for handle in window_handles:
    driver.switch_to.window(handle)
    print("Window ID:", handle)

# Task 3: Close the new windows and switch back to the Home page
for handle in window_handles:
    driver.switch_to.window(handle)
    driver.close()

driver.switch_to.window(driver.window_handles[0])


driver.quit()