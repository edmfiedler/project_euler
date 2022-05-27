"""
The nth term of the sequence of triangle numbers is given by, tn = 0.5n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position
 and adding these values we form a word value. For example,
  the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then
   we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'),
 a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

# Pre-processing data into workable framework
with open('txt_files/p042_words.txt') as f:
    lines = f.readlines()
    lines = lines[0]

sp = lines.split(",")
words = []
for word in sp:
    words.append(word[1:-1])

# Reference for letters to get score
ref = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Collect scores of each word
scores = []
for word in words:
    score = 0
    for let in word:
        score += ref.index(let)
    scores.append(score)

# Obtain the highest required triangle number
maxscore = max(scores)
triangs = [1]
n = 2
while triangs[-1] < maxscore:
    triangs.append(int(0.5*n*(n+1)))
    n += 1

# Count how many triangle numbers exist in scores
nwords = 0
for triang in triangs:
    nwords += scores.count(triang)

print(nwords)