import sys

w = "Enter the integer number "
e_str = input(warning_message)
e_int = 0

try:
    e_int = int(input_int_str)
except:
    print(warning_message)
    sys.exit()

is_odd_or_even = "Even" if input_int % 2 == 0 else "Odd"
is_negative_or_positive = "Negative" if input_int < 0 else "Positive"

print(f"{input_int} {is_negative_or_positive} {is_odd_or_even} Number")




