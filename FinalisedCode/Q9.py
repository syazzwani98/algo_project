import re
import numpy as np
import matplotlib.pyplot as plt

p = open("positiveWord.txt","r")
n = open("negativeWord.txt","r")
pr = p.read().lower()
nr = n.read().lower()
TokensP = pr.split(", ")
TokensN = nr.split(", ")

def Analyze(text):
    positive = 0
    negative = 0
    textPos = tokenizer(text)
    for word in textPos:
        if word in TokensP:
            positive += 1
    for word in textPos:
        if word in TokensN:
            negative += 1
    if positive > negative:
        print("There are more positive words than negative words.So, the article is giving positive sentiment.\nTherefore, this country has positive political situation\n")
    elif negative > positive:
        print("There are more negative words than positive words.So, the article is giving negative sentiment.\nTherefore, this country has negative political situation\n")
    else:
        print("Article is giving neutral sentiment\n")

def tokenizer(Text):
    textTokens = re.findall(r'\b\w[\w-]*\b', Text.lower())
    return textTokens

print("Brazil\n")
fileA = open('Brazil.txt', 'r')
fileA = fileA.read()
Analyze(fileA)

print("China\n")
fileB = open('China.txt', 'r')
fileB = fileB.read()
Analyze(fileB)

print("India\n")
fileC = open('India.txt', 'r')
fileC = fileC.read()
Analyze(fileC)

print("London\n")
fileD = open('London.txt', 'r')
fileD = fileD.read()
Analyze(fileD)

print("Russia\n")
fileE = open('Rusia.txt', 'r')
fileE = fileE.read()
Analyze(fileE)

print("Spain\n")
fileF = open('Spain.txt', 'r')
fileF = fileF.read()
Analyze(fileF)

print("Thailand\n")
fileG = open('Thailand.txt', 'r')
fileG = fileG.read()
Analyze(fileG)

print("United State\n")
fileH = open('US.txt', 'r')
fileH = fileH.read()
Analyze(fileH)