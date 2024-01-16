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

class fitEnum(IntEnum):
    OFF = 0
    GAUSSIAN = 1
    SECH2 = 2
    LORENTZ = 3

class scanEnum(IntEnum):
    _0 = 0
    _150fs = 150
    _500fs = 500
    _1500fs = 1500
    _15ps = 15000
    _150ps = 150000

class sensEnum(IntEnum):
    _1 = 1
    _10 = 10
    _100 = 100


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
    fitType = attribute(
        label= 'set the type of curve fit to apply to measured ACF',
        dtype= fitEnum,
        access= AttrWriteType.READ_WRITE
    )
    measStatus = attribute(
        label= 'Measurement running',
        dtype= "DevBoolean",
        access= AttrWriteType.READ
    )
    filtering = attribute(
        label= 'Set status of ACF filtering',
        dtype= "DevBoolean",
        access= AttrWriteType.READ_WRITE
    )
    scanRange = attribute(
        label = 'Set scan range',
        dtype = scanEnum,
        unit = fs,
        access = AttrWriteType.READ_WRITE
    )
    gain = attribute(
        label = 'Set gain value',
        dtype = 'DevLong',
        min_value = 300,
        max_value = 1000,
        access = AttrWriteType.READ_WRITE
    )
    autoGain = attribute(
        label = 'Activate automatic gain',
        dtype = 'DevBoolean',
        access = AttrWriteType.READ_WRITE
    )
    sensitivity = attribute(
        label = 'set sensitivity',
        dtype = sensEnum,
        access = AttrWriteType.READ_WRITE
    )
    trigLvl = attribute(
        label = 'Trigger level',
        dtype = 'DevLong',
        unit = 'mV',
        access = AttrWriteType.READ
    )
    trigDly = attribute(
        label = 'Trigger delay',
        dtype = 'DevLong',
        unit = 'us',
        access = AttrWriteType.READ
    )
    trigFrq = attribute(
        label = 'Trigger frequenzy',
        dtype = 'DevLong',
        unit = 'Hz',
        access = AttrWriteType.READ
    )
    trigImp = attribute(
        label = 'Trigger impeadence',
        dtype = 'DevLong',
        unit = 'Ohms',
        access = AttrWriteType.READ
    )
    rawData = attribute(
        label = 'Raw Data',
        dtype = 'DevVarDoubleArray',
        access = AttrWriteType.READ
    )
    rawData = attribute(
        label = 'Raw Data',
        dtype = 'DevVarDoubleArray',
        access = AttrWriteType.READ
    )
    ### more Data attributes to be added

    shutterFix = attribute(
        label = 'Set fix-shutter poition',
        dtype = 'DevBoolean',
        access = AttrWriteType.READ_WRITE
    )
    shutterScan = attribute(
        label = 'Set scan-shutter poition',
        dtype = 'DevBoolean',
        access = AttrWriteType.READ_WRITE
    )
    tune = attribute(
        label = 'Set crystal tuning poition',
        dtype = 'DevLong',
        min_value = 500,
        max_value = 11000,
        access = AttrWriteType.READ_WRITE
    )
    lambdaTune = attribute(
        label = 'Set crystal tuning i nm',
        dtype = 'DevLong',
        unit = 'nm',
        access = AttrWriteType.READ_WRITE
    )
    crystalMove = attribute(
        label = 'Status of crystal motor',
        dtype = 'DevBoolean',
        access = AttrWriteType.READ
    )
    crystalType = attribute(
        label = 'Crystal type',
        dtype = 'DevString',
        access = AttrWriteType.READ
    )


    def init_device(self):
        