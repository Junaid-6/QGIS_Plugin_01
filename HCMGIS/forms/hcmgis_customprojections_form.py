# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hcmgis_customprojections_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_hcmgis_customprojections_form(object):
    def setupUi(self, hcmgis_customprojections_form):
        hcmgis_customprojections_form.setObjectName("hcmgis_customprojections_form")
        hcmgis_customprojections_form.setWindowModality(QtCore.Qt.ApplicationModal)
        hcmgis_customprojections_form.setEnabled(True)
        hcmgis_customprojections_form.resize(688, 308)
        hcmgis_customprojections_form.setMouseTracking(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(hcmgis_customprojections_form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.LblEPSGInfo = QtWidgets.QLabel(hcmgis_customprojections_form)
        self.LblEPSGInfo.setObjectName("LblEPSGInfo")
        self.gridLayout.addWidget(self.LblEPSGInfo, 9, 0, 1, 4)
        self.label = QtWidgets.QLabel(hcmgis_customprojections_form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.radProvinces = QtWidgets.QRadioButton(hcmgis_customprojections_form)
        self.radProvinces.setChecked(True)
        self.radProvinces.setObjectName("radProvinces")
        self.gridLayout.addWidget(self.radProvinces, 1, 0, 1, 1)
        self.cboProvinces = QtWidgets.QComboBox(hcmgis_customprojections_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboProvinces.sizePolicy().hasHeightForWidth())
        self.cboProvinces.setSizePolicy(sizePolicy)
        self.cboProvinces.setObjectName("cboProvinces")
        self.gridLayout.addWidget(self.cboProvinces, 1, 1, 1, 1)
        self.TxtEPSGInfo = QtWidgets.QTextEdit(hcmgis_customprojections_form)
        self.TxtEPSGInfo.setReadOnly(True)
        self.TxtEPSGInfo.setObjectName("TxtEPSGInfo")
        self.gridLayout.addWidget(self.TxtEPSGInfo, 10, 0, 1, 4)
        self.radEPSG = QtWidgets.QRadioButton(hcmgis_customprojections_form)
        self.radEPSG.setObjectName("radEPSG")
        self.gridLayout.addWidget(self.radEPSG, 1, 2, 1, 1)
        self.cboEPSG = QtWidgets.QComboBox(hcmgis_customprojections_form)
        self.cboEPSG.setObjectName("cboEPSG")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.gridLayout.addWidget(self.cboEPSG, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.BtnClose = QtWidgets.QDialogButtonBox(hcmgis_customprojections_form)
        self.BtnClose.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.BtnClose.setObjectName("BtnClose")
        self.verticalLayout.addWidget(self.BtnClose)

        self.retranslateUi(hcmgis_customprojections_form)
        self.BtnClose.accepted.connect(hcmgis_customprojections_form.accept)
        self.BtnClose.rejected.connect(hcmgis_customprojections_form.reject)
        QtCore.QMetaObject.connectSlotsByName(hcmgis_customprojections_form)

    def retranslateUi(self, hcmgis_customprojections_form):
        _translate = QtCore.QCoreApplication.translate
        hcmgis_customprojections_form.setWindowTitle(_translate("hcmgis_customprojections_form", "VN-2000 Projections"))
        self.LblEPSGInfo.setText(_translate("hcmgis_customprojections_form", "EPSG Info:"))
        self.label.setText(_translate("hcmgis_customprojections_form", "VN-200/ TM-3"))
        self.radProvinces.setText(_translate("hcmgis_customprojections_form", "Search by Province"))
        self.radEPSG.setText(_translate("hcmgis_customprojections_form", "Search by EPSG Code"))
        self.cboEPSG.setItemText(0, _translate("hcmgis_customprojections_form", "9205"))
        self.cboEPSG.setItemText(1, _translate("hcmgis_customprojections_form", "9206"))
        self.cboEPSG.setItemText(2, _translate("hcmgis_customprojections_form", "9207"))
        self.cboEPSG.setItemText(3, _translate("hcmgis_customprojections_form", "9208"))
        self.cboEPSG.setItemText(4, _translate("hcmgis_customprojections_form", "5897"))
        self.cboEPSG.setItemText(5, _translate("hcmgis_customprojections_form", "9209"))
        self.cboEPSG.setItemText(6, _translate("hcmgis_customprojections_form", "9210"))
        self.cboEPSG.setItemText(7, _translate("hcmgis_customprojections_form", "9211"))
        self.cboEPSG.setItemText(8, _translate("hcmgis_customprojections_form", "9212"))
        self.cboEPSG.setItemText(9, _translate("hcmgis_customprojections_form", "9213"))
        self.cboEPSG.setItemText(10, _translate("hcmgis_customprojections_form", "9214"))
        self.cboEPSG.setItemText(11, _translate("hcmgis_customprojections_form", "9215"))
        self.cboEPSG.setItemText(12, _translate("hcmgis_customprojections_form", "9216"))
        self.cboEPSG.setItemText(13, _translate("hcmgis_customprojections_form", "5899"))
        self.cboEPSG.setItemText(14, _translate("hcmgis_customprojections_form", "5898"))
        self.cboEPSG.setItemText(15, _translate("hcmgis_customprojections_form", "9217"))
        self.cboEPSG.setItemText(16, _translate("hcmgis_customprojections_form", "9218"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hcmgis_customprojections_form = QtWidgets.QDialog()
    ui = Ui_hcmgis_customprojections_form()
    ui.setupUi(hcmgis_customprojections_form)
    hcmgis_customprojections_form.show()
    sys.exit(app.exec_())