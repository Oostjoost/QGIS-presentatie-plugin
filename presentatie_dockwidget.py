# -*- coding: utf-8 -*-
"""
/***************************************************************************
 presentatieDockWidget
                                 A QGIS plugin
 presentatie t.b.v. gebruikersdag
                             -------------------
        begin                : 2018-01-26
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Joost Deen
        email                : jdeen@vrnhn.nl
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
#pyrcc4 -o C:\Users\localadmin\.qgis2\python\plugins\presentatie\resources.py C:\Users\localadmin\.qgis2\python\plugins\presentatie\resources.qrc
import os

from PyQt4 import QtGui, uic
from PyQt4.QtCore import pyqtSignal
from qgis.core import *
from qgis.gui import *
from qgis.utils import iface

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'presentatie_dockwidget_base.ui'))

class presentatieDockWidget(QtGui.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()
    count = 0
    layerlist = []
    mapCanvas = None
    legend = None

    def __init__(self, parent=None):
        super(presentatieDockWidget, self).__init__(parent)

        self.setupUi(self)
        self.iface  = iface
        self.pushButton.clicked.connect(self.volgende)
        self.layerlist = [['logo_qgis'],['ikzelf'],['vr_text'],['veiligheidsregios'], ['Veiligheidsregio', 'gemeente','vrnhn','kazerne'],
                            ['brandweer_bag'], ['infrastructuur'], ['inrichten_qgis']]
        self.layerExtent = ['logo_qgis', 'ikzelf','vr_text','veiligheidsregios', 'gemeente', 'brandweer_bag', 'infrastructuur', 'inrichten_qgis']
        self.demolayer = ["demo_layer"]
        self.legend = self.iface.legendInterface()  # access the legend

    def volgende(self):
        layer = None
        for lyr in QgsMapLayerRegistry.instance().mapLayers().values():
            if lyr.name() in self.layerlist[self.count]:
                self.legend.setLayerVisible(lyr, True)
                if lyr.name() in self.layerExtent:
                    layer = lyr
            else:
                self.legend.setLayerVisible(lyr, False)
        extent = layer.extent()
        self.mapCanvas.setExtent(extent)
        print(layer.name())
        self.count += 1        
        if self.count == len(self.layerlist):
            self.pushButton.clicked.disconnect()
            self.pushButton.clicked.connect(self.play_movie)

    def play_movie(self):
        if self.count == 8:
            movie = Movie_MP4(r"\movie\My Movie.mp4")
        if self.count == 9:
            movie = Movie_MP4(r"\movie\My Movie 2.mp4")
        self.count += 1
        movie.play()          
        
    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()
        
class Video(object):
    def __init__(self,path):
        self.path = path

    def play(self):
        from os import startfile
        basepath = os.path.dirname(os.path.realpath(__file__))
        startfile(basepath + self.path)

class Movie_MP4(Video):
    type = "MP4"

    
