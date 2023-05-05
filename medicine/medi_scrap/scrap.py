import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .find_search import search_medi_in_folder, return_searched_medi_dict

def get_driver():
    """
    Creates and returns an instance of Chrome webdriver
    """
    driver = webdriver.Chrome('/opt/homebrew/bin/chromedriver')
    return driver

def get_medicine_data(medicine_name):
    info = ''
    medicine_name = medicine_name.lower()
    if medicine_name:
        f_name = search_medi_in_folder(medicine_name)
        if f_name != None:
            info = return_searched_medi_dict(f_name)
        else:
            url = 'https://www.1mg.com/'
            driver = get_driver()

            medicine_url = search_medicine(driver, url, medicine_name)
            obj = MedicineInfoScraper(driver, medicine_url)
            info = obj.get_medicine_info()
            add_medi_info_to_file(info)
    return info

def add_medi_info_to_file(medicine_info):
    medicine_full_name = medicine_info['medicine_name'].lower()

    # write the medicine data to a JSON file
    with open(f"/Users/apple/Desktop/MediCare/medicine/medi_scrap/medi_data/{medicine_full_name}.json", "w") as f:
        json.dump(medicine_info, f)
    

def search_medicine(driver, url, medicine_name):
    """
    Navigates to the website and searches for the given medicine
    Returns the first search result href
    """
    try:
        driver.get(url)
        search_bar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="srchBarShwInfo"]')))
        search_bar.send_keys(medicine_name)
        search_bar.send_keys(Keys.RETURN)
        wait = WebDriverWait(driver, 10)
        first_result = wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "style__horizontal-card___1Zwmt")))
        a_tag = first_result.find_element(By.XPATH, ".//a")
        href = a_tag.get_attribute("href")
        return href
    except Exception as e:
        print(f"Error: {e}")


class MedicineInfoScraper:
    """
    A scraper that navigates to a medicine information page and returns various information about the medicine.
    """

    def __init__(self, driver, href):
        """
        Initializes the scraper with a WebDriver and the URL of the medicine information page.
        """
        self.driver = driver
        driver.get(href)

    def get_medicine_info(self):
        """
        Navigates to the given medicine information page and returns the following information about the medicine:
        - Medicine name
        - Manufacturer
        - Composition
        - Product Introduction
        - Uses of Medicine
        - Side effects Medicine
        - How to use
        - Safety Advices
        - Substitute
        """

        information = {}

        try:
            r_medicine_name = self.driver.find_element(
                By.XPATH, "//h1[@class='DrugHeader__title-content___2ZaPo']")
            r_medicine_name = r_medicine_name.text
        except:
            r_medicine_name = None
        information['medicine_name'] = r_medicine_name

        try:
            r_medicine_manufacturer = self.driver.find_element(
                By.XPATH, "//div[@class='DrugHeader__meta-value___vqYM0']")
            r_medicine_manufacturer = r_medicine_manufacturer.text
        except:
            r_medicine_manufacturer = None
        information['manufacturer'] = r_medicine_manufacturer

        try:
            r_medicine_composition = self.driver.find_element(
                By.XPATH, "//div[@class='saltInfo DrugHeader__meta-value___vqYM0']")
            r_medicine_composition = r_medicine_composition.text
        except:
            r_medicine_composition = None

        information['composition'] = r_medicine_composition.split(" + ")

        try:
            r_medicine_description = self.driver.find_element(
                By.XPATH, "//div[@class='DrugOverview__content___22ZBX']")
            r_medicine_description = r_medicine_description.text
        except:
            r_medicine_description = None

        information['introduction'] = r_medicine_description.split("\n\n")

        try:
            r_medicine_uses = self.driver.find_element(
                By.XPATH, "//ul[@class='DrugOverview__list___1HjxR DrugOverview__uses___1jmC3']")
            r_medicine_uses = r_medicine_uses.text
        except:
            r_medicine_uses = None

        information['uses'] = r_medicine_uses.split("\n")

        try:
            r_medicine_side_effects = self.driver.find_element(
                By.XPATH, "//div[@class='DrugOverview__list-container___2eAr6 DrugOverview__content___22ZBX']")
            r_medicine_side_effects = r_medicine_side_effects.text
        except:
            r_medicine_side_effects = None

        information['side_effects'] = r_medicine_side_effects.split("\n")

        try:
            r_medicine_how_to_use = self.driver.find_element(
                By.XPATH, "//div[@id='how_to_use']")
            r_medicine_how_to_use = r_medicine_how_to_use.text
        except:
            r_medicine_how_to_use = None

        temp = r_medicine_how_to_use.split("\n")
        information['how_to_use'] = temp[1]

        warning = []
        content = []
        try:
            r_medicine_warning = self.driver.find_element(By.XPATH, "//div[@id='safety_advice']").find_elements(
                By.XPATH, ".//div[@class='DrugOverview__warning-top___UD3xX']")

            r_medicine_content = self.driver.find_element(By.XPATH, "//div[@id='safety_advice']").find_element(
                By.XPATH, ".//div[@class='DrugOverview__content___22ZBX']").find_elements(By.XPATH, ".//div[@class='DrugOverview__content___22ZBX']")

            for i in r_medicine_warning:
                warning.append(i.find_element(By.XPATH, ".//span").text)

            for i in r_medicine_content:
                content.append(i.text)

            r_medicine_warning = r_medicine_warning.text
            r_medicine_content = r_medicine_content.text
        except:
            r_medicine_warning = None
            r_medicine_content = None

        new_dict = {}
        for i in range(len(warning)):
            new_dict[warning[i]] = content[i]

        information['safety_advice'] = new_dict

        new_dict3 = {}
        try:
            r_medicine_substitute = self.driver.find_elements(
                By.XPATH, "//div[@class='SubstituteItem__col-xs-6-custom___3c09J SubstituteItem__fLeft___9WQ2J']")
            for i in r_medicine_substitute:
                list = i.text.split("\n")
                new_dict3[list[0]] = list[1]
        except:
            r_medicine_substitute = None

        information['substitute'] = new_dict3

        return information
