import os
import sys
import math
from .assests import *
from .physics import *

class Scenario:

    def __init__(self, size, spacecraft, planets, sc_start_pos=None):

        self.size = size
        self.sc = spacecraft
        self.planets = planets
        self.sc_start_pos = sc_start_pos

        if not self.sc_start_pos:
            self.sc_start_pos = self._make_sc_start_pos()

        self.initial_orbit_pos = {}
        for planet in planets:
            self.initial_orbit_pos.update({
                planet: planet.orbit.progress
            })

        self.reset_pos()

    def _make_sc_start_pos(self):
        '''
        Default starting position assumed to be bottom centre of screen
        '''

        return self.size[0] / 2, self.size[1]-25

    def reset_pos(self):

        self.sc.reset(self.sc_start_pos)

        for planet in self.planets:
            planet.orbit.progress = self.initial_orbit_pos[planet]

    def update_sc_pos(self, impulse_time, closest_only=True):

        planet_f = 0.0

        if closest_only:
            closes_planet = find_closest_planet(self.sc, self.planets)

            if closes_planet:
                planet_f = self.sc.calc_gravitational_force(closes_planet)
        else:
            for planet in self.planets:
                planet_f += self.sc.calc_gravitational_force(planet)

        self.sc.set_net_momentum(impulse_time, planet_f)
        self.sc.move(impulse_time)

        return self.sc.x, self.sc.y

    def update_all_pos(self, impulse_time):

        [planet.move(impulse_time) for planet in self.planets]
        self.update_sc_pos(impulse_time)

def find_closest_planet(sc, planets):

    current_distance = sc.calc_distance(planets[0])
    index_of_closest = 0
    current_index = 0
    for num in range(len(planets)):
        if sc.calc_distance(planets[current_index]) < current_distance:
            index_of_closest = current_index
            current_distance = sc.calc_distance(planets[current_index])
        current_index += 1

    return planets[index_of_closest]
