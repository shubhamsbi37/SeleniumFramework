from selenium.webdriver.common.by import By


class Signup:
    fname_xpath = "//input[@name='RESULT_TextField-1']"
    lname_xpath = "//input[@name='RESULT_TextField-2']"
    phone_xpath = "//input[@name='RESULT_TextField-3']"
    country_xpath = "//input[@name='RESULT_TextField-4']"
    city_xpath = "//input[@name='RESULT_TextField-5']"
    email_xpath = "//input[@name='RESULT_TextField-6']"
    # male_xpath = "//table[@role='group']//tr/td/label[text()='Male']"
    radio_xpath = "//table[@role='group']//input[@type='radio']"

    def __init__(self, driver):
        self.driver = driver

    def fname(self, ename):
        self.driver.find_element(By.XPATH, self.fname_xpath).send_keys(ename)

    def lname(self, e_lname):
        self.driver.find_element(By.XPATH, self.lname_xpath).send_keys(e_lname)

    def phone(self, ephone):
        self.driver.find_element(By.XPATH, self.phone_xpath).send_keys(ephone)

    def country(self, ecountry):
        self.driver.find_element(By.XPATH, self.country_xpath).send_keys(ecountry)

    def city(self, ecity):
        self.driver.find_element(By.XPATH, self.city_xpath).send_keys(ecity)

    def email(self, e_email):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(e_email)

    def radio(self):
        try:
            all_radio = self.driver.find_elements(By.XPATH, self.radio_xpath)
            for i in all_radio:
                if i.get_attribute('ID') == "RESULT_RadioButton-7_0":
                    i.click()
                    break
        except Exception as e:
            print(f"Error occurred while selecting the radio button: {e}")


