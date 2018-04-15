# Write a method that takes in two numbers. Return the greatest
# integer that evenly divides both numbers. You may wish to use the
# `%` modulo operation.
#
# Difficulty: medium.

def greatest_common_factor(n1, n2)
  candidate_divisor = n1 < n2 ? n1 : n2
  # ^ if this line is confusing, google, 'Ruby ternary operator'.

  while candidate_divisor >= 1
    if n1 % candidate_divisor == 0 && n2 % candidate_divisor == 0
      return candidate_divisor
    end
    candidate_divisor -= 1
  end
end


# These are tests to check that your code is working. After writing
# your solution, they should all print true.

puts(
  'greatest_common_factor(3, 9) == 3: ' +
  (greatest_common_factor(3, 9) == 3).to_s
)
puts(
  'greatest_common_factor(16, 24) == 8: ' +
  (greatest_common_factor(16, 24) == 8).to_s
)
puts(
  'greatest_common_factor(3, 5) == 1: ' +
  (greatest_common_factor(3, 5) == 1).to_s
)
