import random
import numpy as np

class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = None

    def calculate_fitness(self, route):
        route.calculate_distance()
        self.fitness = 1 / route.distance
        return self.fitness