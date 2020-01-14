from game_engine import *

# Main building
draw_square( Square(-100, 0, 200, "grey") )

# Roof
draw_isosceles( IsoscelesTriangle(-100, 200, 200, 80, "green"))

# Window 1
draw_square( Square(-75, 125, 50, "black"))




renderDrawing()