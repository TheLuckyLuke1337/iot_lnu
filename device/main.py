from machine import Pin
from time import sleep_ms

led = Pin(5, Pin.OUT)

sensor = Pin(0, Pin.IN)

led.value(0)
for _ in range(100):
    sensor_read = sensor.value()
    led.value(sensor_read)
    print(f"Sensor value = {sensor_read}")
    sleep_ms(200)
