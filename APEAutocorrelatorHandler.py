import ape_device

class APEAutocorrelatorHandler(object):
    def __init__(self, host, port, name):
        dev = ape_device.ape_device(host, port, name)

    def get_avg(self):
        return int(ape_device.query("AVERAGE?"))
    def set_avg(self, num):
        ape_device.send("AVERAGE "+str(num))
    def get_res(self):
        return int(ape_device.query("RESOLUTION?"))
    def set_res(self, num):
        ape_device.send("RESOLUTION "+str(num))  
    def get_fit(self):
        return int(ape_device.query("FITTYPE?"))
    def set_fit(self, num):
        ape_device.send("FITTYPE "+str(num)) 
    def get_running(self):
        return bool(ape_device.query("START?"))
    def get_filt(self):
        return int(ape_device.query("FITTYPE?"))
    def set_filt(self, num):
        ape_device.send("FITTYPE "+str(int(num)))
    def get_scanrange(self):
        return int(ape_device.query("SCANRANGE?"))
    def set_scanrange(self, num):
        ape_device.send("SCANRANGE "+str(int(num)))
    def get_gain(self):
        return int(ape_device.query("GAIN?"))
    def set_gain(self, num):
        ape_device.send("GAIN "+str(int(num)))
    def get_autoGain(self):
        return int(ape_device.query("AUTOGAIN?"))
    def set_autoGain(self, num):
        ape_device.send("AUTOGAIN "+str(int(num)))
    def get_sensitivity(self):
        return int(ape_device.query("SENSITIVITY?"))
    def set_sensitivity(self, num):
        ape_device.send("SENSITIVITY "+str(int(num)))
    def get_trigLvl(self):
        return int(ape_device.query("LEVEL?"))
    def get_trigDly(self):
        return int(ape_device.query("DELAY?"))
    def get_trigFrq(self):
        return int(ape_device.query("FREQUENCY?"))
    def get_trigImp(self):
        return int(ape_device.query("IMP?"))
    def get_rawData(self):
        return ape_device.query("DATA?")
    ### not usre what data format to exlpect and how to extract
    ### to be done when device in avalablie 
    def get_shutterFix(self):
        return int(ape_device.query("FIX?"))
    def set_shutterFix(self, num):
        ape_device.send("FIX "+str(int(num)))
    def get_shutterScan(self):
        return int(ape_device.query("SCAN?"))
    def set_shutterScan(self, num):
        ape_device.send("SCAN "+str(int(num)))
    def get_tuning(self):
        return int(ape_device.query("TUNING?"))
    def set_tuning(self, num):
        ape_device.send("TUNING "+str(int(num)))
    def get_labdaTuning(self):
        return int(ape_device.query("LTU?"))
    def set_labdaTuning(self, num):
        ape_device.send("LTU "+str(int(num)))
    def get_crysMove(self):
        return int(ape_device.query("MOV?"))
    def get_crysType(self):
        return ape_device.query("SETXTAL?")
