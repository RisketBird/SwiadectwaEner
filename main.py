from rejestr import REJESTR
from data_storage import EXCEL
from get_excel_data import READ_EXCEL

data_to_filter_by = READ_EXCEL('/Users/kamil/Desktop/Test_data.xlsx')
filters_list = data_to_filter_by.list_of_filters()

rejestr = REJESTR()
excel = EXCEL()

for filters in filters_list:
    excel.add_address_headings()
    excel.add_record(filters)

    rejestr.filter_data_with_parameters(filters)

    if not rejestr.check_if_data_is_present():
        excel.add_record(["Nie znaleziono danych"])
        continue

    excel.add_rejestr_headings()
    number_of_record = rejestr.get_number_of_record()
    counter = 0
    for i in range(number_of_record):
        if counter <= 9:
            record_data = rejestr.get_record(i)
            excel.add_record(record_data)
            counter = counter + 1
        else:
            rejestr.go_to_next_page()
            counter = 1
            record_data = rejestr.get_record(i)
            excel.add_record(record_data)
        print(f"{i} {counter}")

excel.save_file()

rejestr.close_web_browser()




