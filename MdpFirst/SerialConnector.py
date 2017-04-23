# -*- coding: utf-8 -*-

import re
import serial
from PyQt4 import QtCore


class SerialConnector(QtCore.QObject):
    def __init__(self, port):
        super(SerialConnector, self).__init__()
        self.isExiting = False

        self.transport = serial.Serial(port=port,
                                       baudrate=9600,
                                       bytesize=serial.EIGHTBITS,
                                       parity=serial.PARITY_NONE,
                                       stopbits=serial.STOPBITS_ONE,
                                       timeout=0.05)

    def __del__(self):
        self.isExiting = True

    def run(self):
        while not self.isExiting:
            pass

    def read(self):
        return self.transport.readline()

    def write(self, data):
        self.transport.write(data)

    def get(self, cmd):
        if len(cmd) != 1:
            raise ValueError("Command should be one character length.")

        if type(cmd) is str:
            cmd = cmd.encode()

        # Send command
        self.write(cmd + b"\r" if cmd[-1:] != b"\r" else cmd)

        # Read reply
        reply = self.read()\
            .replace(b"\r", b"") \
            .replace(b">", b"")\
            .decode()
        m = re.match(re.escape(cmd.decode()) + r"([0-9]{3})", reply)
        response = {
            'cmd': cmd.decode(),
            'value': m.group(1) if m else reply
        }
        self.emit(QtCore.SIGNAL("serialReply(PyQt_PyObject)"), response)

    def set(self, cmd, value):
        pass
