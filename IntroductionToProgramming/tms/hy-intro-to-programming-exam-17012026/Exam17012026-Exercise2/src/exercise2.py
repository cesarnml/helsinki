# Write your solution to exercise 2 here
def find_allowed(words: list[str], minimum: int):
    target = "aeiouy"
    matches: list[str] = []
    for word in words:
        count = 0
        for char in target:
            count += word.count(char)
        if count >= minimum:
            matches.append(word)
    return matches
