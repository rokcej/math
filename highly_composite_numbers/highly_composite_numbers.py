# Find highly composite numbers

import math
from tabulate import tabulate
from tqdm import tqdm

# Configuration
MAX_N = 100000 # Highest number to test
# Output formatting
TABULATE_KWARGS = { "tablefmt": "simple_grid", "floatfmt": ",.2f", "intfmt": "," }

# If n is the factorial of k, return k; otherwise return None
def inverse_factorial(n: int) -> int | None:
	k = 1
	k_factorial = 1
	while k_factorial < n:
		k += 1
		k_factorial *= k
	return k if k_factorial == n else None

# d(n)
def num_divisors(n: int) -> int:
	count = 0
	ceil_sqrt = int(math.ceil(math.sqrt(n)))
	for div in range(1, ceil_sqrt):
		if n % div == 0:
			count += 2 # We count both div and n/div
	if ceil_sqrt * ceil_sqrt == n:
		count += 1
	return count


table = []
d_max = -1
for n in tqdm(range(1, MAX_N + 1)):
	d_n = num_divisors(n)
	if d_n > d_max:
		d_max = d_n
		index = len(table) + 1
		inv_fac = inverse_factorial(n)
		inv_fac_str = f"{inv_fac}!" if inv_fac else ""
		table.append([index, n, d_n, inv_fac_str])
print(tabulate(table, headers=("", "HCN n", "d(n)", "k!"), stralign="right", **TABULATE_KWARGS))
