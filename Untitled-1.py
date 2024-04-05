# def parfaite(N):
#     S= 0
#     for i in range(1, N):
#         if N % i == 0:
#             S += i
#     if S == N:
#         print(N)

# for i in range(1, 100_000):
#     parfaite(i)

##################################

import math
import time

def sum_of_divisors(n):
    if n <= 1:
        return 0
    total_sum = 1  # Include 1 as a proper divisor
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            total_sum += i
            if i != n // i:
                total_sum += n // i
    return total_sum

def is_perfect_number(n):
    return n == sum_of_divisors(n)

# Measure execution time for finding perfect numbers up to 100,000
start_time = time.time()

for i in range(1, 100_000):
    if is_perfect_number(i):
        print(i)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.4f} seconds")
print("Fin du programme 1 ")

################


def sum_of_divisors(n):
    if n <= 1:
        return 0
    total_sum = 1  # Include 1 as a proper divisor
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            total_sum += i
            if i != n // i:
                total_sum += n // i
    return total_sum

def is_perfect_number(n):
    return n == sum_of_divisors(n)

def precompute_perfect_numbers(up_to):
    perfect_numbers = []
    for n in range(1, up_to + 1):
        if is_perfect_number(n):
            perfect_numbers.append(n)
    return perfect_numbers

# Measure execution time for precomputing and then using perfect numbers up to 100,000
start_time = time.time()

perfect_numbers_up_to_100000 = precompute_perfect_numbers(100_000)

# Use the precomputed list
for number in perfect_numbers_up_to_100000:
    print(number)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.4f} seconds")
print("Fin du programme 2 ")