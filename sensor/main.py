from machine import Pin, ADC
from time import sleep_ms


from sensor_utils import read_soil_sensor, analog2percent

led = Pin(5, Pin.OUT)

water_level = Pin(0, Pin.IN)
soil_moisture = ADC(0)
soil_moisture_power = Pin(28, Pin.OUT)

led.value(0)


for _ in range(100):
    sensor_read = water_level.value()
    led.value(sensor_read)
    # print(f"Sensor value = {sensor_read}")
    soil_read = read_soil_sensor(soil_moisture, soil_moisture_power)
    soil_moisture_power.value(1)
    print(analog2percent(soil_read), soil_read)
    soil_moisture_power.value(0)
    sleep_ms(200-10)
