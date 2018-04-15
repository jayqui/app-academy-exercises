# Write a method that takes in a string and returns the number of
# letters that appear more than once in the string. You may assume
# the string contains only lowercase letters. Count the number of
# letters that repeat, not the number of times they repeat in the
# string.
#
# Difficulty: hard.

def num_repeats(string)
  tallies = {}

  (0..string.length - 1).each do |idx|
    letter = string[idx]
    tallies[letter] ||= 0
    tallies[letter] += 1
  end

  count_tallies_greater_than_two(tallies)
end

def count_tallies_greater_than_two(tally_list)
  result = 0

  tally_list.each do |key, value|
    if value >= 2
      result += 1
    end
  end

  result

  ## ^ The above is roughly equivalent to:
  # tally_list.select {|key, value| key if value >= 2}.count
end

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

puts('num_repeats("abdbc") == 1: ' + (num_repeats('abdbc') == 1).to_s)
# one character is repeated
puts('num_repeats("aaa") == 1: ' + (num_repeats('aaa') == 1).to_s)
puts('num_repeats("abab") == 2: ' + (num_repeats('abab') == 2).to_s)
puts('num_repeats("cadac") == 2: ' + (num_repeats('cadac') == 2).to_s)
puts('num_repeats("abcde") == 0: ' + (num_repeats('abcde') == 0).to_s)
