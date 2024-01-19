import ape_device
import numpy as np

class APEAutocorrelatorHandler(object):
    def __init__(self, host, port, name = "Ape device"):
        self.dev = ape_device.ape_device(host, port, name)
        print(self.dev.idn())
    def get_avg(self):
        print("test1")
        print(self.dev.query(":status:fittype?"))
        test = self.dev.query(":status:average?")
        print("test")
        return test
    def set_avg(self, num):
        self.dev.send(":STATUS:AVERAGE "+str(num))
    def get_res(self):
        return int(self.dev.query(":STATUS:RESOLUTION?"))
    def set_res(self, num):
        self.dev.send(":STATUS:RESOLUTION "+str(num))  
    def get_fit(self):
        return int(self.dev.query(":STATUS:FITTYPE?"))
    def set_fit(self, num):
        self.dev.send(":STATUS:FITTYPE "+str(num)) 
    def get_running(self):
        return bool(self.dev.query(":STATUS:START?"))
    def get_filt(self):
        return int(self.dev.query(":STATUS:FILTER?"))
    def set_filt(self, num):
        self.dev.send(":STATUS:FILTER "+str(int(num)))
    def get_scan(self):
        return int(self.dev.query(":MOTOR:SCANRANGE?"))
    def set_scan(self, num):
        self.dev.send(":MOTOR:SCANRANGE "+str(int(num)))
    def get_gain(self):
        return int(self.dev.query(":DETECTOR:GAIN?"))
    def set_gain(self, num):
        self.dev.send(":DETECTOR:GAIN "+str(int(num)))
    def get_autoGain(self):
        return int(self.dev.query(":DETECTOR:AUTOGAIN?"))
    def set_autoGain(self, num):
        self.dev.send(":DETECTOR:AUTOGAIN "+str(int(num)))
    def get_sensitivity(self):
        return int(self.dev.query(":DETECTOR:SENSITIVITY?"))
    def set_sensitivity(self, num):
        self.dev.send(":DETECTOR:SENSITIVITY "+str(int(num)))
    def get_trigLvl(self):
        return int(self.dev.query(":TRIGGER:LEVEL?"))
    def get_trigDly(self):
        return int(self.dev.query(":TRIGGER:DELAY?"))
    def get_trigFrq(self):
        return int(self.dev.query(":TRIGGER:FREQUENCY?"))
    def get_trigImp(self):
        return int(self.dev.query(":TRIGGER:IMP?"))
    def get_rawData(self):
        acf_binary_data = bytes(self.dev.query(":ACF:DATA?",block=True))
        acf = np.fromstring(acf_binary_data, dtype=np.float64)
        acf = acf.reshape(2, int(acf.shape[0]/2))
        print(acf)
        return acf
    ### not usre what data format to exlpect and how to extract
    ### to be done when device in avalablie 
    def get_shutterFix(self):
        return int(self.dev.query(":SHUTTER:FIX?"))
    def set_shutterFix(self, num):
        self.dev.send(":SHUTTER:FIX "+str(int(num)))
    def get_shutterScan(self):
        return int(self.dev.query(":SHUTTER:SCAN?"))
    def set_shutterScan(self, num):
        self.dev.send(":SHUTTER:SCAN "+str(int(num)))
    def get_tuning(self):
        return int(self.dev.query(":XTAL:TUNING?"))
    def set_tuning(self, num):
        self.dev.send(":XTAL:TUNING "+str(int(num)))
    def get_labdaTuning(self):
        return int(self.dev.query(":XTAL:LTU?"))
    def set_labdaTuning(self, num):
        self.dev.send(":XTAL:LTU "+str(int(num)))
    def get_crysMove(self):
        return int(self.dev.query(":XTAL:MOV?"))
    def get_crysType(self):
        return self.dev.query(":XTAL:SETXTAL?")
