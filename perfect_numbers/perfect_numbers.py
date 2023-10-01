# Find perfect numbers

import math
from tabulate import tabulate
from tqdm import tqdm

# Configuration
MAX_N = 100000 # Highest number to test
# Output formatting
TABULATE_KWARGS = { "tablefmt": "simple_grid", "floatfmt": ",.2f", "intfmt": "," }


# Perfect number validation functions
def get_divisors(n: int) -> list[int]:
	divisors = []
	ceil_sqrt = int(math.ceil(math.sqrt(n)))
	for div in range(1, ceil_sqrt):
		if n % div == 0:
			divisors.extend([div, n // div])
	if ceil_sqrt * ceil_sqrt == n:
		divisors.append(ceil_sqrt)
	return sorted(divisors)

def is_perfect(n: int) -> bool:
	return sum(get_divisors(n)) - n == n


# Compute perfect numbers
table = []
for n in tqdm(range(1, MAX_N + 1)):
	if is_perfect(n):
		index = len(table) + 1
		divisors = get_divisors(n)
		d_n = len(divisors)
		table.append([index, n, d_n, get_divisors(n)])
print(tabulate(table, headers=("", "PN n", "d(n)", "Divisors of n"), **TABULATE_KWARGS))
