# -*- coding: utf-8 -*-

from ui.firstPap import Ui_FirstPapForm
from PyQt4 import QtCore, QtGui


class FirstPAP(QtGui.QWidget):
    def __init__(self, parentWidget):
        super(FirstPAP, self).__init__()
        self.ui = Ui_FirstPapForm()
        self.setupUi(parentWidget)

    def setupUi(self, parentWidget):
        self.ui.setupUi(parentWidget)

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

    def readCurrentConfig(self):
        for cmd in 'abcdefghikmnpqsvwz':
            self.emit(QtCore.SIGNAL("serialGet(PyQt_PyObject)"), cmd)

    def serialReply(self, reply):
        """
        Callback function (Qt slot) called when data is read on serial port
        :param reply: Data read
        """
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
