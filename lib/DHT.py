import board
import adafruit_dht


dhtDevice = adafruit_dht.DHT22(board.D4)


def data():

    try:
        temp_c = dhtDevice.temperature
        temp_f = temp_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        data = {"tmp_c": temp_c, "tmp_f": temp_f, "humidity": humidity}
        return data

    except RunTimeError as error:
        print(error.args[0])
    except Exception as error:
        dht.exit()
        raise error


def display_data():
    dht_data = data()

    print("\n*** Data from DHT22 sensor ***\n")
    print(f'Celcius: {dht_data.get("tmp_c")}\u00b0C')
    print(f'Ferenheit: { round(dht_data.get("tmp_f"), 2)}\u00b0F')
    print(f'Humididty: {dht_data.get("humidity")}%')
    print("\n-----------------------------")
