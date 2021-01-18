import re
import numpy as np
import matplotlib.pyplot as plt

p = open("positiveWord.txt","r")
n = open("negativeWord.txt","r")
pr = p.read().lower()
nr = n.read().lower()
TokensP = pr.split(", ")
TokensN = nr.split(", ")

def Sentiment(text):
    positive = 0
    negative = 0
    textPos = tokenizer(text)
    for word in textPos:
        if word in TokensP:
            positive += 1
    for word in textPos:
        if word in TokensN:
            negative += 1
    print("Positive word = {}".format(positive))
    print("Negative word = {}\n".format(negative))

def tokenizer(Text):
    textTokens = re.findall(r'\b\w[\w-]*\b', Text.lower())
    return textTokens

print("Brazil\n")
file1 = open('Brazil.txt', 'r')
file1 = file1.read()
Sentiment(file1)

print("China\n")
file2 = open('China.txt', 'r')
file2 = file2.read()
Sentiment(file2)

print("India\n")
file3 = open('India.txt', 'r')
file3 = file3.read()
Sentiment(file3)

print("London\n")
file4 = open('London.txt', 'r')
file4 = file4.read()
Sentiment(file4)

print("Russia\n")
file5 = open('Rusia.txt', 'r')
file5 = file5.read()
Sentiment(file5)

print("Spain\n")
file6 = open('Spain.txt', 'r')
file6 = file6.read()
Sentiment(file6)

print("Thailand\n")
file7 = open('Thailand.txt', 'r')
file7 = file7.read()
Sentiment(file7)

print("United State\n")
file8 = open('US.txt', 'r')
file8 = file8.read()
Sentiment(file8)


