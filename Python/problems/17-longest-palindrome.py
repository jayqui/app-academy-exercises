# Write a method that takes in a string of lowercase letters (no
# uppercase letters, no repeats). Consider the *substrings* of the
# string: consecutive sequences of letters contained inside the string.
# Find the longest such string of letters that is a palindrome.
#
# Note that the entire string may itself be a palindrome.
#
# Difficulty: hard.

def longest_palindrome(string):

# These are tests to check that your code is working. After writing
# your solution, they should all print True.

# print(all_substrings('abc'))

print(
  'longest_palindrome("abcbd") == "bcb": ' +
  str(longest_palindrome('abcbd') == 'bcb')
)
print(
  'longest_palindrome("abba") == "abba": ' +
  str(longest_palindrome('abba') == 'abba')
)
print(
  'longest_palindrome("abcbdeffe") == "effe": ' +
  str(longest_palindrome('abcbdeffe') == 'effe')
)
