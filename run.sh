#!/bin/bash

mkdir -p tweet_output
TARGET_FILE="tweets.txt"
python src/words_tweeted.py $TARGET_FILE
python src/median_unique.py $TARGET_FILE
