# -*- Coding: utf-8 *-*
import random
import math

def solve(points, population_size, mutation_probability, iterations_number):
    fitness = (lambda p: (
            lambda q: _fitness_function(p, q)
            ))(points)
    generation = _init_generation(population_size, len(points))
    for _ in range(0, iterations_number):
        generation.sort(key=fitness)
        yield (fitness(generation[0]), generation[0][:])
        generation = generation[0:int(population_size / 2)]
        for i in range(0, int(population_size / 2), 2):
            generation.append(_crossover(generation[i], generation[i + 1]))
            generation.append(_crossover(generation[i + 1], generation[i]))
        for i in range(0, population_size):
            if random.random() < mutation_probability:
                generation[i] = _mutate(generation[i])
    generation.sort(key=fitness)
    yield (fitness(generation[0]), generation[0][:])
    return

def _fitness_function(points, individual):
    fitness = 0.0;
    for i in range(0, len(individual) - 1):
        point_a = points[individual[i]]
        point_b = points[individual[(i + 1) % len(individual)]]
        fitness = fitness + math.sqrt(((point_a[0] - point_b[0]) ** 2) + ((point_a[1] - point_b[1]) ** 2))
    return fitness

def _mutate(individual):
    selected_city = individual[random.randint(0, len(individual) - 1)]
    new_individual = list(filter(lambda x: False if x == selected_city else True, individual))
    new_individual.insert(random.randint(0, len(new_individual)), selected_city)
    return new_individual

def _init_generation(population_size, number_of_cities):
    generation = []
    for i in range(0, population_size):
        new_individual = list(range(0, number_of_cities))
        random.shuffle(new_individual)
        generation.append(new_individual)
    return generation

def _normalize(individual):
    new_individual = individual[:]
    while new_individual[0] != 0:
        old_head = new_individual.pop(0)
        new_individual.append(old_head)
    return new_individual

def _cont_crossover(child):
    try:
        child.index(-1)
        return True
    except ValueError:
        return False

def _crossover(mother, father):
    mother = _normalize(mother)
    father = _normalize(father)
    child = list(range(0, len(mother)))
    for i in range(0, len(child)):
        child[i] = -1 if i != 0 else 0
    left_corner = 1
    right_corner = len(mother) - 1
    for i in range(1, len(mother)):
        while (mother[left_corner] in child) and (left_corner < len(mother)):
            left_corner = left_corner + 1
        if _cont_crossover(child):
            child[i] = mother[left_corner]
        else:
            break
        while (father[right_corner] in child) and (right_corner >= 0):
            right_corner = right_corner - 1
        if _cont_crossover(child):
            child[len(mother) - i] = father[right_corner]
        else:
            break
    return child
