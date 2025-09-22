#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   GIMP - The GNU Image Manipulation Program
#   Copyright (C) 1995 Spencer Kimball and Peter Mattis
#
#   gimp-tutorial-plug-in.py
#   sample plug-in to illustrate the Python plug-in writing tutorial
#   Copyright (C) 2023 Jacob Boerema
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys

import gi
gi.require_version('Gimp', '3.0')
from gi.repository import Gimp
gi.require_version('GimpUi', '3.0')
from gi.repository import GimpUi

from gi.repository import GLib

class GK2A_uhrit_join_05km (Gimp.PlugIn):
    def do_query_procedures(self):
        return [ "jb-plug-in-first-try05" ]

    def do_set_i18n (self, name):
        return False

    def do_create_procedure(self, name):
        procedure = Gimp.ImageProcedure.new(self, name,
                                            Gimp.PDBProcType.PLUGIN,
                                            self.run, None)

        procedure.set_image_types("*")

        procedure.set_menu_label("GK-2A UHRIT join images (0.5km)")
        procedure.add_menu_path('<Image>/GK-2A/')

        procedure.set_documentation("A plugin for GeoKompSat-2A satellite",
                                    "Join segments at 0.5km resolution",
                                    name)
        procedure.set_attribution("John", "Bell", "2025")

        return procedure

    def run(self, procedure, run_mode, image, drawables, config, run_data):
        
        all_layers = image.get_layers()
        all_layers[0].set_offsets(0, 0)
        all_layers[1].set_offsets(0, 500)
        all_layers[2].set_offsets(0,1500)
        all_layers[3].set_offsets(0,2500)
        all_layers[4].set_offsets(0,3500)
        all_layers[5].set_offsets(0,4500)
        all_layers[6].set_offsets(0,5500)
        all_layers[7].set_offsets(0,6500)
        all_layers[8].set_offsets(0,7500)
        all_layers[9].set_offsets(0,8500)
        all_layers[10].set_offsets(0,9500)
        all_layers[11].set_offsets(0,10500)
        all_layers[12].set_offsets(0,11500)
        all_layers[13].set_offsets(0,12500)
        all_layers[14].set_offsets(0,13500)
        all_layers[15].set_offsets(0,14500)
        all_layers[16].set_offsets(0,15500)
        all_layers[17].set_offsets(0,16500)
        all_layers[18].set_offsets(0,17500)
        all_layers[19].set_offsets(0,18500)
        all_layers[20].set_offsets(0,19500)
        all_layers[21].set_offsets(0,20500)
        all_layers[22].set_offsets(0,21500)
        
        return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())

Gimp.main(GK2A_uhrit_join_05km.__gtype__, sys.argv)