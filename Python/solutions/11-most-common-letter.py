# Write a method that takes in a string. Your method should return the
# most common letter in the array, and a count of how many times it
# appears.
#
# Difficulty: medium.

def most_common_letter(string):
    tally = {}
    for letter in string:
        if letter not in tally.keys(): tally[letter] = 0
        tally[letter] += 1
    most_common = max(tally, key=tally.get)
    return [most_common, tally[most_common]]

# These are tests to check that your code is working. After writing
# your solution, they should all print True.

print(
  'most_common_letter("abca") == ["a", 2]: ' +
  str(most_common_letter('abca') == ['a', 2])
)
print(
  'most_common_letter("abbab") == ["b", 3]: ' +
  str(most_common_letter('abbab') == ['b', 3])
)
