import json
from lib import DHT

with open("/home/pi/Documents/code/grow_lib/data/data.json", "r+") as f:
    data = json.load(f)  # load json from file as dictionary
    current_data = DHT.data()

    #compare current lowest temp with previously recorded lowest temp
    if (current_data["tmp_f"] < data["lowest_temp"]):
        #overwrite with current lowest temp
        data["lowest_temp"] = current_data["tmp_f"]

    #compare current highest temp with previously recorded highest temp
    if (current_data["tmp_f"] > data["highest_temp"]):
        #overwrite with current highest temp
        data["highest_temp"] = current_data["tmp_f"]

    f.seek(0)  # set cursor back to index 0 in file
    f.write(json.dumps(data))  # write data
    f.truncate()  # resize file to current cursor position (0)
