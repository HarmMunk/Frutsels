from enum import Enum


class Channel(Enum):
    BROKER = 0
    WORKER = 1


for channel in Channel:
    print(channel)

