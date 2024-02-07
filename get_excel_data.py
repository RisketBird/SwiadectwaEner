import pandas as pd

class READ_EXCEL():

    def __init__(self, file_path):
        """
        Tries to read excel file and store data into a dictionary.
        :param file_path: path to the.xlsx file.
        """
        try:
            if file_path.endswith('.xlsx'):
                self.data_file = pd.read_excel(file_path, keep_default_na=False)
                self.data_file_dict = self.data_file.to_dict(orient='records')
                print(self.data_file_dict)
            else:
                raise ValueError("Niewlaciwe rozszrzenie pliku.")
        except FileNotFoundError:
            print("Plik nie zostal odnaleziony.")
        except Exception as e:
            print(f"Error: {str(e)}")
            self.data_file = None
            self.data_file_dict = None

    def list_of_filters(self):
        """
        Converts read data form file and stores it in a list of lists.
        :return: list of lists of filters.
        """
        try:
            if self.data_file_dict is not None:

                filters_list = [[data.get('Data wystawienia', ''),
                                data.get('Data ważności', ''),
                                data.get('Miejscowość', ''),
                                data.get('Ulica', ''),
                                data.get('Nr budynku', ''),
                                data.get('Nr mieszkania', ''),
                                data.get('Województwo', ''),
                                data.get('Powiat', ''),
                                data.get('Gmina', ''),
                                ] for data in self.data_file_dict]

                return filters_list
            else:
                raise ValueError("No data to get data from")
        except Exception as e:
            print(f"Error: {str(e)}")
            return None

        # 1. - from date,
        # 2. - to date,
        # 3. - city,
        # 4. - street,
        # 5. - number,
        # 6. - flat number,
        # 7. - voivodeship,
        # 8. - county,
        # 9. - borough