# Write a method that takes an array of numbers. If a pair of numbers
# in the array sums to zero, return the positions of those two numbers.
# If no pair of numbers sums to zero, return `None`.
#
# Difficulty: medium.

def two_sum(nums):
    for index_i, num_i in enumerate(nums):
        for index_j, num_j in enumerate(nums):
            if index_i != index_j and num_i + num_j == 0:
                return [index_i, index_j]
    return None

# These are tests to check that your code is working. After writing
# your solution, they should all print True.

print(
  'two_sum([1, 3, 5, -3]) == [1, 3]: ' + str(two_sum([1, 3, 5, -3]) == [1, 3])
)
print(
  'two_sum([1, 3, 5]) == None: ' + str(two_sum([1, 3, 5]) == None)
)
