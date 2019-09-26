#-------------------------------------------------------------------------------
# Name:        Config_port_COM
# Author:      Perrot Cedric
# Created:     28/05/2015
# Copyright:   (c) Cedric 2015
#-------------------------------------------------------------------------------

import serial, time
import ConfigParser

def open_port_COM(Config_file,Section):

    i = 0
    while i < 10 :
        conf = ConfigParser.RawConfigParser()
        conf.read(Config_file)
        try:
            port = conf.get(Section,'port')
            baudrate = conf.getint(Section,'baudrate')
            bytesize = conf.getint(Section,'bytesize')
            parity = conf.get(Section,'parity')
            stopbits = conf.getint(Section,'stopbits')
            timeout = conf.getint(Section,'timeout')
            xonxoff = conf.getboolean(Section,'xonxoff')
            rtscts = conf.getboolean(Section,'rtscts')
            i = 11
            msg_erreur = ""
        except:
            msg_erreur = 'Err;Config_port_COM'
            i+=1
            time.sleep(0.2)

    try:
        ser = serial.Serial(port,baudrate,bytesize,parity,stopbits,timeout,xonxoff,rtscts)
    except :
        try:
            ser.close()
        except:
            return None,msg_erreur

    else:
        return ser,msg_erreur


if __name__ == '__main__':
    ser,msg = open_port_COM('Config_Balances.txt','ZO-BAL-03')
    print ser,msg
##    try:
##        if ser.isOpen() == False:
##            s = open_port_COM('Config_Stade.txt','port_com_xbee')
##        print 'Port COM ouvert'
##    except:
##        ser = open_port_COM('Config_Stade.txt','port_com_xbee')
