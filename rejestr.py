from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import re
import time


class REJESTR:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

    def open_webpage(self):
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://rejestrcheb.mrit.gov.pl/wykaz-swiadectw-charakterystyki-energetycznej-budynkow")

        cookie_notice = self.driver.find_element(By.XPATH, '//*[@id="cookieNotice"]/a[2]')
        cookie_notice.click()

    def set_view_to_100(self):
        select = Select(self.driver.find_element(By.XPATH,
                                                 '//*[@id="ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__list_rowCount"]'))
        select.select_by_value("100")
        time.sleep(10)


    def get_record(self, id):
        record_data =[]

        element = self.driver.find_element(By.ID, f"ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__{id}")
        elements = element.find_elements(By.TAG_NAME, 'div')

        for e in elements:
            record_data.append(e.text)

        return record_data

    def go_to_next_page(self):
        right_arrow = self.driver.find_element(By.ID, 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__List___goNextPage')
        right_arrow.click()

    def get_number_of_record(self):
        string_with_number = self.driver.find_element(By.XPATH, '//*[@id="ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__view"]/table[3]/tbody/tr/td[2]')
        string_text = string_with_number.text
        print(string_text)
        list_number = re.findall(r'\d+(?: \d+)?(?: \d+)?', string_text)
        list_number[0] = list_number[0].replace(' ', '')
        number = list_number[0]
        return int(number)

    def filter_data_by_voivodeship(self, voivodeship):
        voivodeship_input = self.driver.find_element(By.ID, 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__conditionValue___7')
        voivodeship_input.send_keys(voivodeship)

        filter_data = self.driver.find_element(By.ID, 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__List___filter')
        filter_data.click()
        time.sleep(20)