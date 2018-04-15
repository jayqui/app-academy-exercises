# Write a method that takes in a number and returns a string, placing
# a single dash before and after each odd digit. There is one
# exception: don't start or end the string with a dash.
#
# You may wish to use the `%` modulo operation; you can see if a number
# is even if it has zero remainder when divided by two.
#
# Difficulty: medium.

# SOLUTION 1
# def dasherize_number(num):
#     result = ""
#     numstring = str(num)

#     for index, char in enumerate(numstring):
#         if int(char) % 2 == 0:
#             result += char
#         else:
#             if index == 0:
#                 result += f"{char}-"
#             else:
#                 previous_char = numstring[index - 1]
#                 previous_char_odd = int(previous_char) % 2 == 1

#                 if index == len(numstring) - 1:
#                     if previous_char_odd:
#                         result += char
#                     else:
#                         result += f"-{char}"
#                 else:
#                     if previous_char_odd:
#                         result += f"{char}-"
#                     else:
#                         result += f"-{char}-"
#     return result

# SOLUTION 2
import re
def dasherize_number(num):
    result = ""
    numstring = str(num)

    for index, char in enumerate(numstring):
        if int(char) % 2 == 0:
            result += char
        else:
            result += f"-{char}-"

    result = re.sub("--", "-", result)
    if result[0] == "-": result = result[1:]
    if result[-1] == "-": result = result[:-1]
    return result



# These are tests to check that your code is working. After writing
# your solution, they should all print True.

print(
  'dasherize_number(203) == "20-3": ' +
  str(dasherize_number(203) == '20-3')
)
print(
  'dasherize_number(303) == "3-0-3": ' +
  str(dasherize_number(303) == '3-0-3')
)
print(
  'dasherize_number(333) == "3-3-3": ' +
  str(dasherize_number(333) == '3-3-3')
)
print(
  'dasherize_number(3223) == "3-22-3": ' +
  str(dasherize_number(3223) == '3-22-3')
)


######## PSEUDO-CODE ########
# - even
#   - just concat the number
# - odd
#   - first in numstring: concat the number + "-"
#   - last in numstring:
#     - previous was odd:
#       concat the number
#     - previous was even:
#       concat the "-" + the number
#   - else:
#     - previous was odd:
#       concat the number + "-"
#     - previous was even:
#       concat "-" + number + "-"
