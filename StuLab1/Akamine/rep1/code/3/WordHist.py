f = open('dracula.txt')
data = f.read()

# counting
words = {}
for word in data.split():
    words[word] = words.get(word, 0) + 1

print("The number of words = %d" % (len(words)))

# sort by count
d = [(v, k) for k, v in words.items()]
#   上記は「リスト内包表記」と呼ばれるもので、リストを生成する式
d.sort()
d.reverse()
for count, word in d[:20]:
    print(count, word)
