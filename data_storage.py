from openpyxl import Workbook
from datetime import datetime


class EXCEL:

    def __init__(self):
        self.workbook = Workbook()
        self.sheet = self.workbook.active
        self.sheet.title = "Swiadectwa_eneregtyczne"
        self.workbook.save("Swiadectwa_eneregtyczne.xlsx")


    def add_record(self, list):
        self.workbook.active.append(list)

    def save_file(self):
        self.workbook.save("Swiadectwa_eneregtyczne.xlsx")

    def create_new_sheet(self, name):
        current_date_time = datetime.now()
        current_date = current_date_time.date()
        new_sheet = self.workbook.create_sheet(f"{name} {current_date}")
        self.workbook.active = new_sheet
        self.add_headings()

    def add_headings(self):
        headings = ["Numer świadectwa", "Data wystawienia", "Ważne do (rrrr-mm-dd)", "Miejscowość", "Ulica", "Nr domu", "Nr lokalu", "Województwo", "Powiat", "Gmina", "Wskaźnik rocznego zapotrzebowania na energię użytkową EU [kWh/(m2·rok)]", "Wskaźnik rocznego zapotrzebowania na energię końcową EK [kWh/(m2·rok)]", "Wskaźnik rocznego zapotrzebowania na nieodnawialną energię pierwotną EP [kWh/(m2·rok)]", "Udział odnawialnych źródeł energii w rocznym zapotrzebowaniu na energię końcową UOZE[%]", "Jednostkowa wielkość emisji CO2 ECO2 [t CO2/(m2·rok)]"]
        self.workbook.active.append(headings)