# counting vowels of the words

word = input("Your word: ")

vowels = ['a', 'e', 'i', 'o', 'u']

vowel_count = 0

for char in word:
    if char in vowels:
        vowel_count += 1

print(vowel_count)
