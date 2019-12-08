# DAY 06

class celestial_body():
    def __init__(self, name):
        self.body_name = name
        self.orbiting_bodies = []
        self.in_orbit_around = None

bodies = {}
with open('advent06.txt', 'r') as orbit_file:
    for orbit_line in orbit_file:
        orbits = orbit_line.split(')')
        lhs = orbits[0].strip()
        rhs = orbits[1].strip()
        if lhs not in bodies:
            bodies[lhs] = celestial_body(lhs)
        bodies[lhs].orbiting_bodies.append(rhs)
        if rhs not in bodies:
            bodies[rhs] = celestial_body(rhs)
        bodies[rhs].in_orbit_around = lhs
        

def find_orbits(body_name, bodies, curr_depth):
    if body_name in bodies:
        sub_orbits = 0
        for body in bodies[body_name].orbiting_bodies:
            sub_orbits += find_orbits(body, bodies, curr_depth + 1)
        sub_orbits += curr_depth
        return sub_orbits
    else:
        return curr_depth
        
santa_orbit = bodies['SAN']
santa_path_to_com = []
curr_planet = santa_orbit
while curr_planet.body_name != 'COM':
    santa_path_to_com.append(curr_planet.body_name)
    curr_planet = bodies[curr_planet.in_orbit_around]
you_orbit = bodies['YOU']
you_path_to_com = []
curr_planet = you_orbit
while curr_planet.body_name != 'COM':
    if curr_planet.body_name in santa_path_to_com:
        break
    you_path_to_com.append(curr_planet.body_name)
    curr_planet = bodies[curr_planet.in_orbit_around]
santa_index = santa_path_to_com.index(curr_planet.body_name)
print(len(you_path_to_com) + santa_index - 2)