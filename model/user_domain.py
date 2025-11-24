from enum import Enum


class UserDomain(str, Enum):
    CANARY = 'CANARY'
    REGULAR = 'REGULAR'