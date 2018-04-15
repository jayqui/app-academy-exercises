# Write a method that takes in a string of lowercase letters (no
# uppercase letters, no repeats). Consider the *substrings* of the
# string: consecutive sequences of letters contained inside the string.
# Find the longest such string of letters that is a palindrome.
#
# Note that the entire string may itself be a palindrome.
#
# You may want to use Array's `slice(start_index, length)` method,
# which returns a substring of length `length` starting at index
# `start_index`:
#
#     "abcd".slice(1, 2) == "bc"
#     "abcd".slice(1, 3) == "bcd"
#     "abcd".slice(2, 1) == "c"
#     "abcd".slice(2, 2) == "cd"
#
# Difficulty: hard.

def palindrome?(string)
  i = 0
  while i < string.length
    if string[i] != string[(string.length - 1) - i]
      return false
    end

    i += 1
  end

  return true
end

def longest_palindrome(string)
  array = string.split('')
  length_to_check = string.length
  while length_to_check > 0
    array.each_index do |idx|
      current_substring = array.slice(idx, length_to_check).join('')
      break if idx + length_to_check > array.length
      # ^ this break statement prevents looking over edge of array
      return current_substring if palindrome?(current_substring)
    end
    length_to_check -= 1
  end
  nil
end

### Here's the vesion that includes the p statements I used to debug
# def longest_palindrome(string)
#   array = string.split('')
#   length_to_check = string.length
#   while length_to_check > 0
#     p "length_to_check: #{length_to_check}"
#     array.each_index do |idx|
#       current_substring = array.slice(idx, length_to_check).join('')
#       p "idx + length_to_check: #{idx + length_to_check}"
#       p "array.length: #{array.length}"
#       break if idx + length_to_check > array.length
#       p "current_substring: #{current_substring}"
#       return current_substring if palindrome?(current_substring)
#     end
#     length_to_check -= 1
#   end
#   nil
# end

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

puts(
  'longest_palindrome("abcbd") == "bcb": ' +
  (longest_palindrome('abcbd') == 'bcb').to_s
)
puts(
  'longest_palindrome("abba") == "abba": ' +
  (longest_palindrome('abba') == 'abba').to_s
)
puts(
  'longest_palindrome("abcbdeffe") == "effe": ' +
  (longest_palindrome('abcbdeffe') == 'effe').to_s
)
