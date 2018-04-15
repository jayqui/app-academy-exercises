# Write a method that takes in an integer `num` and returns the sum of
# all integers between zero and num, up to and including `num`.
#
# Difficulty: easy.

### A pretty transparent solution
# def sum_nums(num)
#   sum = 0
#   (0..num).each {|n| sum += n}
#   sum
# end

### The Ruby-tacular way. Under the hood it does exactly the same as the above.
def sum_nums(num)
  (0..num).inject(:+)
end

  ### Line 15 is shorthand for line 20:
  # def sum_nums(num)
  #   (0..num).inject(0) {|accum, n| accum + n}
  # end

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

puts('sum_nums(1) == 1: ' + (sum_nums(1) == 1).to_s)
puts('sum_nums(2) == 3: ' + (sum_nums(2) == 3).to_s)
puts('sum_nums(3) == 6: ' + (sum_nums(3) == 6).to_s)
puts('sum_nums(4) == 10: ' + (sum_nums(4) == 10).to_s)
puts('sum_nums(5) == 15: ' + (sum_nums(5) == 15).to_s)
