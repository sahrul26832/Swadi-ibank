from enum import IntEnum, Enum

class StatEnum(IntEnum):
    Approve = 1
    Active = 1
    Pending = 8
    Cancel = -1
    Close = 0
    Error = -100

