# Write a method that takes in a string and an array of indices in the
# string. Produce a new string, which contains letters from the input
# string in the order specified by the indices of the array of indices.
#
# Difficulty: medium.

def scramble_string(string, positions)
  result = []
  positions.each_with_index do |position, idx|
    result[idx] = string[position]
  end
  result.join('')
end

# ### Here's a version with p statements that I used for debugging.
# def scramble_string(string, positions)
#   result = []
#   positions.each_with_index do |position, idx|
#     p "position: #{position}"
#     result[idx] = string[position]
#     p "result (inside): #{result}"
#   end
#   p "result: #{result}"
#   result.join('')
# end



# These are tests to check that your code is working. After writing
# your solution, they should all print true.

puts(
  'scramble_string("abcd", [3, 1, 2, 0]) == "dbca": ' +
  (scramble_string("abcd", [3, 1, 2, 0]) == "dbca").to_s
)
puts(
  'scramble_string("markov", [5, 3, 1, 4, 2, 0]) == "vkaorm"): ' +
  (scramble_string("markov", [5, 3, 1, 4, 2, 0]) == "vkaorm").to_s
)
