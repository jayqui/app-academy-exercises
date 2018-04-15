# Write a method that takes a string and returns the number of vowels
# in the string. You may assume that all the letters are lower cased.
# You can treat "y" as a consonant.
#
# Difficulty: easy.

def count_vowels(string):
    vowels_count = 0
    for letter in string:
        if letter in ['a','e','i','o','u']:
            vowels_count += 1
    return vowels_count

# These are tests to check that your code is working. After writing
# your solution, they should all print True.

print('count_vowels("abcd") == 1: ' + str(count_vowels('abcd') == 1))
print('count_vowels("color") == 2: ' + str(count_vowels('color') == 2))
print('count_vowels("colour") == 3: ' + str(count_vowels('colour') == 3))
print('count_vowels("cecilia") == 4: ' + str(count_vowels('cecilia') == 4))
