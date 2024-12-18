import math
import random
from argparse import ArgumentParser

from selection import sort_selection, roulette_wheel_selection


def fitness_function(path):
    total = 0
    num_point = len(path)
    for i in range(num_point):
        x1, y1 = path[i % num_point]
        x2, y2 = path[(i + 1) % num_point]
        total += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return total


def initial_population(data, population_size):
    population = []
    for _ in range(population_size):
        individual = random.sample(data, len(data))
        if individual not in population:
            population.append(individual)

    return population


def selection(population, new_population_size, operator):
    if operator == 'sort':
        return sort_selection(population, new_population_size, fitness_function)
    if operator == 'roulette_wheel':
        return roulette_wheel_selection(population, new_population_size, fitness_function)

    print(f'Unsupported selection operator: {operator}')
    exit()


def crossover(parent1, parent2, crossover_rate):
    if random.random() >= crossover_rate:
        return parent1, parent2

    child1 = parent1.copy()
    child2 = parent2.copy()

    idx = random.randint(0, len(parent1) - 1)

    a = child1.index(child2[idx])
    b = child2.index(child1[idx])

    tmp = child1[a]
    child1[a] = child1[idx]
    child1[idx] = tmp

    tmp = child2[b]
    child2[b] = child2[idx]
    child2[idx] = tmp

    return child1, child2


def mutation(individual, mutation_rate):
    if random.random() < mutation_rate:
        start = random.randint(1, len(individual) - 1)
        end = random.randint(start, len(individual) - 1)
        tmp = individual[start:end + 1]
        random.shuffle(tmp)
        individual[start:end + 1] = tmp

    return individual


def genetic_algorithm(data, population_size, num_iterations, selection_operator, crossover_rate, mutation_rate):
    population = initial_population(data=data, population_size=population_size)
    for _ in range(num_iterations):
        new_population_size = len(population) - 2
        population = selection(population=population, new_population_size=new_population_size, operator=selection_operator)

        new_population = []

        while len(new_population) < new_population_size:
            parent1, parent2 = random.sample(population, 2)
            child1, child2 = crossover(parent1, parent2, crossover_rate)

            child1 = mutation(child1, mutation_rate)
            child2 = mutation(child2, mutation_rate)

            new_population.append(child1)
            new_population.append(child2)

        population = new_population

    best_path = min(population, key=lambda x: fitness_function(x))
    best_fitness_value = fitness_function(best_path)
    return best_path, best_fitness_value


def plot(path):
    import matplotlib.pyplot as plt

    path.append(path[0])

    x = [point[0] for point in path]
    y = [point[1] for point in path]

    plt.plot(x, y, 'r-o')

    for i, txt in enumerate(path):
        plt.annotate(txt, (x[i], y[i]), textcoords='offset points', xytext=(0, 10), ha='center')

    plt.show()


def parse_arg():
    args = ArgumentParser()
    args.add_argument('--data', type=str, required=True, help='Data.')
    args.add_argument('--population-size', type=int, default=800, help='Population size.')
    args.add_argument('--selection-operator', type=str, default='sort', help='sort|roulette_wheel')
    args.add_argument('--crossover-rate', type=float, default=0.1, help='Crossover rate.')
    args.add_argument('--mutation-rate', type=float, default=0.1, help='Mutation rate.')
    args.add_argument('--num-iterations', type=int, default=100, help='Number of iterations.')
    args.add_argument('--seed', type=int, default=33, help='Random seed.')
    args.add_argument('--plot-result', action='store_true', help='Plot the result.')
    return args.parse_args()


if __name__ == '__main__':
    args = parse_arg()

    random.seed(args.seed)

    best_path, best_fitness_value = genetic_algorithm(data=eval(args.data),
                                                      population_size=args.population_size,
                                                      selection_operator=args.selection_operator,
                                                      crossover_rate=args.crossover_rate,
                                                      mutation_rate=args.mutation_rate,
                                                      num_iterations=args.num_iterations, )

    print(f'The best path: {best_path}')
    print(f'The fitness value: {best_fitness_value}')

    if args.plot_result:
        plot(best_path)
