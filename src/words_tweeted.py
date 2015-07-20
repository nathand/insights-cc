import os
from collections import defaultdict
import sys
tweetInput = "tweets.txt"
if (len(sys.argv) == 2):
    tweetInput = str(sys.argv[1])
baseDir = os.getcwd()
f = open(baseDir + '/tweet_input/' + tweetInput, 'r')
output = open(baseDir + '/tweet_output/ft1.txt', 'w')
longWordList = []
wordFrequency = defaultdict(int)
for line in f:
    wordList = line.split()
    for word in wordList:
        wordFrequency[word] += 1
orderedWords = sorted(wordFrequency)
for key in orderedWords:
    output.write("{:<30} {}\n".format(key, str(wordFrequency[key])))
