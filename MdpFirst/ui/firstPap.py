# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstPap.ui'
#
# Created: Sun Apr 23 23:40:39 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FirstPapForm(object):
    def setupUi(self, FirstPapForm):
        FirstPapForm.setObjectName(_fromUtf8("FirstPapForm"))
        FirstPapForm.resize(437, 426)
        self.formLayout = QtGui.QFormLayout(FirstPapForm)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.cmdMode_cb = QtGui.QComboBox(FirstPapForm)
        self.cmdMode_cb.setObjectName(_fromUtf8("cmdMode_cb"))
        self.cmdMode_cb.addItem(_fromUtf8(""))
        self.cmdMode_cb.addItem(_fromUtf8(""))
        self.cmdMode_cb.addItem(_fromUtf8(""))
        self.cmdMode_cb.addItem(_fromUtf8(""))
        self.cmdMode_cb.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cmdMode_cb)
        self.label_22 = QtGui.QLabel(FirstPapForm)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_22)
        self.fctMode_cb = QtGui.QComboBox(FirstPapForm)
        self.fctMode_cb.setObjectName(_fromUtf8("fctMode_cb"))
        self.fctMode_cb.addItem(_fromUtf8(""))
        self.fctMode_cb.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.fctMode_cb)
        self.label_21 = QtGui.QLabel(FirstPapForm)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_21)
        self.microStep_cb = QtGui.QComboBox(FirstPapForm)
        self.microStep_cb.setObjectName(_fromUtf8("microStep_cb"))
        self.microStep_cb.addItem(_fromUtf8(""))
        self.microStep_cb.addItem(_fromUtf8(""))
        self.microStep_cb.addItem(_fromUtf8(""))
        self.microStep_cb.addItem(_fromUtf8(""))
        self.microStep_cb.addItem(_fromUtf8(""))
        self.microStep_cb.addItem(_fromUtf8(""))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.microStep_cb)
        self.label_20 = QtGui.QLabel(FirstPapForm)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_20)
        self.currentFault_cb = QtGui.QComboBox(FirstPapForm)
        self.currentFault_cb.setObjectName(_fromUtf8("currentFault_cb"))
        self.currentFault_cb.addItem(_fromUtf8(""))
        self.currentFault_cb.addItem(_fromUtf8(""))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.currentFault_cb)
        self.label_19 = QtGui.QLabel(FirstPapForm)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_19)
        self.currentProfile_cb = QtGui.QComboBox(FirstPapForm)
        self.currentProfile_cb.setObjectName(_fromUtf8("currentProfile_cb"))
        self.currentProfile_cb.addItem(_fromUtf8(""))
        self.currentProfile_cb.addItem(_fromUtf8(""))
        self.currentProfile_cb.addItem(_fromUtf8(""))
        self.currentProfile_cb.addItem(_fromUtf8(""))
        self.currentProfile_cb.addItem(_fromUtf8(""))
        self.currentProfile_cb.addItem(_fromUtf8(""))
        self.currentProfile_cb.addItem(_fromUtf8(""))
        self.currentProfile_cb.addItem(_fromUtf8(""))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.currentProfile_cb)
        self.label_18 = QtGui.QLabel(FirstPapForm)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_18)
        self.currentRange_cb = QtGui.QComboBox(FirstPapForm)
        self.currentRange_cb.setObjectName(_fromUtf8("currentRange_cb"))
        self.currentRange_cb.addItem(_fromUtf8(""))
        self.currentRange_cb.addItem(_fromUtf8(""))
        self.currentRange_cb.addItem(_fromUtf8(""))
        self.currentRange_cb.addItem(_fromUtf8(""))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.currentRange_cb)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.groupBox_5 = QtGui.QGroupBox(FirstPapForm)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.formLayout_6 = QtGui.QFormLayout(self.groupBox_5)
        self.formLayout_6.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.label_23 = QtGui.QLabel(self.groupBox_5)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_23)
        self.nominalCurrent = QtGui.QDoubleSpinBox(self.groupBox_5)
        self.nominalCurrent.setDecimals(1)
        self.nominalCurrent.setMaximum(5.0)
        self.nominalCurrent.setSingleStep(0.1)
        self.nominalCurrent.setObjectName(_fromUtf8("nominalCurrent"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.FieldRole, self.nominalCurrent)
        self.label_24 = QtGui.QLabel(self.groupBox_5)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_24)
        self.nominalTime = QtGui.QSpinBox(self.groupBox_5)
        self.nominalTime.setMinimum(0)
        self.nominalTime.setMaximum(99)
        self.nominalTime.setSingleStep(1)
        self.nominalTime.setObjectName(_fromUtf8("nominalTime"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.FieldRole, self.nominalTime)
        self.horizontalLayout_2.addWidget(self.groupBox_5)
        self.groupBox_6 = QtGui.QGroupBox(FirstPapForm)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.formLayout_7 = QtGui.QFormLayout(self.groupBox_6)
        self.formLayout_7.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_7.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_7.setObjectName(_fromUtf8("formLayout_7"))
        self.label_25 = QtGui.QLabel(self.groupBox_6)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_25)
        self.maintainCurrent = QtGui.QDoubleSpinBox(self.groupBox_6)
        self.maintainCurrent.setDecimals(1)
        self.maintainCurrent.setMinimum(0.0)
        self.maintainCurrent.setMaximum(5.0)
        self.maintainCurrent.setSingleStep(0.1)
        self.maintainCurrent.setObjectName(_fromUtf8("maintainCurrent"))
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.FieldRole, self.maintainCurrent)
        self.label_26 = QtGui.QLabel(self.groupBox_6)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.formLayout_7.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_26)
        self.maintainTime = QtGui.QSpinBox(self.groupBox_6)
        self.maintainTime.setMinimum(0)
        self.maintainTime.setMaximum(990)
        self.maintainTime.setSingleStep(10)
        self.maintainTime.setObjectName(_fromUtf8("maintainTime"))
        self.formLayout_7.setWidget(1, QtGui.QFormLayout.FieldRole, self.maintainTime)
        self.horizontalLayout_2.addWidget(self.groupBox_6)
        self.groupBox_7 = QtGui.QGroupBox(FirstPapForm)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.formLayout_8 = QtGui.QFormLayout(self.groupBox_7)
        self.formLayout_8.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_8.setObjectName(_fromUtf8("formLayout_8"))
        self.label_27 = QtGui.QLabel(self.groupBox_7)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.formLayout_8.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_27)
        self.boostCurrent = QtGui.QDoubleSpinBox(self.groupBox_7)
        self.boostCurrent.setDecimals(1)
        self.boostCurrent.setMinimum(0.0)
        self.boostCurrent.setMaximum(5.0)
        self.boostCurrent.setSingleStep(0.1)
        self.boostCurrent.setObjectName(_fromUtf8("boostCurrent"))
        self.formLayout_8.setWidget(0, QtGui.QFormLayout.FieldRole, self.boostCurrent)
        self.boostTime = QtGui.QDoubleSpinBox(self.groupBox_7)
        self.boostTime.setDecimals(1)
        self.boostTime.setMinimum(0.0)
        self.boostTime.setMaximum(9.9)
        self.boostTime.setSingleStep(0.1)
        self.boostTime.setObjectName(_fromUtf8("boostTime"))
        self.formLayout_8.setWidget(1, QtGui.QFormLayout.FieldRole, self.boostTime)
        self.label_28 = QtGui.QLabel(self.groupBox_7)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.formLayout_8.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_28)
        self.horizontalLayout_2.addWidget(self.groupBox_7)
        spacerItem1 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.formLayout.setLayout(6, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_2)
        self.label_29 = QtGui.QLabel(FirstPapForm)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_29)
        self.label_30 = QtGui.QLabel(FirstPapForm)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_30)
        self.label_31 = QtGui.QLabel(FirstPapForm)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_31)
        self.maxSpeed = QtGui.QSpinBox(FirstPapForm)
        self.maxSpeed.setMinimum(100)
        self.maxSpeed.setMaximum(9900)
        self.maxSpeed.setSingleStep(100)
        self.maxSpeed.setObjectName(_fromUtf8("maxSpeed"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.maxSpeed)
        self.fastDecay = QtGui.QSpinBox(FirstPapForm)
        self.fastDecay.setMaximum(15)
        self.fastDecay.setObjectName(_fromUtf8("fastDecay"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.fastDecay)
        self.deadband = QtGui.QSpinBox(FirstPapForm)
        self.deadband.setMinimum(100)
        self.deadband.setMaximum(10090)
        self.deadband.setSingleStep(10)
        self.deadband.setObjectName(_fromUtf8("deadband"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.deadband)
        self.label_32 = QtGui.QLabel(FirstPapForm)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_32)
        self.filterTime = QtGui.QSpinBox(FirstPapForm)
        self.filterTime.setMaximum(7992)
        self.filterTime.setSingleStep(8)
        self.filterTime.setObjectName(_fromUtf8("filterTime"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.filterTime)
        self.label_11 = QtGui.QLabel(FirstPapForm)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_11)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.eepromSave_btn = QtGui.QPushButton(FirstPapForm)
        self.eepromSave_btn.setMinimumSize(QtCore.QSize(160, 40))
        self.eepromSave_btn.setObjectName(_fromUtf8("eepromSave_btn"))
        self.horizontalLayout.addWidget(self.eepromSave_btn)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.formLayout.setLayout(11, QtGui.QFormLayout.SpanningRole, self.horizontalLayout)

        self.retranslateUi(FirstPapForm)
        QtCore.QMetaObject.connectSlotsByName(FirstPapForm)

    def retranslateUi(self, FirstPapForm):
        FirstPapForm.setWindowTitle(_translate("FirstPapForm", "Form", None))
        self.cmdMode_cb.setItemText(0, _translate("FirstPapForm", "Horloge/Sens", None))
        self.cmdMode_cb.setItemText(1, _translate("FirstPapForm", "CW/CCW", None))
        self.cmdMode_cb.setItemText(2, _translate("FirstPapForm", "EnableCW/EnableCCW", None))
        self.cmdMode_cb.setItemText(3, _translate("FirstPapForm", "Consigne analogique/Sens", None))
        self.cmdMode_cb.setItemText(4, _translate("FirstPapForm", "Pilotage par PC", None))
        self.label_22.setText(_translate("FirstPapForm", "Config Fdc :", None))
        self.fctMode_cb.setItemText(0, _translate("FirstPapForm", "Avec fin de course", None))
        self.fctMode_cb.setItemText(1, _translate("FirstPapForm", "Avec boost et maintien", None))
        self.label_21.setText(_translate("FirstPapForm", "Micro pas :", None))
        self.microStep_cb.setItemText(0, _translate("FirstPapForm", "Pas entier", None))
        self.microStep_cb.setItemText(1, _translate("FirstPapForm", "1/2 pas", None))
        self.microStep_cb.setItemText(2, _translate("FirstPapForm", "1/4 pas", None))
        self.microStep_cb.setItemText(3, _translate("FirstPapForm", "1/8 pas", None))
        self.microStep_cb.setItemText(4, _translate("FirstPapForm", "1/16 pas", None))
        self.microStep_cb.setItemText(5, _translate("FirstPapForm", "1/32 pas", None))
        self.label_20.setText(_translate("FirstPapForm", "Courant de défaut :", None))
        self.currentFault_cb.setItemText(0, _translate("FirstPapForm", "Arrêt en défaut", None))
        self.currentFault_cb.setItemText(1, _translate("FirstPapForm", "Maintien en défaut", None))
        self.label_19.setText(_translate("FirstPapForm", "Profil de courant :", None))
        self.currentProfile_cb.setItemText(0, _translate("FirstPapForm", "Total", None))
        self.currentProfile_cb.setItemText(1, _translate("FirstPapForm", "Sans boost", None))
        self.currentProfile_cb.setItemText(2, _translate("FirstPapForm", "Sans arrêt", None))
        self.currentProfile_cb.setItemText(3, _translate("FirstPapForm", "Sans boost et sans arrêt", None))
        self.currentProfile_cb.setItemText(4, _translate("FirstPapForm", "Sans maintien", None))
        self.currentProfile_cb.setItemText(5, _translate("FirstPapForm", "Sans maintien et sans boost", None))
        self.currentProfile_cb.setItemText(6, _translate("FirstPapForm", "Sans maintien et sans arrêt", None))
        self.currentProfile_cb.setItemText(7, _translate("FirstPapForm", "Sans maintien, sans boost et sans arrêt", None))
        self.label_18.setText(_translate("FirstPapForm", "Gamme de courant :", None))
        self.currentRange_cb.setItemText(0, _translate("FirstPapForm", "0.2 - 1.9 A", None))
        self.currentRange_cb.setItemText(1, _translate("FirstPapForm", "0.2 - 2.4 A", None))
        self.currentRange_cb.setItemText(2, _translate("FirstPapForm", "0.3 - 3.1 A", None))
        self.currentRange_cb.setItemText(3, _translate("FirstPapForm", "0.5 - 4.9 A", None))
        self.groupBox_5.setTitle(_translate("FirstPapForm", "Nominal", None))
        self.label_23.setText(_translate("FirstPapForm", "Courant :", None))
        self.nominalCurrent.setSuffix(_translate("FirstPapForm", " A", None))
        self.label_24.setText(_translate("FirstPapForm", "Temps :", None))
        self.nominalTime.setSuffix(_translate("FirstPapForm", " ms", None))
        self.groupBox_6.setTitle(_translate("FirstPapForm", "Maintien", None))
        self.label_25.setText(_translate("FirstPapForm", "Courant :", None))
        self.maintainCurrent.setSuffix(_translate("FirstPapForm", " A", None))
        self.label_26.setText(_translate("FirstPapForm", "Temps :", None))
        self.maintainTime.setSuffix(_translate("FirstPapForm", " ms", None))
        self.groupBox_7.setTitle(_translate("FirstPapForm", "Boost", None))
        self.label_27.setText(_translate("FirstPapForm", "Courant :", None))
        self.boostCurrent.setSuffix(_translate("FirstPapForm", " A", None))
        self.boostTime.setSuffix(_translate("FirstPapForm", " ms", None))
        self.label_28.setText(_translate("FirstPapForm", "Temps :", None))
        self.label_29.setText(_translate("FirstPapForm", "Vitesse max :", None))
        self.label_30.setText(_translate("FirstPapForm", "Fast decay :", None))
        self.label_31.setText(_translate("FirstPapForm", "Seuil de déclenchement :", None))
        self.maxSpeed.setSuffix(_translate("FirstPapForm", " pps", None))
        self.fastDecay.setSuffix(_translate("FirstPapForm", " µs", None))
        self.deadband.setSuffix(_translate("FirstPapForm", " mV", None))
        self.label_32.setText(_translate("FirstPapForm", "Temps d\'établissement :", None))
        self.filterTime.setSuffix(_translate("FirstPapForm", " ms", None))
        self.label_11.setText(_translate("FirstPapForm", "Mode de commande :", None))
        self.eepromSave_btn.setText(_translate("FirstPapForm", "Sauvegarde des paramètres\n"
"en EEPROM", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FirstPapForm = QtGui.QWidget()
    ui = Ui_FirstPapForm()
    ui.setupUi(FirstPapForm)
    FirstPapForm.show()
    sys.exit(app.exec_())

