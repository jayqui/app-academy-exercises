# Write a method that takes in a string of lowercase letters and
# spaces, producing a new string that capitalizes the first letter of
# each word.
#
# Difficulty: medium.

def capitalize_words(string):

# These are tests to check that your code is working. After writing
# your solution, they should all print True.

print(
  'capitalize_words("this is a sentence") == "This Is A Sentence": ' +
  str(capitalize_words("this is a sentence") == "This Is A Sentence")
)
print(
  'capitalize_words("mike bloomfield") == "Mike Bloomfield": ' +
  str(capitalize_words("mike bloomfield") == "Mike Bloomfield")
)
