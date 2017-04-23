# -*- coding: utf-8 -*-

from FirstPAP import FirstPAP
from SerialConnector import SerialConnector
from ui.main import Ui_MainWindow
from PyQt4 import QtCore, QtGui
from serial.tools import list_ports
from serial import SerialException
import logging
import sys


class MdpFirst(QtGui.QMainWindow):
    def __init__(self):
        super(MdpFirst, self).__init__()

        self.ui = Ui_MainWindow()
        self.setupUi()

        logging.basicConfig(level=logging.DEBUG)

        self.fillSerialPortList()

        self.serialConnector = SerialConnector(None)
        self.thread = QtCore.QThread()

        self.firstModule = FirstPAP(self.ui.moduleWidget, self.serialConnector)

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.serialDisconnect_btn.setEnabled(False)
        QtCore.QObject.connect(self.ui.serialPortListRefresh_btn,
                               QtCore.SIGNAL("clicked()"),
                               self.fillSerialPortList)
        QtCore.QObject.connect(self.ui.serialConnect_btn,
                               QtCore.SIGNAL("clicked()"),
                               self.onSerialConnect)
        QtCore.QObject.connect(self.ui.serialDisconnect_btn,
                               QtCore.SIGNAL("clicked()"),
                               self.onSerialDisconnect)

    def closeEvent(self, event):
        """
        Reimplementation of QWidget.closeEvent()
        This event handler is called with the given event when Qt receives a window close request
        for a top-level widget from the window system.
        :param event: QCloseEvent
        """
        self.thread.quit()
        self.thread.wait()

    def fillSerialPortList(self):
        """
        Get the list of serial ports existing on the computer and fill the QComboBox
        Enable the "Connect" button if the list is not empty
        """
        self.ui.serialPortsList_cb.clear()
        availablePorts = list_ports.comports()
        for port in availablePorts:
            self.ui.serialPortsList_cb.addItem(port.device)

        self.ui.serialConnect_btn.setEnabled(not len(availablePorts) == 0)

    def onSerialConnect(self):
        """
        Function called when the user clicks on the "Connect" button
        Connect to the selected serial port and read data
        """
        port = self.ui.serialPortsList_cb.currentText()
        try:
            self.serialConnector.setPort(port)
            self.serialConnector.open()
        except SerialException as e:
            QtGui.QMessageBox.critical(self.ui.centralwidget,
                                       u"COM port error",
                                       u"An error occurred while trying to open serial port {} :\n{}".format(port, e),
                                       QtGui.QMessageBox.Ok)
            return
        self.serialConnector.moveToThread(self.thread)
        # application -> thread
        QtCore.QObject.connect(self,
                               QtCore.SIGNAL("serialGet(PyQt_PyObject)"),
                               self.serialConnector.get)
        # application <- thread
        QtCore.QObject.connect(self.serialConnector,
                               QtCore.SIGNAL("serialReply(PyQt_PyObject)"),
                               self.serialReply)

        self.thread.start()

        self.firstModule.readCurrentConfig()

        self.ui.serialConnect_btn.setEnabled(False)
        self.ui.serialDisconnect_btn.setEnabled(True)
        self.ui.serialPortsList_cb.setEnabled(False)
        self.ui.serialPortListRefresh_btn.setEnabled(False)

    def onSerialDisconnect(self):
        """
        Function called when the user clicks on the "Disconnect" button.
        Disconnect from serial port and release it
        """
        self.thread.quit()
        self.thread.wait()

        self.serialConnector.close()

        self.ui.serialConnect_btn.setEnabled(True)
        self.ui.serialDisconnect_btn.setEnabled(False)
        self.ui.serialPortsList_cb.setEnabled(True)
        self.ui.serialPortListRefresh_btn.setEnabled(True)

    def serialReply(self, reply):
        """
        Callback function (Qt slot) called when data is read on serial port
        :param reply: Data read
        """
        logging.info(reply)

        self.firstModule.serialReply(reply)


def MdpFirstApplication():
    app = QtGui.QApplication(sys.argv)

    w = MdpFirst()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    MdpFirstApplication()
