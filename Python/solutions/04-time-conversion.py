# Write a method that will take in a number of minutes, and returns a
# string that formats the number into `hours:minutes`.
#
# Difficulty: easy.

def time_conversion(minutes):
    hours = 0

    while minutes >= 60:
        hours += 1
        minutes -= 60

    result_minutes = "0" + str(minutes) if minutes < 10 else str(minutes)

    return f"{hours}:{result_minutes}"

# These are tests to check that your code is working. After writing
# your solution, they should all print True.

print('time_conversion(15) == "0:15": ' + str(time_conversion(15) == '0:15'))
print('time_conversion(150) == "2:30": ' + str(time_conversion(150) == '2:30'))
print('time_conversion(360) == "6:00": ' + str(time_conversion(360) == '6:00'))
