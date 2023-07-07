from attrs import define
from typing import Any


@define
class SensorPacket:

    sensor_type: str
    sensor_value: Any
    transmitted: bool = False

    def get_data(self):
        return self.sensor_type, self.sensor_value

    def has_been_transmitted(self):
        self.transmitted = True

    def get_data_for_transmition(self):
        self.has_been_transmitted()
        return self.get_data()


def main():
    print(SensorPacket("water_level_sensor", 1))


if __name__ == '__main__':
    main()
