# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hcmgis_csv2shp_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_hcmgis_csv2shp_form(object):
    def setupUi(self, hcmgis_csv2shp_form):
        hcmgis_csv2shp_form.setObjectName("hcmgis_csv2shp_form")
        hcmgis_csv2shp_form.setWindowModality(QtCore.Qt.ApplicationModal)
        hcmgis_csv2shp_form.setEnabled(True)
        hcmgis_csv2shp_form.resize(513, 463)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        hcmgis_csv2shp_form.setFont(font)
        hcmgis_csv2shp_form.setMouseTracking(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(hcmgis_csv2shp_form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(hcmgis_csv2shp_form)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.BtnInputFolder = QtWidgets.QPushButton(hcmgis_csv2shp_form)
        self.BtnInputFolder.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.BtnInputFolder.setFont(font)
        self.BtnInputFolder.setObjectName("BtnInputFolder")
        self.gridLayout_3.addWidget(self.BtnInputFolder, 0, 1, 1, 1)
        self.LinInputFolder = QtWidgets.QLineEdit(hcmgis_csv2shp_form)
        self.LinInputFolder.setEnabled(True)
        self.LinInputFolder.setMouseTracking(True)
        self.LinInputFolder.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.LinInputFolder.setAcceptDrops(False)
        self.LinInputFolder.setText("")
        self.LinInputFolder.setReadOnly(True)
        self.LinInputFolder.setObjectName("LinInputFolder")
        self.gridLayout_3.addWidget(self.LinInputFolder, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.lblCSV = QtWidgets.QLabel(hcmgis_csv2shp_form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblCSV.setFont(font)
        self.lblCSV.setText("")
        self.lblCSV.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lblCSV.setObjectName("lblCSV")
        self.verticalLayout.addWidget(self.lblCSV)
        self.lsCSV = QtWidgets.QListWidget(hcmgis_csv2shp_form)
        self.lsCSV.setObjectName("lsCSV")
        self.verticalLayout.addWidget(self.lsCSV)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.longitude_field = QtWidgets.QComboBox(hcmgis_csv2shp_form)
        self.longitude_field.setObjectName("longitude_field")
        self.gridLayout_2.addWidget(self.longitude_field, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(hcmgis_csv2shp_form)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)
        self.latitude_field = QtWidgets.QComboBox(hcmgis_csv2shp_form)
        self.latitude_field.setObjectName("latitude_field")
        self.gridLayout_2.addWidget(self.latitude_field, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(hcmgis_csv2shp_form)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.LblStatus = QtWidgets.QLabel(hcmgis_csv2shp_form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LblStatus.setFont(font)
        self.LblStatus.setText("")
        self.LblStatus.setObjectName("LblStatus")
        self.verticalLayout.addWidget(self.LblStatus)
        self.status = QtWidgets.QProgressBar(hcmgis_csv2shp_form)
        self.status.setProperty("value", 24)
        self.status.setObjectName("status")
        self.verticalLayout.addWidget(self.status)
        self.label = QtWidgets.QLabel(hcmgis_csv2shp_form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.txtError = QtWidgets.QTextEdit(hcmgis_csv2shp_form)
        self.txtError.setObjectName("txtError")
        self.verticalLayout.addWidget(self.txtError)
        self.BtnApplyClose = QtWidgets.QDialogButtonBox(hcmgis_csv2shp_form)
        self.BtnApplyClose.setOrientation(QtCore.Qt.Horizontal)
        self.BtnApplyClose.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Close)
        self.BtnApplyClose.setCenterButtons(False)
        self.BtnApplyClose.setObjectName("BtnApplyClose")
        self.verticalLayout.addWidget(self.BtnApplyClose)

        self.retranslateUi(hcmgis_csv2shp_form)
        self.BtnApplyClose.accepted.connect(hcmgis_csv2shp_form.accept)
        self.BtnApplyClose.rejected.connect(hcmgis_csv2shp_form.reject)
        QtCore.QMetaObject.connectSlotsByName(hcmgis_csv2shp_form)

    def retranslateUi(self, hcmgis_csv2shp_form):
        _translate = QtCore.QCoreApplication.translate
        hcmgis_csv2shp_form.setWindowTitle(_translate("hcmgis_csv2shp_form", "Batch Convert CSV to Point"))
        self.label_2.setText(_translate("hcmgis_csv2shp_form", "Input CSV Point Folder"))
        self.BtnInputFolder.setText(_translate("hcmgis_csv2shp_form", "Browse..."))
        self.label_7.setText(_translate("hcmgis_csv2shp_form", "Longitude Field"))
        self.label_8.setText(_translate("hcmgis_csv2shp_form", "Latitude Field"))
        self.label.setText(_translate("hcmgis_csv2shp_form", "Errors Log"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hcmgis_csv2shp_form = QtWidgets.QDialog()
    ui = Ui_hcmgis_csv2shp_form()
    ui.setupUi(hcmgis_csv2shp_form)
    hcmgis_csv2shp_form.show()
    sys.exit(app.exec_())