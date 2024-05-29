# Returns Unique Characters from string

string = "Kazhindhi"

uni_char = ""
for i in range(len(string)):
    if string[i] not in uni_char:
        uni_char = uni_char + string[i]
print("\n Unique Characters are:", uni_char)
print("\n Length of Unique Character is:", len(uni_char))
