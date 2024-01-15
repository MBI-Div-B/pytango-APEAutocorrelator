import APEAutocorrelatorHandler
from tango import AttrWriteType, DevState, AttrWriteType, DispLevel, DebugIt
from tango.server import Device, attribute, command, device_property

class avgEnum(IntEnum):
    _0 = 0
    _2 = 1
    _4 = 2
    _8 = 3
    _16 = 4

class resEnum(IntEnum):
    _0 = 0
    _2 = 1
    _4 = 2
    _8 = 3
    _16 = 4


class APEAutocorrelator(Device):
    # device properties
    Host = device_property(
        dtype=str,
    )
    Port = device_property(
        dtype=str,
    )
    Baudrate = device_property(
        dtype=int,
        default_value=9600
    )

    averaging = attribute(
        label= 'set number of measurements used for averaging',
        dtype= avgEnum,
        access= AttrWriteType.READ_WRITE
    )
    res = attribute(
        label= 'set number of data points used for averaging',
        dtype= resEnum,
        access= AttrWriteType.READ_WRITE
    )
    


    def init_device(self):
        