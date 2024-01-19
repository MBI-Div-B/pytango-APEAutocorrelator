import ape_device

class APEAutocorrelatorHandler(object):
    def __init__(self, host, port, name = "Ape device"):
        self.dev = ape_device.ape_device(host, port, name)
        print(self.dev.idn())
    def get_avg(self):
        print("test1")
        test = int(self.dev.query("*AVERAGE?"))
        print("test")
        return test
    def set_avg(self, num):
        self.dev.send("AVERAGE "+str(num))
    def get_res(self):
        return int(self.dev.query("RESOLUTION?"))
    def set_res(self, num):
        self.dev.send("RESOLUTION "+str(num))  
    def get_fit(self):
        return int(self.dev.query("FITTYPE?"))
    def set_fit(self, num):
        self.dev.send("FITTYPE "+str(num)) 
    def get_running(self):
        return bool(self.dev.query("START?"))
    def get_filt(self):
        return int(self.dev.query("FITTYPE?"))
    def set_filt(self, num):
        self.dev.send("FITTYPE "+str(int(num)))
    def get_scan(self):
        return int(self.dev.query("SCANRANGE?"))
    def set_scan(self, num):
        self.dev.send("SCANRANGE "+str(int(num)))
    def get_gain(self):
        return int(self.dev.query("GAIN?"))
    def set_gain(self, num):
        self.dev.send("GAIN "+str(int(num)))
    def get_autoGain(self):
        return int(self.dev.query("AUTOGAIN?"))
    def set_autoGain(self, num):
        self.dev.send("AUTOGAIN "+str(int(num)))
    def get_sensitivity(self):
        return int(self.dev.query("SENSITIVITY?"))
    def set_sensitivity(self, num):
        self.dev.send("SENSITIVITY "+str(int(num)))
    def get_trigLvl(self):
        return int(self.dev.query("LEVEL?"))
    def get_trigDly(self):
        return int(self.dev.query("DELAY?"))
    def get_trigFrq(self):
        return int(self.dev.query("FREQUENCY?"))
    def get_trigImp(self):
        return int(self.dev.query("IMP?"))
    def get_rawData(self):
        return self.dev.query("DATA?")
    ### not usre what data format to exlpect and how to extract
    ### to be done when device in avalablie 
    def get_shutterFix(self):
        return int(self.dev.query("FIX?"))
    def set_shutterFix(self, num):
        self.dev.send("FIX "+str(int(num)))
    def get_shutterScan(self):
        return int(self.dev.query("SCAN?"))
    def set_shutterScan(self, num):
        self.dev.send("SCAN "+str(int(num)))
    def get_tuning(self):
        return int(self.dev.query("TUNING?"))
    def set_tuning(self, num):
        self.dev.send("TUNING "+str(int(num)))
    def get_labdaTuning(self):
        return int(self.dev.query("LTU?"))
    def set_labdaTuning(self, num):
        self.dev.send("LTU "+str(int(num)))
    def get_crysMove(self):
        return int(self.dev.query("MOV?"))
    def get_crysType(self):
        return self.dev.query("SETXTAL?")
