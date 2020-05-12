import sys
sys.path.append("../")

from spaceshots_core.game import *
from spaceshots_core.scene import LevelBuilder

builder = LevelBuilder(900,700)
scene = builder.create("medium")
print(scene)

# screen_x, screen_y = 900,700
# sc = Spacecraft('Test', mass = 100, thrust_force = 3000, gas_level = 600)
# orbit = Orbit(a=screen_x*500/1920, b=screen_y*500/1080, center_x=screen_x, center_y=screen_y/2, CW=True, angular_step = 2*np.pi/(200.0), progress = np.pi/2)
# planet = Planet('Test', mass = 3e16, orbit = orbit)
# scene = Scene((screen_x, screen_y),sc, [planet], win_region = ([0,0], [screen_x, 0]), win_velocity = 90.0,)
# game = Game(scenes=[scene])

def get_command(scene):
    return 1

level_won, level_fail = False, False

while not game.done or not level_won or not level_fail:
    
    command = get_command(game.current_scene)
    level_won, level_failed = game.step(command) # iterate next time step    
    
    # print("SC", game.current_scene.sc.x, game.current_scene.sc.y) 
    print("SC", game.current_scene.sc.vel)    
    # print("Won", level_won, "Failed", level_failed)
    