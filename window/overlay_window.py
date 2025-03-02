"""Demonstrates creation of a transparent overlay window in pyglet
"""

import pyglet

from pyglet.graphics import Batch
from pyglet.window import Window


batch = Batch()
window = Window(1800, 500, style=Window.WINDOW_STYLE_OVERLAY)
window.set_caption("Overlay Window")

circle = pyglet.shapes.Circle(250, 250, 50, color=(100, 250, 250), batch=batch)
moveRight = True

@window.event
def on_draw():
    global moveRight
    window.clear()
    if moveRight:
        circle.x += 4
        if circle.x >= 1750: moveRight = False
    else:
        circle.x -= 4
        if circle.x <= 50: moveRight = True

    batch.draw()


pyglet.app.run()
