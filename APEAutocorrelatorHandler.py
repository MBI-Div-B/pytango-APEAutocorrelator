import ape_device

class APEAutocorrelatorHandler(object):
    def __init__(self, host, port, name):
        dev = ape_device.ape_device(host, port, name)

    