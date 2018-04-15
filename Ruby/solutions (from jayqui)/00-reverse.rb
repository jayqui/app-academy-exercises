# Write a method that will take a string as input, and return a new
# string with the same letters in reverse order.
#
# Don't use String's reverse method; that would be too simple.
#
# Difficulty: easy.

def reverse(string)
  result = ""

  array = string.split('')
  array.reverse_each do |letter|
    result += letter
  end

  result
end

#### another way:
# def reverse(string)
#   result = ""
#   (0..string.length - 1).reverse_each do |idx|
#     result.concat(string[idx])
#   end
#   result
# end

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

puts(
  'reverse("abc") == "cba": ' + (reverse("abc") == "cba").to_s
)
puts(
  'reverse("a") == "a": ' + (reverse("a") == "a").to_s
)
puts(
  'reverse("") == "": ' + (reverse("") == "").to_s
)
