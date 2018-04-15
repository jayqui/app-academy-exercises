# Write a method that takes an array of numbers. If a pair of numbers
# in the array sums to zero, return the positions of those two numbers.
# If no pair of numbers sums to zero, return `nil`.
#
# Difficulty: medium.

def two_sum(nums)
  nums.each_with_index do |x, ix|
    nums.each_with_index do |y, iy|
      if ix != iy
        if x + y == 0
          return [ix, iy]
        end
      end
    end
  end
  nil
end

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

puts(
  'two_sum([1, 3, 5, -3]) == [1, 3]: ' + (two_sum([1, 3, 5, -3]) == [1, 3]).to_s
)
puts(
  'two_sum([1, 3, 5]) == nil: ' + (two_sum([1, 3, 5]) == nil).to_s
)
puts(
  'two_sum([0]) == nil: ' + (two_sum([0]) == nil).to_s
)
puts(
  'two_sum([7,0,7,0,0]) == [1,3]: ' + (two_sum([7,0,7,0,0]) == [1,3]).to_s
)