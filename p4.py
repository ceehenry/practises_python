# Calculate the number of words in a file

words = 0
blank_lines = 0
sentences = 0
f = file('p4_file.txt')

for line in f:
    if line.startswith("\n"):
        blank_lines += 1
    sentences += line.count('.')+line.count('?')+line.count('!')
    temp_words = line.split(" ")
    words += len(temp_words)
print 'the total number of words is '+str(words)
print 'the total number of sentences is '+str(sentences)
print 'the total number of blanklines is '+str(blank_lines)

f.close()



