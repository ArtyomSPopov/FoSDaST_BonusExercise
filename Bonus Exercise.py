from selenium import webdriver
from locators import locator
from csv import reader
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Edge(executable_path = '.\\msedgedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("http://automationpractice.com/")
driver.maximize_window()

with open('data.csv') as csvfile:
    csvreader = reader(csvfile, delimiter='—')
    for row in csvreader:

        # Click on the button "Contact us"
        assert driver.find_element(*locator["button_contactUs"]).is_displayed()
        driver.find_element(*locator["button_contactUs"]).click()

        # Check if the page is correct
        assert driver.title == "Contact us - My Store"

        # Select second value in "Subject Heading" selector
        select = Select(driver.find_element(*locator["select_subjectHeading"])).select_by_value("2")

        # Fill out the "Email address" field
        assert driver.find_element(*locator["input_email"]).is_displayed()
        driver.find_element(*locator["input_email"]).send_keys(row[0])
        
        # Fill out the "Order reference" field
        assert driver.find_element(*locator["input_orderReference"]).is_displayed()
        driver.find_element(*locator["input_orderReference"]).send_keys(row[1])
        
        # Fill out the "Message" field
        assert driver.find_element(*locator["textarea_message"]).is_displayed()
        driver.find_element(*locator["textarea_message"]).send_keys(row[2])

        # Click on the button "Send >"
        assert driver.find_element(*locator["button_send"]).is_displayed()
        driver.find_element(*locator["button_send"]).click()
        
        # Check if the shown message is correct one
        assert driver.find_element(*locator["text_alertMessage"]).is_displayed()

        # Click on the button "Home"
        assert driver.find_element(*locator["button_home"]).is_displayed()
        driver.find_element(*locator["button_home"]).click()

        # Show message in command prompt
        print("\n\n-----/  Bonus Exercise for 2 points is Completed! Hurray!!!  /-----\n----->  ©️ Popov Artem (DIY053)\n")
driver.quit()
