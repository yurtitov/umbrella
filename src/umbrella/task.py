from enum import Enum


class Task:
    class Interval(Enum):
        MINUTES = 1
        HOURS = 2
        DAYS = 3

    def __init__(self, path: str, interval: Interval, every_unit: int):
        self.path = path
        self.interval = interval
        self.every_unit = every_unit
