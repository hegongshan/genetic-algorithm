import random


def sort_selection(population, new_population_size, fitness_function):
    return sorted(population, key=lambda x: fitness_function(x))[:new_population_size]


def roulette_wheel_selection(population, new_population_size, fitness_function):
    weights = []
    for i in range(len(population)):
        weights.append(fitness_function(population[i]))
    x = random.choices(population, weights, k=new_population_size)
    return x
