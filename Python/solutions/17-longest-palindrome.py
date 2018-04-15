# Write a method that takes in a string of lowercase letters (no
# uppercase letters, no repeats). Consider the *substrings* of the
# string: consecutive sequences of letters contained inside the string.
# Find the longest such string of letters that is a palindrome.
#
# Note that the entire string may itself be a palindrome.
#
# Difficulty: hard.

def is_palindrome(string):
    if len(string) < 2: return True
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False

def all_substrings(string):
    result = set([string, ""])
    for n in range(1, len(string)):
        for index, _ in enumerate(string):
            result.add(string[index:(index + n)])
    return sorted(result, key=len, reverse=True)

def longest_palindrome(string):
    longest_palindrome_length = 0
    for substring in all_substrings(string):
        if is_palindrome(substring):
            return substring

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
