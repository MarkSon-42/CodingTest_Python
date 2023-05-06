str = input()
tmp = ''
for c in str:
    if c.isupper() == True:
        c = c.lower()
        tmp += c

    else:
        c = c.upper()
        tmp += c

print(tmp)


# Get user input
input_str = input()

# Initialize an empty string for the result
result = ''

# Loop through each character in the input string
for char in input_str:
    # If the character is uppercase, convert it to lowercase, and vice versa
    result += char.lower() if char.isupper() else char.upper()

# Print the resulting string
print(result)