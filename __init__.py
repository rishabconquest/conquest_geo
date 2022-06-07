# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ConquestGeo
                                 A QGIS plugin
 This plugin connects to your Conquest assets
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-12-10
        copyright            : (C) 2021 by Conquest Software Pty Ltd.
        email                : support@conquestsoftware.com.au
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.insert(0, dir_path)

from ui.conquest_geo import ConquestGeo

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ConquestGeo class from file ConquestGeo.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    return ConquestGeo(iface)
