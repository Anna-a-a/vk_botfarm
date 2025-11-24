from enum import Enum


class UserEnv(str, Enum):
    PROD = 'PROD'
    PREPROD = 'PREPROD'
    STAGE = 'STAGE'