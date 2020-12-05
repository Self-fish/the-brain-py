from Core.data.device.NoSerialException import NoSerialException


def get_serial_number():
    try:
        serial = ""
        f = open('/proc/cpuinfo', 'r')
        for line in f:
            if line[0:6] == 'Serial':
                serial = line[10:26]
        f.close()
        if serial == "":
            raise NoSerialException
        return serial
    except:
        raise NoSerialException
