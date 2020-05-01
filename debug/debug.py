import sys
sys.path.append("../")

from deflectiun_core.game import *
from deflectiun_core.scene import LevelBuilder

builder = LevelBuilder(1920, 1080)
scene = builder.create("medium")
game = Game(scenes=[scene])

def get_command(scene):
    return 1

level_won, level_fail = False, False

while not game.done or not level_won or not level_fail:
    
    command = get_command(game.current_scene)
    level_won, level_failed = game.send_command(command) # iterate next time step    
    
    # print("SC", game.current_scene.sc.x, game.current_scene.sc.y) 
    print("SC", game.current_scene.sc.vel)    
    # print("Won", level_won, "Failed", level_failed)
    