import json
from lib import DHT

with open("/home/pi/Documents/code/grow_lib/data/data.json", "r+") as f:
    data = json.load(f)  # load json from file as dictionary
    # store current lowest and highest recorded data
    lowest_tmp_recorded = data["lowest_temp"]
    highest_tmp_recorded = data["highest_temp"]
    # read data from sensors and save
    current_data = DHT.data()

    # initialise an object with starting values

    data_updated = {"lowest_temp": lowest_tmp_recorded,
                    "highest_temp": highest_tmp_recorded}

    if (current_data["tmp_f"] < lowest_tmp_recorded):
        data_updated["lowest_temp"] = current_data["tmp_f"]

    if (current_data["tmp_f"] > highest_tmp_recorded):
        data_updated["highest_temp"] = current_data["tmp_f"]

    f.seek(0)  # set cursor back to index 0 in file
    f.write(json.dumps(data_updated))  # write data
    f.truncate()  # resize file to current cursor position (0)
