#!/bin/bash

FILE_NAME_HOME="home-superliga-$1.csv"
FILE_NAME_GUEST="guest-superliga-$1.csv"

if [ $2 ]
then
    FILE_NAME_HOME="$2-home-superliga-$1.csv"
    FILE_NAME_GUEST="$2-guest-superliga-$1.csv"
fi

scrapy crawl home_superliga -a match=$1 -o data/$FILE_NAME_HOME &&
scrapy crawl guest_superliga -a match=$1 -o data/$FILE_NAME_GUEST

exec bash