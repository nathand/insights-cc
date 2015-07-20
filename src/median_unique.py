import os
from sets import Set
import sys
tweetInput = "tweets.txt"
if (len(sys.argv) == 2):
    tweetInput = str(sys.argv[1])
baseDir = os.getcwd()
f = open(baseDir + '/tweet_input/' + tweetInput, 'r')
output = open(baseDir + '/tweet_output/ft2.txt', 'w')
wordCountList = [];
for line in f:
    setWordCount = len(Set(line.split()))#set of unique words for current tweet
    wordCountList.append(setWordCount)#grow the dataset
    median = sum(wordCountList) / float(len(wordCountList))#calculate new median
    output.write(str(round(median, 1)) + '\n')#write new median to file
