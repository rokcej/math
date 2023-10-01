# Radix Economy

## Introduction

Radix economy of a number $N$ in a particular base $b$ is defined as the number of digits needed to express $N$ in base $b$, multiplied by the base $b$. This can be used to evaluate the relative cost of using different bases to represent $N$.

Asymptotically ($N \rightarrow \infty$), base 3 has the best radix economy. But what is the best base for lower values of $N$? How does the best base change as $N$ increases?

Just to clarify, we are only interested in values of $b$ and $N$ that are integers ($b, N  \in \N; b \ge 2$).

## Equations

* Radix economy: $E(b, N) = b \lfloor \log_b(N) + 1 \rfloor$  
* Asymptotic approximation: $\frac{E(b, N)}{\ln(N)} \sim \frac{b}{\ln(b)}$

## Results

The following table shows bases with the most common lowest radix economy up to different values of $N$.

|         Max N |   Base |       Count |   Ratio |
|--------------:|:------:|------------:|:-------:|
|             1 |      2 |           1 |    1.00 |
|            10 |      2 |           7 |    0.70 |
|           100 |      2 |          69 |    0.69 |
|         1,000 |      2 |         636 |    0.64 |
|        10,000 |      3 |       5,800 |    0.58 |
|       100,000 |      3 |      76,229 |    0.76 |
|     1,000,000 |      3 |     891,232 |    0.89 |
|    10,000,000 |      3 |   9,388,404 |    0.94 |
|   100,000,000 |      3 |  969,60,096 |    0.97 |
| 1,000,000,000 |      3 | 991,882,532 |    0.99 |

**Fun fact**: it appears that for **any** given value of $N$, the best radix economy is **always** obtained for $b \in \{2, 3, 5\}$. Furthermore, $b=5$ yields the best radix economy for only a single number, $N=4$ (tested for $N \le 10^9$).

## Sources

* https://en.wikipedia.org/wiki/Radix_economy
