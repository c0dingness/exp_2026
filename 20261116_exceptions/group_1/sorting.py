words = ['s','z', 'dog', 'zebra', 'bee', 'wolf', 'aaaaaaaaaa']


print(words)
words.sort()
print(words)
words.sort(key=lambda x: len(x))
print(words)

