# vim:set et ts=4:
#
# ibus-tmpl - The Input Bus template project
#
# Copyright (c) 2007-2008 Huang Peng <shawn.p.huang@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from ibus import interface
import engine

FACTORY_PATH = "/com/redhat/IBus/engines/Demo/Factory"
ENGINE_PATH = "/com/redhat/IBus/engines/Demo/Engine/%d"

class EngineFactory(interface.IEngineFactory):
    NAME = "Enchant"
    LANG = "en"
    ICON = "ibus-enchant"
    AUTHORS = "Huang Peng <shawn.p.huang@gmail.com>"
    CREDITS = "GPLv2"

    def __init__(self, dbusconn):
		super(EngineFactory, self).__init__(dbusconn, object_path = FACTORY_PATH)
        self._dbusconn = dbusconn
        self._max_engine_id = 1

    def GetInfo(self):
        return [
            self.NAME,
            self.LANG,
            self.ICON,
            self.AUTHORS,
            self.CREDITS
            ]

    def CreateEngine(self):
        engine_path = ENGINE_PATH % self._max_engine_id
        self._max_engine_id += 1
        return engine.DemoEngine(self._dbusconn, engine_path)

    def Destroy(self):
        self.remove_from_connection()
        self._dbusconn = None

