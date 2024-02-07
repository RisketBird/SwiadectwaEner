from rejestr import REJESTR
from data_storage import EXCEL

rejestr = REJESTR()


rejestr.open_webpage()
rejestr.filter_data_with_parameters(["", "", "Ostrowiec Świętokrzyski", "", "", 12, "Świętokrzyskie", "Ostrowiecki", "Ostrowiec"])
rejestr.check_if_data_is_present()
number_of_record = rejestr.get_number_of_record()
rejestr.set_view_to_100(number_of_record)
# excel.create_new_sheet("Podlaskie")
#
counter = 0

for i in range(number_of_record):
    if counter <= 99:
        record_data = rejestr.get_record(i)
        # excel.add_record(record_data)
        counter = counter + 1
    else:
        # excel.save_file()
        rejestr.go_to_next_page()
        counter = 1
        record_data = rejestr.get_record(i)
        # excel.add_record(record_data)
    print(f"{i} {counter}")

# excel.save_file()
