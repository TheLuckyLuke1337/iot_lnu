import dht
from machine import Pin, ADC
from time import sleep_ms

from sensor_utils import read_soil_sensor, read_dht_sensor

DOWN_TIME = 20000    # PERIOD_TIME must be larger than
PUMPING_TIME = 20000   # PUMPING_TIME
MOISTURE_THRESHOLD = 50


dht_sensor = dht.DHT11(Pin(27))

water_sensor = Pin(0, Pin.IN)
water_pump = Pin(1, Pin.OUT)

soil_moisture_sensor = ADC(0)
soil_moisture_power = Pin(28, Pin.OUT)

while True:
    read_dht_sensor(dht_sensor)
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    water_level = water_sensor.value()
    soil_moisture = read_soil_sensor(soil_moisture_sensor, soil_moisture_power)
    print(f"Soil: {soil_moisture}% Water: {water_level}\n" +
          f"Temperature: {temperature} C Humidity: {humidity}%")
    water_pump.value(0)
    if water_level and soil_moisture < MOISTURE_THRESHOLD:
        water_pump.value(1)
        sleep_ms(PUMPING_TIME)
        sleep_ms(DOWN_TIME-PUMPING_TIME)
    else:
        sleep_ms(DOWN_TIME)
