# Write a method that takes in a string of lowercase letters and
# spaces, producing a new string that capitalizes the first letter of
# each word.
#
# Difficulty: medium.

# # SOLUTION 1
# def capitalize_words(string):
#     result = ""
#     for index, char in enumerate(string):
#         if index == 0 or string[index - 1] == " ":
#             result += char.upper()
#         else:
#             result += char

#     return result

# # SOLUTION 2
# def capitalize_words(string):
#     return " ".join(map(lambda word: word.capitalize(), string.split()))

# # SOLUTION 3
# def capitalize_words(string):
#     words_list = string.split()
#     capitalized_words_list = map(lambda word: word.capitalize(), words_list)
#     return " ".join(capitalized_words_list)

# SOLUTION 4
def capitalize_words(string):
    return " ".join([word.capitalize() for word in string.split()])

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
