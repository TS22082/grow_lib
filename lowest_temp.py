import json
from lib import DHT

with open("/home/pi/Documents/code/grow_lib/data/data.json", "r+") as f:
  data = json.load(f) # load json from file as dictionary
  lowest_tmp_recorded = data["lowest_temp"] # store data as the lowest_tmp_recorded
  current_data = DHT.data() # save tmp to be compared with the lowest recorded tmp 

  # if current temp is lower than the lowest recorded tmp
  if (current_data["tmp_f"] < lowest_tmp_recorded) : 
    data_updated = {"lowest_temp" : current_data["tmp_f"]} # create dictionary with new lowest temp
    f.seek(0) # set cursor back to index 0 in file
    f.write(json.dumps(data_updated)) # write data
    f.truncate() # resize file to current cursor position (0)
    print("data.json modified")

