# -*- coding: utf-8 -*-

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

        self.serialConnector = None
        self.thread = QtCore.QThread()

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
        QtCore.QObject.connect(self.ui.cmdMode_cb,
                               QtCore.SIGNAL("currentIndexChanged(int)"),
                               self.onSelectionChange)
        QtCore.QObject.connect(self.ui.fctMode_cb,
                               QtCore.SIGNAL("currentIndexChanged(int)"),
                               self.onSelectionChange)
        QtCore.QObject.connect(self.ui.microStep_cb,
                               QtCore.SIGNAL("currentIndexChanged(int)"),
                               self.onSelectionChange)
        QtCore.QObject.connect(self.ui.currentFault_cb,
                               QtCore.SIGNAL("currentIndexChanged(int)"),
                               self.onSelectionChange)
        QtCore.QObject.connect(self.ui.currentProfile_cb,
                               QtCore.SIGNAL("currentIndexChanged(int)"),
                               self.onSelectionChange)
        QtCore.QObject.connect(self.ui.currentRange_cb,
                               QtCore.SIGNAL("currentIndexChanged(int)"),
                               self.onSelectionChange)

        QtCore.QObject.connect(self.ui.nominalCurrent,
                               QtCore.SIGNAL("valueChanged(double)"),
                               self.onValueChange)
        QtCore.QObject.connect(self.ui.nominalTime,
                               QtCore.SIGNAL("valueChanged(int)"),
                               self.onValueChange)
        QtCore.QObject.connect(self.ui.maintainCurrent,
                               QtCore.SIGNAL("valueChanged(double)"),
                               self.onValueChange)
        QtCore.QObject.connect(self.ui.maintainTime,
                               QtCore.SIGNAL("valueChanged(int)"),
                               self.onValueChange)
        QtCore.QObject.connect(self.ui.boostCurrent,
                               QtCore.SIGNAL("valueChanged(double)"),
                               self.onValueChange)
        QtCore.QObject.connect(self.ui.boostTime,
                               QtCore.SIGNAL("valueChanged(double)"),
                               self.onValueChange)
        QtCore.QObject.connect(self.ui.maxSpeed,
                               QtCore.SIGNAL("valueChanged(int)"),
                               self.onValueChange)
        QtCore.QObject.connect(self.ui.fastDecay,
                               QtCore.SIGNAL("valueChanged(int)"),
                               self.onValueChange)
        QtCore.QObject.connect(self.ui.deadband,
                               QtCore.SIGNAL("valueChanged(int)"),
                               self.onValueChange)
        QtCore.QObject.connect(self.ui.filterTime,
                               QtCore.SIGNAL("valueChanged(int)"),
                               self.onValueChange)

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
            self.serialConnector = SerialConnector(port)
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
        # thread -> application
        QtCore.QObject.connect(self.serialConnector,
                               QtCore.SIGNAL("serialReply(PyQt_PyObject)"),
                               self.serialReply)
        # QtCore.QObject.connect(self.serialConnector,
        #                        QtCore.SIGNAL("serialReply(PyQt_PyObject)"),
        #                        lambda value, func=self.serialReply: func(value, "bla"))

        self.thread.start()

        for cmd in 'abcdefghikmnpqsvwz':
            self.emit(QtCore.SIGNAL("serialGet(PyQt_PyObject)"), cmd)

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

        self.serialConnector = None

        self.ui.serialConnect_btn.setEnabled(True)
        self.ui.serialDisconnect_btn.setEnabled(False)
        self.ui.serialPortsList_cb.setEnabled(True)
        self.ui.serialPortListRefresh_btn.setEnabled(True)

    def serialReply(self, reply):
        logging.info(reply)
        try:
            cmd = reply['cmd'].lower()
            value = reply['value']
        except (KeyError, AttributeError):
            cmd = ""
            value = None

        if cmd == "a":  # Lecture du temps de maintien
            self.ui.maintainTime.blockSignals(True)
            self.ui.maintainTime.setValue(int(value) * 10)
            self.ui.maintainTime.blockSignals(False)
        elif cmd == "b":  # Lecture du courant de boost
            self.ui.boostCurrent.blockSignals(True)
            self.ui.boostCurrent.setValue(float(value) / 10)
            self.ui.boostCurrent.blockSignals(False)
        elif cmd == "c":  # Lecture de la configuration de commande
            self.ui.cmdMode_cb.blockSignals(True)
            self.ui.cmdMode_cb.setCurrentIndex(int(value[1]))
            self.ui.cmdMode_cb.blockSignals(False)

            self.ui.fctMode_cb.blockSignals(True)
            self.ui.fctMode_cb.setCurrentIndex(int(value[2]))
            self.ui.fctMode_cb.blockSignals(False)
        elif cmd == "d":  # Lecture de l'état de la carte
            # TODO: Afficher les données
            pass
        elif cmd == "e":  # Lecture de la zone morte de la consigne analogique
            self.ui.deadband.blockSignals(True)
            self.ui.deadband.setValue(int(value) * 10)
            self.ui.deadband.blockSignals(False)
        elif cmd == "f":  # Lecture du sens de rotation (pilotage par PC)
            # TODO: Afficher les données
            pass
        elif cmd == "g":  # Lecture de la gamme de courant
            self.ui.currentRange_cb.blockSignals(True)
            self.ui.currentRange_cb.setCurrentIndex(int(value))
            self.ui.currentRange_cb.blockSignals(False)
        elif cmd == "h":  # Lecture de la vitesse max. pour commande en consigne analogique
            self.ui.maxSpeed.blockSignals(True)
            self.ui.maxSpeed.setValue(int(value) * 100)
            self.ui.maxSpeed.blockSignals(False)
        elif cmd == "i":  # Lecture de l'identifiant de la carte
            pass
        elif cmd == "k":  # Lecture du temps d'établissement pour les entrées Sens et Enable
            self.ui.filterTime.blockSignals(True)
            self.ui.filterTime.setValue(int(value) * 8)
            self.ui.filterTime.blockSignals(False)
        elif cmd == "m":  # Lecture du courant de maintien
            self.ui.maintainCurrent.blockSignals(True)
            self.ui.maintainCurrent.setValue(float(value) / 10)
            self.ui.maintainCurrent.blockSignals(False)
        elif cmd == "n":  # Lecture du courant nominal
            self.ui.nominalCurrent.blockSignals(True)
            self.ui.nominalCurrent.setValue(float(value) / 10)
            self.ui.nominalCurrent.blockSignals(False)
        elif cmd == "p":  # Lecture du fast decay
            self.ui.fastDecay.blockSignals(True)
            self.ui.fastDecay.setValue(int(value))
            self.ui.fastDecay.blockSignals(False)
        elif cmd == "q":  # lecture du temps nominal
            self.ui.nominalTime.blockSignals(True)
            self.ui.nominalTime.setValue(int(value))
            self.ui.nominalTime.blockSignals(False)
        elif cmd == "s":  # Lecture de la configuration de micro pas
            self.ui.microStep_cb.blockSignals(True)
            self.ui.microStep_cb.setCurrentIndex(int(value))
            self.ui.microStep_cb.blockSignals(False)
        elif cmd == "v":  # Lecture de la consigne de vitesse (pilotage par PC)
            # TODO: Afficher les données
            pass
        elif cmd == "w":  # Lecture du temps de boost
            self.ui.boostTime.blockSignals(True)
            self.ui.boostTime.setValue(float(value) / 10)
            self.ui.boostTime.blockSignals(False)
        elif cmd == "z":  # Lecture du profil de courant
            self.ui.currentProfile_cb.blockSignals(True)
            self.ui.currentProfile_cb.setCurrentIndex(int(value[2]))
            self.ui.currentProfile_cb.blockSignals(False)

            self.ui.currentFault_cb.blockSignals(True)
            self.ui.currentFault_cb.setCurrentIndex(int(value[1]))
            self.ui.currentFault_cb.blockSignals(False)

    def onSelectionChange(self, idx):
        print("Selection changed %s %s" % (idx, self.sender()))

    def onValueChange(self, idx):
        print("Value changed %s %s" % (idx, self.sender()))


def main():
    app = QtGui.QApplication(sys.argv)

    w = MdpFirst()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
