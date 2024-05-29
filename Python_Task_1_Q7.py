# Finding Most frequent character in string

string = "Kazhindhini"

# Declaring an empty dictionary
freq_char = {}

# Iteration through string

for i in string:
    if i in freq_char:
# Adding the character in the dictionary and keeping a count of the frequent character
        freq_char[i] = freq_char[i]+1
    else:
        freq_char[i] = 1
# getting  maximum count and storing the value returned
result = max(freq_char, key=freq_char.get)

# Print the result
print("\n", string)
print("\nMost frequent character is: ", result)
