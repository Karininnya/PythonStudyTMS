with open('hw9.txt') as inf, open('hw9-2.txt', 'w') as ouf:
    maxc = 0
    s = inf.read().lower().strip().split()
    s.sort()
    for word in s:
        counter = s.count(word)
        if counter > maxc:
            maxc = counter
            result_word = word
    ouf.write(result_word + ' ' + str(maxc))


with open("stop_words.txt", encoding="utf-8") as file, open('text.txt') as infile:
    text = infile.read()
    for f in file.read().strip("\n").split():
        pos = text.lower().find(f)
        while pos > -1:
            text = text[:pos] + "*" * len(f) + text[pos+len(f):]
            pos = text.lower().find(f)
print(text)