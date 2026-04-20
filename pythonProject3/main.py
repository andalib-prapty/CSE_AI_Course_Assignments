import random

values = [10, 7, 12, 8, 15]
weights = [2, 3, 4, 5, 7]
capacity = 12

def fitness(chrom):
    total_weight = sum(w * c for w, c in zip(weights, chrom))
    total_value = sum(v * c for v, c in zip(values, chrom))

    if total_weight > capacity:
        return 0
    return total_value


def int_to_chrom(i):
    return [int(b) for b in format(i, "05b")]

all_chromosomes = [int_to_chrom(i) for i in range(32)]

# TOP 8 chromosomes

sorted_chromosomes = sorted(all_chromosomes, key=lambda c: fitness(c), reverse=True)
top8 = sorted_chromosomes[:8]

#  Divide top 8 into 4 groups

groups = [top8[i:i+2] for i in range(0, 8, 2)]

# Step 4: Tournament Selection

winners = []
for group in groups:
    c1, c2 = group
    winners.append(max([c1, c2], key=lambda c: fitness(c)))

# Step 5: Pair winners for crossover (2 pairs)

crossover_pairs = [(winners[i], winners[i+1]) for i in range(0, 4, 2)]

# Step 6: Crossover (string split)
def crossover(p1, p2):
    point = random.randint(1, 4)
    child1 = p1[:point] + p2[point:]
    child2 = p2[:point] + p1[point:]
    return child1, child2


offspring = []

for p1, p2 in crossover_pairs:
    c1, c2 = crossover(p1, p2)
    offspring.extend([c1, c2])


# Mutation (bit flip)

def mutate(chrom):
    idx = random.randint(0, 4)
    chrom[idx] = 1 - chrom[idx]
    return chrom


mutated_offspring = []
for child in offspring:
    mutated = mutate(child[:])  # copy for safety
    mutated_offspring.append(mutated)


best_chrom = None
best_value = -1
best_weight = 0

for chrom in all_chromosomes:
    total_weight = sum(weights[i] * chrom[i] for i in range(5))
    total_value = sum(values[i] * chrom[i] for i in range(5))

    if total_weight <= capacity and total_value > best_value:
        best_value = total_value
        best_chrom = chrom
        best_weight = total_weight


print("Best Chromosome:", best_chrom)
print("Total Value:", best_value)
print("Total Weight:", best_weight)


