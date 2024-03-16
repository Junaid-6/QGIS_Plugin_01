import os
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'latlangcalc_dialog_base.ui'))

class LatLangCacDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(LatLangCacDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        # Event Connecter to Latitude 
        self.sb_Lat_D.valueChanged.connect(self.latDMStoDD)
        self.sb_Lat_M.valueChanged.connect(self.latDMStoDD)
        self.sb_Lat_S.valueChanged.connect(self.latDMStoDD)        

        # Event Connecter to Longitude
        self.sb_Lng_D.valueChanged.connect(self.lngDMStoDD)
        self.sb_Lng_M.valueChanged.connect(self.lngDMStoDD)
        self.sb_Lng_S.valueChanged.connect(self.lngDMStoDD)

        
        # Event Connecter to Hemisphere 
        self.cb_Lat_Hshpere.currentTextChanged.connect(self.latDMStoDD)
        self.cb_Lng_Hshpere.currentTextChanged.connect(self.lngDMStoDD)

        # DD Connector
        self.sbLatDD.valueChanged.connect(self.latDDtoDMS)
        self.sbLngDD.valueChanged.connect(self.lngDDtoDMS)
        

    def latDMStoDD(self):
        d = self.sb_Lat_D.value()
        m = self.sb_Lat_M.value()
        s = self.sb_Lat_S.value()
        dms = DMS(d, m, s) 
        hemisphere = self.cb_Lat_Hshpere.currentText() 
        if hemisphere == "S":
            dms.dd = dms.dd*-1
        self.sbLatDD.setValue(dms.dd)

    def lngDMStoDD(self):
        d = self.sb_Lng_D.value()
        m = self.sb_Lng_M.value()
        s = self.sb_Lng_S.value() 
        dms = DMS(d, m, s)
        hemisphere = self.cb_Lng_Hshpere.currentText()
        if hemisphere == "S":
            dms.dd =  dms.dd*-1
        self.sbLngDD.setValue(dms.dd)

    def latDDtoDMS(self):
        dd = self.sbLatDD.value()
        hemisphere = self.cb_Lat_Hshpere.currentText()
        
        if dd < 0:
            hemisphere = "S"  # Force hemisphere to be South if DD is negative
            dd = abs(dd)
        
        d = int(dd)
        m = int((dd - d) * 60)
        s = int((dd - d - m / 60) * 3600 )
        
        self.sb_Lat_D.setValue(d)
        self.sb_Lat_M.setValue(m)
        self.sb_Lat_S.setValue(s)
        self.cb_Lat_Hshpere.setCurrentText(hemisphere)


    def lngDDtoDMS(self):
        dd = self.sbLngDD.value()
        hemisphere = self.cb_Lng_Hshpere.currentText()
        
        if dd < 0:
            hemisphere = "W"  # Force hemisphere to be West if DD is negative
            dd = abs(dd)
        
        d = int(dd)
        m = int((dd - d) * 60)
        s = int((dd - d - m / 60) * 3600)
        
        self.sb_Lng_D.setValue(d)
        self.sb_Lng_M.setValue(m)
        self.sb_Lng_S.setValue(s)
        self.cb_Lng_Hshpere.setCurrentText(hemisphere)

            
        

class DMS:
    def __init__(self, d, m, s):
        self.d = d
        self.m = m 
        self.s = s
        self.dd = self.DMS_to_DD()

    def DMS_to_DD(self):
        return float(self.d) + (float(self.m)/60) + (float(self.s)/3600)
    
    


class Point:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng