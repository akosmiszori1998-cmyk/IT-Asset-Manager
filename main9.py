from devices import Devices
from system import ITSystem

my_company = ITSystem()

raw_data = ["Lenovo T480;150000;Active;Laptop",

"HP ProLiant;800000;Active;Server",

"Dell OptiPlex;20000;Unknown;Laptop"]

for data in raw_data:

    new_device = Devices.create_fromtext(data)
    
    my_company.add_device(new_device)

    print(new_device)

my_company.inventory_stats()
server_test = my_company.device_list[1]
server_test.error_report()

laptop_test = my_company.device_list[0]
laptop_test.error_report()

print("\n --- Exporting Data ---")
my_company.save_to_json("inventory.json")

