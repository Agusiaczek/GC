# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:26:57 2023

@author: student
"""

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Area: {self.area} sq. meters\nRooms: {self.rooms}\nPrice: {self.price}\nAddress: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"{super().__str__()}\nPlot size: {self.plot} sq. meters"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"{super().__str__()}\nFloor: {self.floor}"


house = House(200, 6, 356849, "231 Demobowskiego", 200)
flat = Flat(60, 2, 22484, "987 Bakery Street", 1)

print("House:")
print(house)
print("\nFlat:")
print(flat)