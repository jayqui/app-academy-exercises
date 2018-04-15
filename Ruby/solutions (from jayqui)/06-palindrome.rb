# Write a method that takes a string and returns true if it is a
# palindrome. A palindrome is a string that is the same whether written
# backward or forward. Assume that there are no spaces; only lowercase
# letters will be given.
#
# Difficulty: easy.

### lazy solution
def palindrome?(string)
  string == string.reverse
end

### recursive solution
# def palindrome?(string)
#   return true if string.length == 0 || string.length == 1
#   return false if string[0] != string[-1]
#   palindrome?(string[1..-2])
# end

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

puts('palindrome?("abc") == false: ' + (palindrome?('abc') == false).to_s)
puts('palindrome?("abcba") == true: ' + (palindrome?('abcba') == true).to_s)
puts('palindrome?("z") == true: ' + (palindrome?('z') == true).to_s)
