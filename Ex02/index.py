# file = input('Enter a file: ')
handle = open('C:\\Users\\Samuel\\Documents\\Estudos\\Python-Exercises\\Ex02\\text.txt', 'r')

counts = dict()
for lines in handle:
    words = lines.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1