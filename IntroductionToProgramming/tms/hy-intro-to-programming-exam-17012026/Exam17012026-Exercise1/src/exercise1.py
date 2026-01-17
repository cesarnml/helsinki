# Write your solution to exercise 1 here
inputs: list[str] = []

while True:
    word = input("Type in a string: ")
    if word == "":
        break
    inputs.append(word)
max_length = 0
for item in inputs:
    if len(item) > max_length:
        max_length = len(item)
combine = "".join(inputs)
max_count = 0
max_char = ""
for char in combine:
    if combine.count(char) > max_count:
        max_count = combine.count(char)
        max_char = char
print(f"The total number of strings: {len(inputs)}")
print(f"The length of the longest string: {max_length}")
print(f"The most common character in strings: {max_char}")
