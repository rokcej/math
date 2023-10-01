import math
from collections import defaultdict
from tabulate import tabulate
from tqdm import tqdm

# Configuration
MAX_N = 1000000 # Highest number to test
MAX_B = 16      # Highest radix (base) to test
# Output formatting
TABULATE_KWARGS = { "tablefmt": "simple_grid", "floatfmt": ",.2f", "intfmt": "," }
PRINT_INTERMEDIATE_RESULTS = True


# Helper functions
def is_power_of_two(n):
    return (n & (n-1) == 0) and (n != 0)

def is_power_of_ten(n):
    while n > 1:
        if n % 10 != 0:
            return False
        n //= 10
    return n == 1


# Radix economy functions
def E(b: int, n: int) -> float:
    return b * math.floor(math.log(n, b) + 1)

def E_asymptotic(b: int) -> float: 
    return b / math.log(b)


# Find best radices
b_counts = defaultdict(int)
best_table = []

for n in tqdm(range(1, MAX_N + 1)):
    economies = dict()
    for b in range(2, MAX_B + 1):
        economies[b] = E(b, n)
    best_b_for_n = min(economies, key=economies.get)
    b_counts[best_b_for_n] += 1

    if is_power_of_ten(n):
        total_count = sum(b_counts.values())
        assert total_count == n, "Total count and N should be equal"

        best_b = sorted(b_counts, key=b_counts.get)[-1]
        best_count = b_counts[best_b]
        best_ratio = best_count / total_count
        best_table.append([n, best_b, best_count, best_ratio])

        if PRINT_INTERMEDIATE_RESULTS:
            tqdm.write(f" N <= {n:,} ")
            intermediate_table = []
            for b, count in sorted(b_counts.items()):
                ratio = count / total_count
                intermediate_table.append((b, count, ratio))
            tqdm.write(tabulate(intermediate_table, headers=["Base", "Count", "Ratio"], **TABULATE_KWARGS))
            tqdm.write("")

print()
print(" BEST BASES ")
print(tabulate(best_table, headers=["Max N", "Base", "Count", "Ratio"], **TABULATE_KWARGS))
