# https://dmoj.ca/problem/wc17c3j3
password = input()
lowercase_count = 0
uppercase_count = 0
digit_count = 0

for char in password:
    if char.islower():
        lowercase_count = lowercase_count + 1
    elif char.isupper():
        uppercase_count = uppercase_count + 1
    elif char.isdigit():
        digit_count = digit_count + 1

if not (8 <= len(password) <= 12):
    is_valid_password = "Invalid"
elif lowercase_count >= 3 and uppercase_count >= 2 and digit_count >= 1:
    is_valid_password = "valid"
else:
    is_valid_password = "Invalid"

print(is_valid_password)