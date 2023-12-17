import tkinter as tk
import time

TILE_SIZE = 32
RED_SQUARE_SIZE = 24
FILL_GREEN = "green"
FILL_BLACK = "black"
FILL_GRAY = "light grey"
FILL_RED = "red"
FILL_PLAYER = "orange"

MOVE_UP = 'w'
MOVE_DOWN = 's'
MOVE_LEFT = 'a'
MOVE_RIGHT = 'd'

px, py = 68, 68

window = tk.Tk()
window.title("TEST")
window.geometry("800x500")

canvas = tk.Canvas(window, width=400, height=250)
canvas.pack()

fps_label = tk.Label(window, text="FPS: 0", anchor='e')
fps_label.pack()

game_map = [[1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]]

original_map = [row[:] for row in game_map]

fps_start_time = time.time()
fps_frame_count = 0

ZOOM_FACTOR = 1.1  # Adjust the zoom factor according to your preference
s1, s2 = 10, 200  # Set the minimum and maximum sizes for zooming

def draw_map():
    global game_map
    canvas.delete("all")
    x, y = 0, 0

    red_square_cells = set()
    for i in range(px // TILE_SIZE, (px + RED_SQUARE_SIZE - 1) // TILE_SIZE + 1):
        for j in range(py // TILE_SIZE, (py + RED_SQUARE_SIZE - 1) // TILE_SIZE + 1):
            red_square_cells.add((i, j))

    for i, row in enumerate(game_map):
        for j, tile in enumerate(row):
            fill_color = FILL_GREEN if tile == 0 else FILL_BLACK if tile == 1 else FILL_PLAYER

            if (j, i) in red_square_cells:
                fill_color = FILL_GRAY
                game_map[i][j] = "p"

            canvas.create_rectangle(x, y, x + TILE_SIZE, y + TILE_SIZE, fill=fill_color)
            x += TILE_SIZE
        x = 0
        y += TILE_SIZE
    canvas.create_rectangle(px, py, px + RED_SQUARE_SIZE, py + RED_SQUARE_SIZE, fill=FILL_RED)


def revert_to_original():
    global game_map
    for i in range(len(game_map)):
        for j in range(len(game_map[0])):
            game_map[i][j] = original_map[i][j]


def update():
    global fps_start_time, fps_frame_count
    global px, py
    global fps_frame_count
    draw_map()
    fps_frame_count += 1

    current_time = time.time()
    elapsed_time = current_time - fps_start_time
    if elapsed_time >= 1.0:
        fps = fps_frame_count
        fps_label.config(text=f"FPS: {fps}")
        fps_start_time = current_time
        fps_frame_count = 0

    window.after(10, update)


def handle_key(event):
    global px, py
    step_size = 4

    if event.char == MOVE_UP:
        py -= step_size
    elif event.char == MOVE_DOWN:
        py += step_size
    elif event.char == MOVE_LEFT:
        px -= step_size
    elif event.char == MOVE_RIGHT:
        px += step_size

    px = max(0, min(px, canvas.winfo_width() - RED_SQUARE_SIZE))
    py = max(0, min(py, canvas.winfo_height() - RED_SQUARE_SIZE))

    revert_to_original()


def handle_mouse_wheel(event):
    global RED_SQUARE_SIZE, TILE_SIZE
    if event.delta > 0:  # Zoom in
        RED_SQUARE_SIZE = min(s2, int(RED_SQUARE_SIZE * ZOOM_FACTOR))
        TILE_SIZE = min(s2, int(TILE_SIZE * ZOOM_FACTOR))
    elif event.delta < 0:  # Zoom out
        RED_SQUARE_SIZE = max(s1, int(RED_SQUARE_SIZE / ZOOM_FACTOR))
        TILE_SIZE = max(s1, int(TILE_SIZE / ZOOM_FACTOR))

    revert_to_original()


window.bind("<Key>", handle_key)
window.bind("<MouseWheel>", handle_mouse_wheel)

update()
window.mainloop()
