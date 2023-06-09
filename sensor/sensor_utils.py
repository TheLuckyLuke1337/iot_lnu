from time import sleep_ms


def read_dht_sensor(dht_sensor):
    try:
        dht_sensor.measure()
    except Exception as e:
        print(f"An error occurred: {e}")


def read_soil_sensor(soil_moisture, soil_moisture_power=None):
    """ Activates the sensor for 10 ms then reads the adc """
    # 16200 ~ 100%, 53450 ~ 0%

    reading = 0
    if soil_moisture_power:
        soil_moisture_power.value(1)
        sleep_ms(10)
        reading = soil_moisture.read_u16()
        soil_moisture_power.value(0)
    else:
        reading = soil_moisture.read_u16()
    return round(analog2percent(reading))


def analog2percent(x, in_min=53150, in_max=20200, out_min=0, out_max=100):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
