# Use the modulo operator to confirm which of the values
# shown below are divisible by seven.

numbers = [42, 137, 455, 1997]

divisible_by_seven = [number for number in numbers if number % 7 == 0]

print("The following numbers are divisible by seven:", divisible_by_seven)