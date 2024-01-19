import APEAutocorrelatorHandler
from tango import AttrWriteType, DevState, AttrWriteType, DispLevel, DebugIt
from tango.server import Device, attribute, command, device_property
from enum import IntEnum, Flag
import numpy as np

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
    _150fs = 1 #150
    _500fs = 2 #500
    _1500fs = 3 #1500
    _15ps = 4 #15000
    _150ps = 5 #150000

class sensEnum(IntEnum):
    _1 = 0 # 1
    _10 = 1 #10
    _100 = 2 #100


class APEAutocorrelator(Device):
    # device properties
    Host = device_property(
        dtype=str,
    )
    Port = device_property(
        dtype=int,
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
        dtype = str,
        unit = 'fs',
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
        dtype = int,
        unit = "us",
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
        dtype = ((float,),),
        max_dim_x=1024, 
        max_dim_y=1024,
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
        label='Crystal type',
        dtype = 'DevString',
        access = AttrWriteType.READ
    )


    def init_device(self):
        Device.init_device(self)
        print("test")
        self.debug_stream("init done")
        self.set_state(DevState.INIT)
        self.corr = APEAutocorrelatorHandler.APEAutocorrelatorHandler(self.Host, self.Port)
        self.set_state(DevState.ON)
        
    

    def read_averaging(self):
        self.debug_stream("in averageing")
        return self.corr.get_avg()

    def write_averaging(self,num):
        self.corr.set_avg(num)
        
    def read_res(self):
        return self.corr.get_res()

    def write_res(self,num):
        self.corr.set_res(num)

    def read_fitType(self):
        return self.corr.get_fit()

    def write_fitType(self,num):
        self.corr.set_fit(num)

    def read_measStatus(self):
        return self.corr.running()
    
    def read_filtering(self):
        return self.corr.get_filt()

    def write_filtering(self,num):
        self.corr.set_filt(num)
    
    def read_scanRange(self):
        return self.corr.get_scan()

    def write_scanRange(self,num):
        self.corr.set_scan(num)

    def read_gain(self):
        return self.corr.get_gain()

    def write_gain(self,num):
        self.corr.set_gain(num)

    def read_autoGain(self):
        return self.corr.get_autoGain()

    def write_autoGain(self,num):
        self.corr.set_autoGain(num)

    def read_sensitivity(self):
        return self.corr.get_sensitivity()

    def write_sensitivity(self,num):
        self.corr.set_sensitivity(num)

    def read_trigLvl(self):
        return self.corr.get_trigLvl()
    
    def read_trigDly(self):
        return self.corr.get_trigDly()

    def read_trigFrq(self):
        return self.corr.get_trigFrq()
    
    def read_trigImp(self):
        return self.corr.get_trigImp()
        
    def read_rawData(self):
        print(self.corr.get_rawData())
        return self.corr.get_rawData()

    def read_shutterFix(self):
        return self.corr.get_shutterFix()

    def write_shutterFix(self,num):
        self.corr.set_shutterFix(num)

    def read_shutterScan(self):
        return self.corr.get_shutterScan()

    def write_shutterScan(self,num):
        self.corr.set_shutterScan(num)

    def read_tune(self):
        return self.corr.get_tuning()

    def write_tune(self,num):
        self.corr.set_tuning(num)

    def read_lambdaTune(self):
        return self.corr.get_labdaTuning()

    def write_lambdaTune(self,num):
        self.corr.set_labdaTuning(num)
    
    def read_crystalMove(self):
        return self.corr.get_crysMove()

    def read_crystalType(self):
        return self.corr.get_crysType()
    
if __name__ == "__main__":
    APEAutocorrelator.run_server()


'''
        avereage ["OFF","LOW (2)","Medium (4)", High (8), Very high (16)]
        resolution [200,500,1000,1500,2000]

        '''