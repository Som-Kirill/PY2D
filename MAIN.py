import tkinter as tk
import threading
import random
import time

class main:
    def __init__(self, typical_objects, atypical_objects, interface):
        self.typical_objects = typical_objects
        self.atypical_objects = atypical_objects
        self.interface = interface
        self.pool_action = []
    def сreating_window(self, title = "TEST", geometry_width = 800, geometry_height = 600, resizable = False):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{geometry_width}x{geometry_height}")
        self.root.resizable(width=resizable, height=resizable)
        self.canvas = tk.Canvas(self.root, width=geometry_width, height=geometry_height, bg="black", bd=0, relief=tk.FLAT)
        self.canvas.pack()
        self.root.bind('<KeyPress>', self.atypical_objects.on_key_press)
        self.root.bind('<KeyRelease>', self.atypical_objects.on_key_release)

    def loading_maps_of_objects(self):
        self.typical_objects = typical_objects()
        self.typical_objects.load()
        self.atypical_objects = atypical_objects()
        self.atypical_objects.load()
        self.interface = interface()
        self.interface.load()
    def map_drawing(self):
        tile_position_x = -(self.typical_objects.tile_size)
        tile_position_y = -(self.typical_objects.tile_size)
        for line in self.typical_objects.map_typical_objects:
            tile_position_y += self.typical_objects.tile_size
            for item in line:
                tile_position_x += self.typical_objects.tile_size
                self.canvas.create_rectangle(tile_position_x, tile_position_y, tile_position_x + self.typical_objects.tile_size, tile_position_y + self.typical_objects.tile_size, fill=item.texture)
            tile_position_x = -(self.typical_objects.tile_size)
        for item in self.atypical_objects.map_atypical_objects:
            self.canvas.create_rectangle(item.position_x, item.position_y, item.position_x + item.box_size, item.position_y + item.box_size, fill=item.texture)
                
    def collision(self):
        pass
    def update(self):
        start_time = time.time()
        for item in self.pool_action:
            item()
        self.collision()
        self.map_drawing()
        elapsed_time = time.time() - start_time
        if elapsed_time != 0:
            updates_per_second = int(1 / elapsed_time)
            #print(f"FPS: {updates_per_second:.2f}")
        self.canvas.after(200, self.update)
class typical_objects:
    def __init__(self, map_typical_objects = [], tile_size = 32):
        self.map_typical_objects = map_typical_objects
        self.tile_size = tile_size
    def load(self):
        self.map_typical_objects = [[wall(), wall(), wall(), wall(), wall(), wall(), wall()],
                                    [wall(), grass(), grass(), grass(), grass(), grass(), wall()],
                                    [wall(), grass(), grass(), grass(), grass(), grass(), wall()],
                                    [wall(), grass(), grass(), grass(), grass(), grass(), wall()],
                                    [wall(), grass(), grass(), grass(), grass(), grass(), wall()],
                                    [wall(), grass(), grass(), grass(), grass(), grass(), wall()],
                                    [wall(), wall(), wall(), wall(), wall(), wall(), wall()]]

class wall:
    def __init__(self, texture = "grey", collision = True):
        self.texture = texture
        self.collision = collision

class grass:
    def __init__(self, texture = "green", collision = False):
        self.texture = texture
        self.collision = collision

class atypical_objects:
    def __init__(self, map_atypical_objects = []):
        self.map_atypical_objects = map_atypical_objects
    def load(self):
        self.map_atypical_objects = [player(68, 68), stone(80,43), stone(140,140)]
    def on_key_press(self, event):
        #print(f"Початок натискання клавіші: {event.char}")
        if event == "w":
            player.player_move_w
        if event == "s":    
            player.player_move_s
        if event == "a":
            player.player_move_a
        if event == "d":
            player.player_move_d
    def on_key_release(self, event):
        #print(f"Кінець натискання клавіші: {event.char}")
        pass

class player:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.box_size = 24
        self.texture = "red"
        self.collision = True
        self.last_move = None
        self.attached_object = False
        self.speed_movement = 0
    def player_move_w(self):
        self.speed_movement += 0.5
        main.pool_action.append(player.player_move_w)
    def player_move_s(self):
        self.speed_movement += 0.5
        main.pool_action.append(player.player_move_s)
    def player_move_a(self):
        self.speed_movement += 0.5
        main.pool_action.append(player.player_move_a)
    def player_move_d(self):
        self.speed_movement += 0.5
        main.pool_action.append(player.player_move_d)
    def player_action_move_w(self):
        print(main.pool_action)
    def player_action_move_s(self):
        pass
    def player_action_move_a(self):
        pass
    def player_action_move_d(self):
        pass
class stone:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.box_size = 14
        self.texture = "blue"
        self.collision = True
        self.last_move = None
        self.attached_object = True
        self.speed_movement = 0

class interface:
    def __init__(self, map_interface = []):
        self.map_interface = map_interface
    def load(self):
        pass

typical_objs = typical_objects()
atypical_objs = atypical_objects()
Interface = interface()

engine = main(typical_objs, atypical_objs, Interface)
engine.сreating_window()
engine.loading_maps_of_objects()
engine.update()
tk.mainloop()