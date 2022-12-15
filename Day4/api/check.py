
from models import *


def addLog(ts, hostname, phyint, serial):
    log = OLT(timestamp=ts, hostname=hostname, phyinterface=phyint,serialnumber=serial)
    log.save()

addLog('1 1:3', "1.1.3.4", '0/0/14', '1234567')