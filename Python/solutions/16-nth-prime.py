# Write a method that returns the `n`th prime number. Recall that only
# numbers greater than 1 can be prime.
#
# Difficulty: medium.

def is_prime(number):
    if number in [2,3]: return True

    possible_divisors = range(2, int(number / 2) + 1)
    for possible_divisor in possible_divisors:
        if number % possible_divisor == 0:
            return False
    return True

def nth_prime(n):
    prime_count = 0
    candidate_number = 2

    while prime_count < n:
        if is_prime(candidate_number): prime_count += 1
        candidate_number += 1
    return candidate_number - 1

# These are tests to check that your code is working. After writing
# your solution, they should all print True.

print('nth_prime(1) == 2: ' + str(nth_prime(1) == 2))
print('nth_prime(2) == 3: ' + str(nth_prime(2) == 3))
print('nth_prime(3) == 5: ' + str(nth_prime(3) == 5))
print('nth_prime(4) == 7: ' + str(nth_prime(4) == 7))
print('nth_prime(5) == 11: ' + str(nth_prime(5) == 11))
