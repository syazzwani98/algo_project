fname = "China.txt"
fname1 ="Brazil.txt"
fname2 = "Spain.txt"
fname3 = "Rusia.txt"
fname4 = "Thailand.txt"
fname5 = "London.txt"
fname6 = "India.txt"
fname7 = "US.txt"

num_words = 0
num_words1 = 0
num_words2 = 0
num_words3 = 0
num_words4 = 0
num_words5 = 0
num_words6 = 0
num_words7 = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
with open(fname1, 'r') as f:
    for line in f:
        words = line.split()
        num_words1 += len(words)
with open(fname2, 'r') as f:
    for line in f:
        words = line.split()
        num_words2 += len(words)
with open(fname3, 'r') as f:
    for line in f:
        words = line.split()
        num_words3 += len(words)
with open(fname4, 'r') as f:
    for line in f:
        words = line.split()
        num_words4 += len(words)
with open(fname5, 'r') as f:
    for line in f:
        words = line.split()
        num_words5 += len(words)
with open(fname6, 'r') as f:
    for line in f:
        words = line.split()
        num_words6 += len(words)
with open(fname7, 'r') as f:
    for line in f:
        words = line.split()
        num_words7 += len(words)

Afname = "China-output.txt"
Afname1 ="Brazil-output.txt"
Afname2 = "Spain-output.txt"
Afname3 = "Rusia-output.txt"
Afname4 = "Thailand-output.txt"
Afname5 = "London-output.txt"
Afname6 = "India-output.txt"
Afname7 = "US-output.txt"

num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
num7 = 0
num8 = 0

with open(Afname, 'r') as f:
    for line in f:
        words = line.split()
        num1 += len(words)
with open(Afname1, 'r') as f:
    for line in f:
        words = line.split()
        num2 += len(words)
with open(Afname2, 'r') as f:
    for line in f:
        words = line.split()
        num3 += len(words)
with open(Afname3, 'r') as f:
    for line in f:
        words = line.split()
        num4 += len(words)
with open(Afname4, 'r') as f:
    for line in f:
        words = line.split()
        num5 += len(words)
with open(Afname5, 'r') as f:
    for line in f:
        words = line.split()
        num6 += len(words)
with open(Afname6, 'r') as f:
    for line in f:
        words = line.split()
        num7 += len(words)
with open(Afname7, 'r') as f:
    for line in f:
        words = line.split()
        num8 += len(words)

print("\nWORD COUNT FOR ARTICLE IN EACH COUNTRY BEFORE FILTER")
print("|China:", num_words,"|  Brazil:", num_words1, "|Spain :", num_words2, "|Rusia:",num_words3, "|Thailand:", num_words4, "|London:", num_words5, "|India: ", num_words6, "|US: ", num_words7 ,"|")

print("\nWORD COUNT FOR ARTICLE IN EACH COUNTRY AFTER FILTER")
print("|China:", num1 ,"|  Brazil:", num2 , " |Spain :", num3, " |Rusia:",num4 , " |Thailand:", num5 , " |London:", num6 , " |India: ", num7, " |US: ", num8 ,"|")
