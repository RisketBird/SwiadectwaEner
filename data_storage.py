from openpyxl import Workbook
from datetime import datetime


class EXCEL:

    def __init__(self, name=""):
        self.workbook = Workbook()
        self.sheet = self.workbook.active

        current_date_time = datetime.now()
        current_date = current_date_time.date()
        self.sheet.title = f"{name} {current_date}"
        self.workbook.active.append(["Utworzono", datetime.now().strftime("%d/%m/%Y %H:%M:%S")])

        self.workbook.save("Swiadectwa_eneregtyczne.xlsx")


    def add_record(self, list):
        self.workbook.active.append(list)

    def save_file(self):
        self.workbook.save("Swiadectwa_eneregtyczne.xlsx")

    def add_rejestr_headings(self):
        headings = ["Numer świadectwa", "Data wystawienia", "Ważne do (rrrr-mm-dd)", "Miejscowość", "Ulica", "Nr domu", "Nr lokalu", "Województwo", "Powiat", "Gmina", "Wskaźnik rocznego zapotrzebowania na energię użytkową EU [kWh/(m2·rok)]", "Wskaźnik rocznego zapotrzebowania na energię końcową EK [kWh/(m2·rok)]", "Wskaźnik rocznego zapotrzebowania na nieodnawialną energię pierwotną EP [kWh/(m2·rok)]", "Udział odnawialnych źródeł energii w rocznym zapotrzebowaniu na energię końcową UOZE[%]", "Jednostkowa wielkość emisji CO2 ECO2 [t CO2/(m2·rok)]"]
        self.workbook.active.append(headings)

    def add_address_headings(self):
        self.workbook.active.append([""])
        headings = ['Data wystawienia','Data ważności', 'Miejscowość', 'Ulica', 'Nr budynku', 'Nr mieszkania', 'Województwo', 'Powiat', 'Gmina']
        self.workbook.active.append(headings)
