# Python program to calculate total number of vowels and counting each individual vowels

string = "Guvi Geeks Network Private Limited"

# Initialize count variables
a_num = 0
e_num = 0
i_num = 0
o_num = 0
u_num = 0
# Count each vowel in the string
for i in string:
    if i == 'a' or i == 'A':
        a_num += 1
    elif i == 'e' or i == 'E':
        e_num += 1
    elif i == 'i' or i == 'I':
        i_num += 1
    elif i == 'o' or i == 'O':
        o_num += 1
    elif i == 'u' or i == 'U':
        u_num += 1
# Calculate the total count of vowels
total_vowels = a_num + e_num + i_num + o_num + u_num

# Printing each vowels count and total count
print("Total count of 'A': {}".format(a_num))
print("Total count of 'E': {}".format(e_num))
print("Total count of 'I': {}".format(i_num))
print("Total count of 'O': {}".format(o_num))
print("Total count of 'U': {}".format(u_num))
print("Total count of vowels: {}".format(total_vowels))
