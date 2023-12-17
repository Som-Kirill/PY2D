import tkinter as tk
#файл об'єктів та мап
#typical not_typical static dynamic

#Мапа статичних денамічних об'єктів для рендерінгу
class Level:
    def __init__(self, typical_map, typical_map_tile_size, original_typical_map, atypical_map, interface_map):
        self.typical_map = typical_map
        self.typical_map_tile_size = typical_map_tile_size
        self.original_typical_map = original_typical_map

        self.atypical_map = atypical_map

        self.interface_map = interface_map

        self.typical_map = [["wall", "wall", "wall", "wall", "wall", "wall", "wall"],
                            ["wall", "grass", "grass", "grass", "grass", "grass", "wall"],
                            ["wall", "grass", "grass", "grass", "grass", "grass", "wall"],
                            ["wall", "grass", "grass", "grass", "grass", "grass", "wall"],
                            ["wall", "grass", "grass", "grass", "grass", "grass", "wall"],
                            ["wall", "grass", "grass", "grass", "grass", "grass|invisible_wall", "wall"],
                            ["wall", "wall", "wall", "wall", "wall", "wall", "wall"]]
        self.original_typical_map = [row[:] for row in self.typical_map]

        self.atypical_map = [player]

#typical об'єкти
class wall:
    def __init__(self, texture_of_the_object = "black", collision_of_the_object = True):
        self.texture_of_the_object = texture_of_the_object
        self.collision_of_the_object = collision_of_the_object

class grass:
    def __init__(self, texture_of_the_object = "green", collision_of_the_object = False):
        self.texture_of_the_object = texture_of_the_object
        self.collision_of_the_object = collision_of_the_object

class invisible_wall:
    def __init__(self, texture_of_the_object = f"#00FF00{128:02X}", collision_of_the_object = True):
        self.texture_of_the_object = texture_of_the_object
        self.collision_of_the_object = collision_of_the_object

#not_typical об'єкти
    
class player:
    def __init__(self, physical_size_of_object = 24, texture_of_the_object = "red", collision_of_the_object = True, position_of_the_object_X = 68, position_of_the_object_Y = 68, step_size = 4):
        self.physical_size_of_object = physical_size_of_object

        self.texture_of_the_object = texture_of_the_object
        self.collision_of_the_object = collision_of_the_object

        self.position_of_the_object_X = position_of_the_object_X
        self.position_of_the_object_Y = position_of_the_object_Y

        self.step_size = step_size #pixel/click

#Інтерфейсні об'єкти    