from attrs import define
from typing import Any


@define(frozen=True)
class SensorPacket:

    sensor_type: str
    sensor_value: Any


def main():
    print(SensorPacket("water_level_sensor", 1))


if __name__ == '__main__':
    main()
