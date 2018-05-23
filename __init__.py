# -*- coding: utf-8 -*-
"""
/***************************************************************************
 presentatie
                                 A QGIS plugin
 presentatie t.b.v. gebruikersdag
                             -------------------
        begin                : 2018-01-26
        copyright            : (C) 2018 by Joost Deen
        email                : jdeen@vrnhn.nl
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load presentatie class from file presentatie.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .presentatie import presentatie
    return presentatie(iface)
