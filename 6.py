str=" I love Logical Python. Python is one of the most used Programming Language"

unique_letters=set(str)

letters_count={}

for letter in unique_letters:
    letters_count[letter]=str.count(letter)

print(letters_count)