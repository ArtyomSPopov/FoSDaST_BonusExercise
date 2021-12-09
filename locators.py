from selenium.webdriver.common.by import By

locator = {
    "button_contactUs"      : (By.ID, "contact-link"),
    "select_subjectHeading" : (By.ID, "id_contact"),
    "input_email"           : (By.ID, "email"),
    "input_orderReference"  : (By.ID, "id_order"),
    "textarea_message"      : (By.ID, "message"),
    "button_send"           : (By.ID, "submitMessage"),
    "text_alertMessage"     : (By.XPATH, "//*[text()='Your message has been successfully sent to our team.']"),
    "button_home"           : (By.XPATH, "/html/body/div/div[2]/div/div[3]/div/ul/li/a"),
}