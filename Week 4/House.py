# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class House:
    count = 0
    def __init__(self, typ, rooms):
        self._typ = typ
        self._rooms = rooms
        self.__class__.count += 1
    def getType(self):
        return self._typ
    def getRooms(self):
        return self._rooms
    def setRooms(self, rooms):
        self._rooms = rooms
    def getCount (self):
        return self.__class__.count
    def __str__(self):
        return "Type of House: " + self._typ + \
            "\nNumber of Rooms: " + str(self._rooms)