import pandas as pd
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