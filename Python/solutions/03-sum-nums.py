# Write a method that takes in an integer `num` and returns the sum of
# all integers between zero and num, up to and including `num`.
#
# Difficulty: easy.

# ITERATIVE SOLUTION
# def sum_nums(num):
#     result = 0
#     n = num
#     while n > 0:
#         result += n
#         n -= 1
#     return result

# RECURSIVE SOLUTION
def sum_nums(num):
    if num == 1: return num
    return num + sum_nums(num - 1)

# These are tests to check that your code is working. After writing
# your solution, they should all print True.

print('sum_nums(1) == 1: ' + str(sum_nums(1) == 1))
print('sum_nums(2) == 3: ' + str(sum_nums(2) == 3))
print('sum_nums(3) == 6: ' + str(sum_nums(3) == 6))
print('sum_nums(4) == 10: ' + str(sum_nums(4) == 10))
print('sum_nums(5) == 15: ' + str(sum_nums(5) == 15))
