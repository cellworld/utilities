from tkinter import *
from cellworld import *
from time import sleep
import os

if 'CELLWORLD_CACHE' in os.environ:
    cell_group_folder = os.environ['CELLWORLD_CACHE'] + "/cell_group"
else:
    print ("CELLWORLD_CACHE environment variable not set")
    exit(0)

world_name = ""
w = World.get_from_parameters_names("hexagonal",  "canonical")
d = Display(w, animated=True)


def occlusion_toggle(b, c):
    print (b, c)
    c.occluded = not c.occluded
    d.__draw_cells__()


def key_pressed(k):
    global world_name
    if k.key == "s":
        world_name = input("World name:")

        if world_name:
            file_name = cell_group_folder + "/hexagonal." + world_name + ".occlusions"
            print("saving file ", file_name)
            w.cells.occluded_cells().save(file_name)
    elif k.key == "q":
        exit(0)
    elif k.key == "p":
        if world_name:
            import subprocess
            subprocess.run(["../scripts/prep_world", world_name])


d.set_cell_clicked_event(occlusion_toggle)
d.set_key_pressed_event(key_pressed)

while True:
    d.update()
    sleep(.05)



