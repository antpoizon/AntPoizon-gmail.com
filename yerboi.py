import selenium

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')
skip_button = driver.find_element_by_name('ytp-ad-skip-button ytp-button')
skip_button.click()
