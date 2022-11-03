#!/bin/bash

FILE_NAME_HOME="data/home-superliga-$1.csv"
FILE_NAME_GUEST="data/guest-superliga-$1.csv"

if test $2
then
FILE_NAME_HOME="data/$2-home-superliga-$1.csv"
FILE_NAME_GUEST="data/$2-guest-superliga-$1.csv"
fi

if test $3
then
FILE_NAME_HOME="data/round-$3/$2-home-superliga-$1.csv"
FILE_NAME_GUEST="data/round-$3/$2-guest-superliga-$1.csv"
fi

scrapy crawl home_superliga -a match=$1 -o $FILE_NAME_HOME &&
scrapy crawl guest_superliga -a match=$1 -o $FILE_NAME_GUEST

exec bash