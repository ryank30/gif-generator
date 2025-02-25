import numpy as np
import pyvista as pv

mesh = pv.examples.load_ant()
texture = pv.examples.load_ant()

pl = pv.Plotter(off_screen= False)
pl.add_mesh(
    mesh,
    style = "points",
    render_points_as_spheres = True,
    emissive=True,
    color = "#fff7c2",
    opacity=1,
    point_size= 8.0,
    show_scalar_bar=False,)

pl.add_text("Ant", color = "b")
pl.background_color = "k"
pl.enable_eye_dome_lighting()
pl.show()
