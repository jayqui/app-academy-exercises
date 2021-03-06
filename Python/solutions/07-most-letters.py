# Write a method that takes a string in and returns True if the letter
# "z" appears within three letters **after** an "a". You may assume
# that the string contains only lowercase letters.
#
# Difficulty: medium.

def nearby_az(string):
    for index, letter in enumerate(string):
        if letter == "a":
            # print("string[index + 1:index + 4]:", string[index + 1:index + 4])
            for other_letter in string[index + 1:index + 4]:
                if other_letter == "z": return True
    return False

# These are tests to check that your code is working. After writing
# your solution, they should all print True.

print('nearby_az("baz") == True: ' + str(nearby_az('baz') == True))
print('nearby_az("abz") == True: ' + str(nearby_az('abz') == True))
print('nearby_az("abcz") == True: ' + str(nearby_az('abcz') == True))
print('nearby_az("a") == False: ' + str(nearby_az('a') == False))
print('nearby_az("z") == False: ' + str(nearby_az('z') == False))
print('nearby_az("za") == False: ' + str(nearby_az('za') == False))
