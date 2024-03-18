# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MapTiler
                                 A QGIS plugin
 Show MapTiler cloud maps.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2020-04-02
        git sha              : $Format:%H$
        copyright            : (C) 2020 by MapTiler AG
        email                : sales@maptiler.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os.path
import re

from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, QMetaObject
from qgis.core import *

from .browser_root_collection import DataItemProvider
from .geocoder import MapTilerGeocoderToolbar


class MapTiler:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        self.proj = QgsProject.instance()

        # Save reference to the QGIS interface
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'MapTiler_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&MapTiler')

        # init Geocoding Toolbar
        self.gc_toolbar = MapTilerGeocoderToolbar(self.iface)

        self.pluginIsActive = False

        #copyright variables
        self._previous_copyrights = []
        self._default_copyright = QgsProject.instance().readEntry("CopyrightLabel", "/Label")[0]
        self._default_copyright_is_visible = QgsProject.instance().readEntry("CopyrightLabel", "/Enabled")[0] == "true"
        self.proj.readProjectWithContext.connect(lambda a0, context:self._on_custom_project_loaded(a0, context))
        self.proj.cleared.connect(self._on_project_closed)

    # noinspection PyMethodMayBeStatic

    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('MapTiler', message)

    def initGui(self):
        # add MapTiler Collection to Browser
        self.dip = DataItemProvider()
        QgsApplication.instance().dataItemProviderRegistry().addProvider(self.dip)

        self._activate_copyrights()

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""

        # remove MapTiler Collection to Browser
        QgsApplication.instance().dataItemProviderRegistry().removeProvider(self.dip)
        self.dip = None

        # remove the toolbar
        del self.gc_toolbar

        self._deactivate_copyrights()

    def _on_custom_project_loaded(self, a0, context):
        copyright_label_in_the_project = ""
        copyright_enabled_in_the_project = False
        copyright_nodes = a0.elementsByTagName("CopyrightLabel").at(0).childNodes()
        for i in range(copyright_nodes.count()):
            if copyright_nodes.at(i).nodeName() == "Label":
                copyright_label_in_the_project = copyright_nodes.at(i).toElement().text()
            if copyright_nodes.at(i).nodeName() == "Enabled":
                if copyright_nodes.at(i).toElement().text() == "true":
                    copyright_enabled_in_the_project = True
            
        self._default_copyright = copyright_label_in_the_project
        self._default_copyright_is_visible = copyright_enabled_in_the_project
        QgsProject.instance().writeEntry("CopyrightLabel", "/Label", self._default_copyright)
        QgsProject.instance().writeEntry("CopyrightLabel", "/Enabled", self._default_copyright_is_visible)

    def _on_project_closed(self):
        self._default_copyright = ""
        self._default_copyright_is_visible = False
        QgsProject.instance().writeEntry("CopyrightLabel", "/Label", self._default_copyright)
        QgsProject.instance().writeEntry("CopyrightLabel", "/Enabled", self._default_copyright_is_visible)

    def _activate_copyrights(self):
        # self.iface.layerTreeView().clicked.connect(self._write_copyright_entries)
        # self.iface.layerTreeView().currentLayerChanged.connect(self._write_copyright_entries)
        self.proj.layersAdded.connect(self._write_copyright_entries)
        self.proj.layersWillBeRemoved.connect(self._write_copyright_entries)

    def _deactivate_copyrights(self):
        # self.iface.layerTreeView().clicked.disconnect(self._write_copyright_entries)
        # self.iface.layerTreeView().currentLayerChanged.disconnect(self._write_copyright_entries)
        self.proj.layersAdded.disconnect(self._write_copyright_entries)
        self.proj.layersWillBeRemoved.disconnect(self._write_copyright_entries)
        QgsProject.instance().writeEntry("CopyrightLabel", "/Label", self._default_copyright)
        QgsProject.instance().writeEntry("CopyrightLabel", "/Enabled", self._default_copyright_is_visible)
        QMetaObject.invokeMethod(self.iface.mainWindow(), "projectReadDecorationItems")
        self.iface.mapCanvas().refresh()

    def _was_added_via_plugin(self, lyr):
        """
        Estimates whether layer was added via MapTiler plugin:
        1. Layer is an instance of QgsVectorTileLayer
        2. Layer's source contains 'api.maptiler'
        """

        if isinstance(lyr, list):
            lyr = lyr[0]
        # Adding layers
        if isinstance(lyr, QgsVectorTileLayer) or (isinstance(lyr, QgsMapLayer) and "api.maptiler" in lyr.source()):
            return True
        # Removing layers
        elif isinstance(lyr, str):
            layers = self.proj.mapLayers()
            if lyr in layers.keys():
                return self._was_added_via_plugin(layers.get(lyr))
        return False

    def _write_copyright_entries(self, param):
        if not self._was_added_via_plugin(param):
            return
        adding_layers = []
        if isinstance(param, QgsMapLayer):
            adding_layers.append(param)
        elif isinstance(param, list):
            if isinstance(param[0], QgsMapLayer):
                adding_layers += param

        parsed_copyrights = self._parse_copyrights(adding_layers=adding_layers)
        copyrights_to_text = []
        for c in parsed_copyrights:
            if c in self._default_copyright:
                continue
            copyrights_to_text.append(c)
        
        copyrights_text = ' '.join(copyrights_to_text)

        #trim copyright to raw
        copyrights_to_trim = parsed_copyrights + self._previous_copyrights
        trimed_copyrights_text = self._trim_copyrights_to_default(copyrights_to_trim)
        if not trimed_copyrights_text == "":
            self._default_copyright = trimed_copyrights_text
            self._default_copyright_is_visible = True

        #if user defined copyright exists and visible
        if self._default_copyright and self._default_copyright_is_visible:
            copyrights_text += " " + self._default_copyright
        
        # when no active MapTiler layer
        if parsed_copyrights == []:
            QgsProject.instance().writeEntry("CopyrightLabel", "/Label", self._default_copyright)
            QgsProject.instance().writeEntry("CopyrightLabel", "/Enabled", self._default_copyright_is_visible)
        else:
            QgsProject.instance().writeEntry("CopyrightLabel", "/Label", copyrights_text)
            QgsProject.instance().writeEntry("CopyrightLabel", "/Enabled", True)

        QgsProject.instance().writeEntry("CopyrightLabel", "/MarginH", 1)
        QgsProject.instance().writeEntry("CopyrightLabel", "/MarginV", 1)
        QMetaObject.invokeMethod(self.iface.mainWindow(), "projectReadDecorationItems")
        self.iface.mapCanvas().refresh()

        self._previous_copyrights = copyrights_to_text

    def _trim_copyrights_to_default(self, copyrights_to_text = []):
        current_copyrights_text = QgsProject.instance().readEntry("CopyrightLabel", "/Label")[0]
        for c in copyrights_to_text:
            current_copyrights_text = current_copyrights_text.replace(c, "")
        current_copyrights_text = current_copyrights_text.strip()
        return current_copyrights_text

    def _parse_copyrights(self, adding_layers=[]):
        copyrights = []
        target_layers = []
        target_layers += adding_layers
        root_group = self.iface.layerTreeView().layerTreeModel().rootGroup()
        for l in root_group.findLayers():
            # when invalid layer is in Browser
            if not isinstance(l.layer(), QgsMapLayer):
                continue
            target_layers.append(l.layer())

        for l in target_layers:
            attribution = l.attribution()
            attribution = re.sub(
                '<a.*?>|</a>', '', attribution).replace('&copy;', '©').replace('©', '!!!©')
            parsed_attributions = attribution.split('!!!')
            parsed_attributions = list(map(str.strip, parsed_attributions))
            for attr in parsed_attributions:
                if attr == '':
                    continue
                if not attr in copyrights:
                    copyrights.append(attr)
        
        return copyrights

    # --------------------------------------------------------------------------