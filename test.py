'''fw = open('b.txt','w')
fw.write("Hello\n")
fw.write("Friend\n")
fw.close()
fr = open('b.txt','r')
text = fr.readlines()
print(text)
fr.close()

print(len(text.split(' ')))'''
fname = 'b.txt'
num_lines = 0
num_words = 0
num_chars = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()

        num_lines += 1
        num_words += len(words)
        num_chars += len(line)

print(num_lines)
print(num_words)
print(num_chars)


