import numpy as np
from turtle import *


# Gravitational constant
G = 6.67428e-11

# Distance scale
SCALE = 1e-9

# A step
dphi = 0.05 * 1 / np.pi


class Simulation(Turtle):
    '''
    Draws the orbit based on the parameters
    - mechanical energy, masses, and angular momentum.
    '''


    def __init__(self, m, M, E, L):
        super(Simulation, self).__init__(visible=False)

        self.e = 1 + 2 * E * L**2 / (G**2 * M**2 * m**3)
        self.r0 = L**2 / (G * M * m**2)

        self.r = 0.0
        self.phi = 0.0

    def update_position(self):
        self.setpos(self.r * np.cos(self.phi), self.r * np.sin(self.phi))

    def update_parameters(self):
        self.phi += dphi

        self.r = self.r0 / (1 + self.e * np.cos(self.phi)) * SCALE

    def run(self):
        self.penup()
        self.radians()

        self.pencolor(0, 255, 186)

        while 1:
            self.update_parameters()

            self.update_position()

            self.dot(2, (0, 255, 186))


def main():
    radians()
    colormode(255)

    screen = Screen()
    screen.bgcolor('black')

    m = screen.numinput('Korbit', 'Enter the planet mass(kg): ')
    M = screen.numinput('Korbit', 'Enter the central body mass(kg): ')
    E = screen.numinput('Korbit', 'Enter the mechanical energy(J): ')
    L = screen.numinput('Korbit', 'Enter the angular momentum(Js): ')

    sim = Simulation(m, M, E, L)
    sim.run()


if __name__ == '__main__':
    main()
