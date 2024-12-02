import random


def sort_selection(population, new_population_size, fitness_function):
    return sorted(population, key=lambda x: fitness_function(x))[:new_population_size]


def roulette_wheel_selection(population, new_population_size, fitness_function):
    weights = [fitness_function(individual) for individual in population]
    x = random.choices(population, weights, k=new_population_size)
    return x
