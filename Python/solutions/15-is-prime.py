# Write a method that takes in an integer (greater than one) and
# returns True if it is prime; otherwise return False.
#
# You may want to use the `%` modulo operation. `5 % 2` returns the
# remainder when dividing 5 by 2; therefore, `5 % 2 == 1`. In the case
# of `6 % 2`, since 2 evenly divides 6 with no remainder, `6 % 2 == 0`.
# More generally, if `m` and `n` are integers, `m % n == 0` if and only
# if `n` divides `m` evenly.
#
# You would not be expected to already know about modulo for the
# challenge.
#
# Difficulty: medium.

# ITERATIVE SOLUTION
# def is_prime(number):
#     if number in [2,3]: return True
#     possible_divisors = range(2, int(number / 2) + 1)
#     for possible_divisor in possible_divisors:
#         if number % possible_divisor == 0:
#             return False
#     return True

# RECURSIVE SOLUTION
def is_prime(number, candidate_divisor = None):
    if number in [2,3]: return True
    if candidate_divisor == 1: return True

    candidate_divisor = candidate_divisor or number - 1
    if number % candidate_divisor == 0:
        return False
    return is_prime(number, candidate_divisor - 1)

# These are tests to check that your code is working. After writing
# your solution, they should all print True.

print('is_prime(2) == True: ' + str(is_prime(2) == True))
print('is_prime(3) == True: ' + str(is_prime(3) == True))
print('is_prime(4) == False: ' + str(is_prime(4) == False))
print('is_prime(5) == True: ' + str(is_prime(5) == True))
print('is_prime(9) == False: ' + str(is_prime(9) == False))
print('is_prime(13) == True: ' + str(is_prime(13) == True))
print('is_prime(14) == False: ' + str(is_prime(14) == False))
