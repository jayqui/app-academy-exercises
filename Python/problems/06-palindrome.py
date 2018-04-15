# Write a method that takes a string and returns True if it is a
# palindrome. A palindrome is a string that is the same whether written
# backward or forward. Assume that there are no spaces; only lowercase
# letters will be given.
#
# Difficulty: easy.

# ITERATIVE SOLUTION
# import math
# def is_palindrome(string):
#     middle_index = math.ceil(len(string)) - 1

#     index = 0
#     while index < middle_index:
#         if string[index] != string[-1 * (index + 1)]: return False
#         index += 1
#     return True

# RECURSIVE SOLUTION
def is_palindrome(string):

# These are tests to check that your code is working. After writing
# your solution, they should all print True.

print('palindrome?("abc") == False: ' + str(is_palindrome('abc') == False))
print('is_palindrome("abcba") == True: ' + str(is_palindrome('abcba') == True))
print('is_palindrome("z") == True: ' + str(is_palindrome('z') == True))
