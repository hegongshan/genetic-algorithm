import math
import random


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
        individual = []
        for j in range(len(data)):
            individual.append(data[j])
        random.shuffle(individual)

        if individual not in population:
            population.append(individual)

    return population


def selection(population, new_population_size):
    return sorted(population, key=lambda x: fitness_function(x))[:new_population_size]


def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b


def crossover(parent1, parent2):
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


def mutation(individual, mutation_threshold=0.9):
    if random.random() > mutation_threshold:
        start = random.randint(1, len(individual) - 1)
        end = random.randint(start, len(individual) - 1)
        tmp = individual[start:end + 1]
        random.shuffle(tmp)
        individual[start:end + 1] = tmp

    return individual


def genetic_algorithm(data, population_size, num_iterations):
    population = initial_population(population_size=population_size, data=data)
    for _ in range(num_iterations):
        new_population_size = len(population) - 2
        population = selection(population=population, new_population_size=new_population_size)

        new_population = []

        while len(new_population) < new_population_size:
            parent1, parent2 = random.sample(population, 2)
            child1, child2 = crossover(parent1, parent2)

            child1 = mutation(child1)
            child2 = mutation(child2)

            new_population.append(child1)
            new_population.append(child2)

        population = new_population

    return population


def plot(path):
    import matplotlib.pyplot as plt

    path.append(path[0])

    x = [point[0] for point in path]
    y = [point[1] for point in path]

    plt.plot(x, y, 'r-o')

    for i, txt in enumerate(path):
        plt.annotate(txt, (x[i], y[i]), textcoords='offset points', xytext=(0, 10), ha='center')

    plt.show()


if __name__ == '__main__':
    data = [(0, 1), (1, 0), (2, 0), (11, 10), (22, 23), (33, 35), (15, 13), (20, 3)]

    random.seed(33)
    population = genetic_algorithm(data=data, population_size=800, num_iterations=300)
    best_path = min(population, key=lambda x: fitness_function(x))
    print(f'The best path: {best_path}')
    print(f'The fitness value: {fitness_function(best_path)}')
    plot(best_path)
