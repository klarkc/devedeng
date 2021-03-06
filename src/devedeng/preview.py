# Copyright 2014 (C) Raster Software Vigo (Sergio Costas)
#
# This file is part of DeVeDe-NG
#
# DeVeDe-NG is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# DeVeDe-NG is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from gi.repository import Gtk
import os
import devedeng.configuration_data

class preview_window:

    def __init__(self):

        self.config = devedeng.configuration_data.configuration.get_config()

    def run(self):

        builder = Gtk.Builder()
        builder.set_translation_domain(self.config.gettext_domain)

        builder.add_from_file(os.path.join(self.config.glade,"wpreview.ui"))
        builder.connect_signals(self)
        wpreview_window = builder.get_object("dialog_preview")
        wlength = builder.get_object("length")

        wpreview_window.show_all()
        wlength.set_value(60.0)
        retval = wpreview_window.run()
        self.lvalue = int(wlength.get_value())
        wpreview_window.destroy()
        if (retval == 1):
            return True
        else:
            return False