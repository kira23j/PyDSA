def abbreviate_word(word):
    if len(word) > 10:
        return word[0] + str(len(word) - 2) + word[-1]
    else:
        return word

# Read the number of words
n = int(input())

# Process each word
for _ in range(n):
    word = input().strip()
    result = abbreviate_word(word)
    print(result)
