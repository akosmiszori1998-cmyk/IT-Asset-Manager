import json
class ITSystem:
    def __init__(self):
        self.device_list = []

    def add_device(self,new_device):
        self.device_list.append(new_device)

    def inventory_stats(self):
        active_count = 0
        service_count = 0
        reject_count = 0

        for device in self.device_list:
            if device.state == "Active":
                active_count += 1
            elif device.state == "Service":
                service_count += 1
            elif device.state == "Reject":
                reject_count += 1
        print(f"Active: {active_count}")
        print(f"Service: {service_count}")
        print(f"Reject: {reject_count}")

            
    def save_to_json(self,filename):
        data_to_save = []

        for device in self.device_list:
            data_to_save.append(device.__dict__)

        with open(filename,"w") as f:
            json.dump(data_to_save, f, indent=4)
            print("Save successful")



    


