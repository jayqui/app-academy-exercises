# Write a method that takes an integer `n` in; it should return
# n*(n-1)*(n-2)*...*2*1. Assume n >= 0.
#
# As a special case, `factorial(0) == 1`.
#
# Difficulty: easy.

# # An iterative solution.
# def factorial(n)
#   result = 1
#   current = 2
#   while current <= n
#     result *= current
#     current += 1
#   end
#   result
# end

# A recursive solution. (Maybe the most famous example of recursion.)
def factorial(n)
  raise "Factorial only works on non-negative integers" if n < 0
  return 1 if n == 0 || n == 1
  n * factorial(n - 1)
end

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

puts('factorial(0) == 1: ' + (factorial(0) == 1).to_s)
puts('factorial(1) == 1: ' + (factorial(1) == 1).to_s)
puts('factorial(2) == 2: ' + (factorial(2) == 2).to_s)
puts('factorial(3) == 6: ' + (factorial(3) == 6).to_s)
puts('factorial(4) == 24: ' + (factorial(4) == 24).to_s)
