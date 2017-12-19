import enum


class Status(enum.Enum):
    ACTIVE = 0
    ASSOCIATE = 1
    EXPIRED = 2


class Pal(enum.Enum):
    NONE = 0
    NR = 1
    R = 2

class Division(enum.Enum):
    OPEN = 0
    STANDARD = 1
    CLASSIC = 2
    PRODUCTION = 3
    REVOLVER = 4
    PRODUCTION_OPTICS = 5