# For example, let's say we need to create a list of integers which specify the length of each word in a certain sentence, but only if the word is not the word "the".

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print(type(words))
print(words)

word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))
print(words)
print(word_lengths)

# List Comprehension version below
print("="*10)
word_lengths_compre = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths_compre)

# iseng coba
print("="*10)
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# if want to convert the result into integer, just int(num)
newlist = [num for num in numbers if num > 0]
print(newlist)
