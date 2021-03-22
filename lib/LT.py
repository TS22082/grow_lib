import board
import busio
import adafruit_tsl2561

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2561.TSL2561(i2c)

sensor.gain = 0
sensor.integration_time = 1

def data():
	return {
		"lux" : sensor.lux, 
		"broadband" : sensor.broadband, 
		"infrared" : sensor.infrared, 
		"luminosity" : sensor.luminosity
		}

def display_data():
  lt_data = data()
  
  print("\n*** Data from tsl2561 sensor ***\n")
  print(f'Lux: {lt_data.get("lux")}')
  print(f'Broadband: {lt_data.get("broadband")}')
  print(f'Infrared: {lt_data.get("infrared")}')
  print(f'Luminosity: {lt_data.get("luminosity")}')
  print("\n-----------------------------")
