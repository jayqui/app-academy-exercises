# Write a method that takes an array of numbers in. Your method should
# return the third greatest number in the array. You may assume that
# the array has at least three numbers in it.
#
# Difficulty: medium.

def third_greatest(nums):
    greatest_so_far = [0, 0, 0]

    for num in nums:
        for greatest_index, big_num in enumerate(greatest_so_far):
            if num > big_num:
                greatest_so_far.insert(greatest_index, num)
                greatest_so_far.pop()
                break
    return greatest_so_far[2]


# These are tests to check that your code is working. After writing
# your solution, they should all print True.

print(
  'third_greatest([5, 3, 7]) == 3: ' +
  str(third_greatest([5, 3, 7]) == 3)
)
print(
  'third_greatest([5, 3, 7, 4]) == 4: ' +
  str(third_greatest([5, 3, 7, 4]) == 4)
)
print(
  'third_greatest([2, 3, 7, 4]) == 3: ' +
  str(third_greatest([2, 3, 7, 4]) == 3)
)
