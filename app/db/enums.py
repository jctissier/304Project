import enum

class Status(enum.Enum):
    ACTIVE = 'active'
    ASSOCIATE = 'associate'
    EXPIRED = 'expired'


class Pal(enum.Enum):
    NONE = ''
    NR = 'NR'
    R = 'R'


class Division(enum.Enum):
    OPEN = 'open'
    STANDARD = 'standard'
    CLASSIC = 'classic'
    PRODUCTION = 'production'
    REVOLVER = 'revolver'
    PRODUCTION_OPTICS = 'production optics'