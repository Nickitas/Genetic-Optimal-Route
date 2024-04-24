import random
import numpy as np
from classes.Individual import Individual


class Genetic:
    def __init__(self, population_size, chromosome_length, mutation_rate, generations, route):
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.route = route

    def initialize_population(self, route):
        population = []
        for _ in range(self.population_size):
            chromosome = np.random.permutation(self.chromosome_length)
            individual = Individual(chromosome)
            individual.calculate_fitness(route)
            population.append(individual)
        return population

    def selection(self, population):
        selected = []
        tournament_size = min(2, len(population))
        for _ in range(self.population_size // 2):
            participants = random.sample(population, tournament_size)
            for winner in participants:
                selected.append(winner)
        return selected



    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, len(parent1.chromosome) - 1)
        child1_chromosome = np.concatenate((parent1.chromosome[:crossover_point], [gene for gene in parent2.chromosome if gene not in parent1.chromosome[:crossover_point]]))
        child2_chromosome = np.concatenate((parent2.chromosome[:crossover_point], [gene for gene in parent1.chromosome if gene not in parent2.chromosome[:crossover_point]]))
        offspring1 = Individual(child1_chromosome)
        offspring2 = Individual(child2_chromosome)
        return offspring1, offspring2

    def mutation(self, individual):
        mutation_rate = 0.1
        if random.random() < mutation_rate:
            idx1, idx2 = random.sample(range(len(individual.chromosome)), 2)
            individual.chromosome[idx1], individual.chromosome[idx2] = individual.chromosome[idx2], individual.chromosome[idx1]

    def replacement(self, population, offspring_population):
        combined_population = population + offspring_population
        filtered_population = [individual for individual in combined_population if individual.fitness is not None]
        sorted_population = sorted(filtered_population, key=lambda x: x.fitness, reverse=True)
        new_population = sorted_population[:len(population)]
        return new_population

    def evolve(self, route):
        population = self.initialize_population(route)
        for generation in range(self.generations):
            selected_population = self.selection(population)
            offspring_population = []
            for i in range(0, self.population_size, 2):
                parent1 = selected_population[i]
                parent2 = selected_population[i+1]
                offspring1, offspring2 = self.crossover(parent1, parent2)
                offspring_population.extend([offspring1, offspring2])
            for individual in offspring_population:
                if random.random() < self.mutation_rate:
                    self.mutation(individual)
            population = self.replacement(population, offspring_population)
        best_individual = max(population, key=lambda x: x.fitness)
        return best_individual