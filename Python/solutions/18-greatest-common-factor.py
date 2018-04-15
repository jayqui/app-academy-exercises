# Write a method that takes in two numbers. Return the greatest
# integer that evenly divides both numbers. You may wish to use the
# `%` modulo operation.
#
# Difficulty: medium.

def greatest_common_factor(number1, number2):
    greater_number = number1 if number1 >= number2 else number2
    for possible_factor in reversed(range(1, greater_number)):
        if number1 % possible_factor == 0 and number2 % possible_factor == 0:
            return possible_factor

# These are tests to check that your code is working. After writing
# your solution, they should all print True.

print(
  'greatest_common_factor(3, 9) == 3: ' +
  str(greatest_common_factor(3, 9) == 3)
)
print(
  'greatest_common_factor(16, 24) == 8: ' +
  str(greatest_common_factor(16, 24) == 8)
)
print(
  'greatest_common_factor(3, 5) == 1: ' +
  str(greatest_common_factor(3, 5) == 1)
)
