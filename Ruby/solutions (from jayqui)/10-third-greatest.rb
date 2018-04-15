# Write a method that takes an array of numbers in. Your method should
# return the third greatest number in the array. You may assume that
# the array has at least three numbers in it.
#
# Difficulty: medium.

### The stunningly obvious solution when you think about it
def third_greatest(nums)
  nums.sort[-3]
end

### my initial crappy but working solution
# def third_greatest(nums)
#   three_greatest = []
#   nums.each do |num|
#     if three_greatest.empty?
#       three_greatest.push(num)
#     else
#       three_greatest.each_with_index do |list_item, idx|
#         if num > list_item
#           three_greatest.insert(idx, num)
#           three_greatest.pop if three_greatest.length > 3
#           break
#         elsif num <= list_item && three_greatest.length < 3
#           three_greatest.push(num)
#         end
#       end
#     end
#   end

#   # p "three_greatest: #{three_greatest}"
#   three_greatest[2]
# end

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

puts(
  'third_greatest([5, 3, 7]) == 3: ' +
  (third_greatest([5, 3, 7]) == 3).to_s
)
puts(
  'third_greatest([5, 3, 7, 4]) == 4: ' +
  (third_greatest([5, 3, 7, 4]) == 4).to_s
)
puts(
  'third_greatest([2, 3, 7, 4]) == 3: ' +
  (third_greatest([2, 3, 7, 4]) == 3).to_s
)