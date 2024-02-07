import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import re
import datetime


class REJESTR:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)  # run the WebDriver in the background.
        self.driver = webdriver.Chrome(options=self.chrome_options)  # creates a new instance of the Chrome WebDriver.
        # waits 60 sec before throwing a NoSuchElementException if an element is not immediately found
        self.driver.implicitly_wait(60)

    def open_webpage(self):
        """
        This function opens the webpage with certificates and clicks "Przejdz do serwisu" button on cookie notice.
        :return: nothing
        """
        self.driver.get("https://rejestrcheb.mrit.gov.pl/wykaz-swiadectw-charakterystyki-energetycznej-budynkow")

        cookie_notice = self.driver.find_element(By.XPATH, '//*[@id="cookieNotice"]/a[2]')
        cookie_notice.click()

    def set_view_to_100(self, number_of_records):
        """
        This function sets the view to 100 records.
        :return: nothing
        """
        select = Select(self.driver.find_element(By.ID,
                                                 'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__list_rowCount'))
        select.select_by_value("100")

        # Conditions to check weather the view was set corecctlly
        if number_of_records >= 100:
            self.driver.find_element(By.ID, "ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__99")
        else:
            self.driver.find_element(By.ID,
                                     f"ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__{number_of_records - 1}")

    def get_record(self, record_id):
        """
        This function gets row with data and returns it as a list.
        :param record_id: id of the record to get
        :return: whole row data
        """

        record_data = []

        element = self.driver.find_element(By.ID, f"ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__{record_id}")
        elements = element.find_elements(By.TAG_NAME, 'div')

        for e in elements:
            record_data.append(e.text)

        return record_data

    def go_to_next_page(self):
        """
        This function goes to the next page on webpage.
        :return: nothing
        """
        right_arrow = self.driver.find_element(By.ID,
                                               'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__List___goNextPage')
        right_arrow.click()

    def get_number_of_record(self):
        """
        This function gets the number of records available in the database and returns it as an int.
        :return: int number with number of records.
        """
        string_with_number = self.driver.find_element(By.XPATH,
                        '//*[@id="ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__view"]/table[3]/tbody/tr/td[2]')
        string_text = string_with_number.text
        list_number = re.findall(r'\d+(?: \d+)?(?: \d+)?', string_text)
        list_number[0] = list_number[0].replace(' ', '')
        number = list_number[0]
        return int(number)

    def filter_data(self):
        """
        This function clicks on "Filtruj" button.
        :return: nothing
        """
        filter_data = self.driver.find_element(By.ID,
                                               'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__List___filter')
        filter_data.click()

    def check_if_data_is_present(self):
        self.driver.implicitly_wait(10)  # set implicitly wait to 10
        try:
            self.driver.find_element(By.ID, 'nodata')
        except:
            print("Data are present.")
        else:
            print("Data not found.")

        self.driver.implicitly_wait(60)  # set implicitly wait back to 60

    def filter_data_by_voivodeship(self, voivodeship):
        """
        This function writes the given voivodeship in the box "Wojewodztwo".
        :param voivodeship: name of the voivodeship you want to filter by.
        :return: nothing.
        """
        voivodeship_input = self.driver.find_element(By.ID,
                                                'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__conditionValue___7')
        voivodeship_input.send_keys(voivodeship)

    def filter_data_by_from_date(self, date):
        """
        This function writes the given date in the box "Data wystawienia" and sets the condition to "mniejsze lub rowne"
        :param date: date to filter by.
        :return: nothing.
        """
        try:
            datetime.date.fromisoformat(date)
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        else:
            date_input = self.driver.find_element(By.ID,
                                                'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__conditionValue___1')
            date_input.send_keys(date)
            select = Select(self.driver.find_element(By.ID,
                                        'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__conditionComparator___1'))
            select.select_by_value("le")

            time.sleep(4)

    def filter_data_by_to_date(self, date):
        """
        This function writes the given date in the box "Wazne do..." and sets the condition to "mniejsze lub rowne".
        :param date: date to filter by.
        :return: nothing.
        """
        try:
            datetime.date.fromisoformat(date)
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        else:
            date_input = self.driver.find_element(By.ID,
                                                'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__conditionValue___2')
            date_input.send_keys(date)
            select = Select(self.driver.find_element(By.ID,
                                        'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__conditionComparator___2'))
            select.select_by_value("le")
            time.sleep(4)

    def filter_data_by_city(self, city):
        """
        This function writes the given city in the box "Miejscowosc".
        :param city: city to filter by.
        :return: nothing.
        """
        city_input = self.driver.find_element(By.ID,
                                              'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__conditionValue___3')
        city_input.send_keys(city)

    def filter_data_by_street(self, street):
        """
        This function writes the given street in the box "Ulica".
        :param street: street to filter by.
        :return: nothing.
        """
        street_input = self.driver.find_element(By.ID,
                                                'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__conditionValue___4')
        street_input.send_keys(street)

    def filter_data_by_number(self, number):
        """
        This function writes the given number in the box "Nr domu".
        :param number: number to filter by.
        :return: nothing.
        """
        number_input = self.driver.find_element(By.ID,
                                                'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__conditionValue___5')
        number_input.send_keys(number)

    def filter_data_by_flat_number(self, flat_number):
        """
        This function writes the given flat number in the box "Nr lokalu".
        :param flat_number: flat number to filter by.
        :return: nothing.
        """
        flat_number_input = self.driver.find_element(By.ID,
                                                'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__conditionValue___6')
        flat_number_input.send_keys(flat_number)

    def filter_data_by_county(self, county):
        """
        This function writes the given county in the box "Powiat".
        :param county: county to filter by.
        :return: nothing.
        """
        county_input = self.driver.find_element(By.ID,
                                                'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__conditionValue___8')
        county_input.send_keys(county)

    def filter_data_by_borough(self, borough):
        """
        This function writes the given borough in the box "Gmina"
        :param borough: borough to filter by.
        :return: nothing.
        """
        borough_input = self.driver.find_element(By.ID,
                                             'ox_bgk-sr_ZatwierdzoneSwiadectwoEnergetyczneWykaz__conditionValue___9')
        borough_input.send_keys(borough)

    def filter_data_with_parameters(self, filter_param):
        """
        This function filters the records by given filter_param.
        :param filter_param: list of paramters to filter by in this order:
            1. - from date,
            2. - to date,
            3. - city,
            4. - street,
            5. - number,
            6. - flat number,
            7. - voivodeship,
            8. - county,
            9. - borough
        :return: nothing
        """

        if len(filter_param) == 9:
            if filter_param[0]:
                self.filter_data_by_from_date(filter_param[0])
            if filter_param[1]:
                self.filter_data_by_to_date(filter_param[1])
            if filter_param[2]:
                self.filter_data_by_city(filter_param[2])
            if filter_param[3]:
                self.filter_data_by_street(filter_param[3])
            if filter_param[4]:
                self.filter_data_by_number(filter_param[4])
            if filter_param[5]:
                self.filter_data_by_flat_number(filter_param[5])
            if filter_param[6]:
                self.filter_data_by_voivodeship(filter_param[6])
            if filter_param[7]:
                self.filter_data_by_county(filter_param[7])
            if filter_param[8]:
                self.filter_data_by_borough(filter_param[8])

            self.filter_data()
        else:
            print("You have passed to little paramters.")
