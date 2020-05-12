import sys
import pygame
sys.path.append("../")

from spaceshots_core.game import *
from spaceshots_core.scene import LevelBuilder

# Setup Pygame
pygame.init()
screen_x, screen_y = 1280, 720
screen = pygame.display.set_mode((screen_x, screen_y))
screen.fill((0, 0, 0))

# Game
# builder = LevelBuilder(screen_x, screen_y)
# scene = builder.create("medium")

sc = Spacecraft('Test', mass = 100, thrust_force = 3000, gas_level = 600)
orbit = Orbit(a=screen_x*500/1920, b=screen_y*500/1080, center_x=screen_x, center_y=screen_y/2, CW=True, angular_step = 2*np.pi/(200.0), progress = np.pi/2)
planet = Planet('Test', mass = 3e16, orbit = orbit)
scene = Scene((screen_x, screen_y),sc, [planet], win_region = ([0,0], [screen_x, 0]), win_velocity = 90.0,)
game = Game(scenes=[scene])

level_won, level_fail = False, False
command = 0

while not level_won and not level_fail:
        
        screen.fill((0, 0, 0))
        
        # Get command
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                level_won = True
            
            elif event.type == pygame.KEYDOWN and event.key in [pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT]:
                    if event.key == pygame.K_DOWN:
                            command = 3
                    if event.key == pygame.K_UP:
                            command = 1
                    if event.key == pygame.K_RIGHT:
                            command = 4
                    if event.key == pygame.K_LEFT:
                            command = 2
            elif event.type == pygame.KEYUP and event.key in [pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT]:
                command = 0
        
        level_won, level_fail = game.step(command)
        print(sc.gas_level, sc.thrust_direction)
        
        # Goal post
        p1 = game.current_scene.win_region[0][0], game.current_scene.win_region[1][0]
        p2 = game.current_scene.win_region[0][1], game.current_scene.win_region[1][1]
        pygame.draw.line(screen, (0.0, 255, 174), p1, p2, 15)
        
        # Planet
        for planet in game.current_scene.planets:
                pygame.draw.ellipse(screen, (100,100,100), pygame.Rect(planet.x-25, planet.y-25, 50, 50))
                # Orbit
                pygame.draw.ellipse(screen, (255,255,255), pygame.Rect(planet.orbit.center_x-planet.orbit.a, planet.orbit.center_y-planet.orbit.b, planet.orbit.a*2, planet.orbit.b*2), 1)
        
        
        pygame.draw.polygon(screen, (255,100,100), game.current_scene.sc.poly.exterior.coords)
               
        pygame.display.update()
        
pygame.quit()
