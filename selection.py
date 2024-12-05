import random


def sort_selection(population, new_population_size, fitness_function):
    return sorted(population, key=lambda x: fitness_function(x))[:new_population_size]


def roulette_wheel_selection(population, new_population_size, fitness_function):
    fitness_values = [fitness_function(individual) for individual in population]
    fitness_value_sum = sum(fitness_values)

    weights = [fitness_value / fitness_value_sum for fitness_value in fitness_values]
    return random.choices(population, weights, k=new_population_size)
