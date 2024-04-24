from classes.Route import Route
from classes.Genetic import Genetic


def algorithm(population_size=10, chromosome_length=10, mutation_rate=0.1, generations=10):
    route = Route(CITIES)

    population_size = population_size
    chromosome_length = chromosome_length
    mutation_rate = mutation_rate
    generations = generations

    ga = Genetic(population_size, chromosome_length, mutation_rate, generations, route)

    best_individual = ga.evolve(route)

    current_population = ga.initialize_population(route)

    print("Первые 5 особей:")
    for i in range(5):
        print("Хромосома:", current_population[i].chromosome, "Приспособленность:", current_population[i].fitness)

    print("\nПоследние 5 особей:")
    for i in range(-1, -6, -1):
        print("Хромосома:", current_population[i].chromosome, "Приспособленность:", current_population[i].fitness)

    print("\nСамая лучшая особь:")
    print("Хромосома:", best_individual.chromosome)
    print("Приспособленность:", best_individual.fitness)



if __name__ == '__main__':


    CITIES = [
        (47.15389021, 39.73343477),
        (47.27843879, 39.66504917),
        (47.27908131, 39.8532115),
        (47.23956633, 39.686936),
        (47.23876258, 39.72910032),
        (47.26100013, 39.7189723),
        (47.21593813, 39.67961893),
        (47.2294162, 39.6284853),
        (47.23343191, 39.75903914),
        (47.25423635, 39.76570175),
        (47.23600049, 39.59843919),
        (47.29597385, 39.71406386),
        (47.29408339, 39.70305607),
        (47.26360024, 39.85908554),
        (47.22374472, 39.72594068),
        (47.28950657, 39.71387074),
        (47.28401677, 39.7063391),
        (47.28298007, 39.71715376),
        (47.26878544, 39.88010333),
        (47.23348307, 39.71436963),
        (47.22882423, 39.69366298),
        (47.23015798, 39.68220458),
        (47.27205698, 39.75013421)
    ]

    POPULATION_SIZE = 10
    CHROMOSOME_LENGTH = 10
    MUTATION_RATE = 0.1
    GENERATIONS = 10

    algorithm(
        POPULATION_SIZE,
        CHROMOSOME_LENGTH,
        MUTATION_RATE,
        GENERATIONS,
    )