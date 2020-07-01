# Multiple Organisms
import random
import string

SIZE = 30
TARGET = 'Hello World'
pool = []

def fitness(enter, target):
	fit = 0
	for i in range(0, len(enter)):
		fit += abs(ord(target[i]) - ord(enter[i]))
	return(fit)

def mutate(parent1, parent2):
    child = list(parent1['dna'])
    
    start = random.randint(0, len(parent2['dna']) -1)
    end = random.randint(0, len(parent2['dna']) - 1)
    if(start > end):
        end, start = start, end

    child[start:end] = parent2['dna'][start:end]
    index = random.randint(0, len(child) - 1)
    child[index] = chr(ord(child[index]) + random.randint(-1, 1))
    candidate = {'dna': ''.join(child), 'fitness': fitness(child, TARGET)}
    return(candidate)

def random_parent(pool):
    index = random.random() * random.random() * (SIZE - 1)
    index = int(index)
    return(pool[index])

def genesis(spec):
    to = ''
    for i in range(spec):
        to += random.choice(string.ascii_letters) 
    return(to)

for i in range(SIZE):
    dna = genesis(len(TARGET))
    fit = fitness(dna, TARGET)
    candidate = {'dna': dna, 'fitness': fit}
    pool.append(candidate)

i = 0
while True:
    i += 1
    pool.sort(key=lambda candidate: candidate['fitness'])
    if pool[0]['fitness'] == 0:
        print('Target reached!')
        break
    child = mutate(random_parent(pool), random_parent(pool))
    if child['fitness'] < pool[-1]['fitness']:
        pool[-1] = child
    stats = []
    for j in range(len(pool)):
        stats.append(pool[j]['dna'])
    stats = '\n'.join(stats)
    print('\nGeneration: {i}'.format(i = i))
    print(stats)