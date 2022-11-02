#!/bin/bash

d=`date +%Y-%m`

scrapy crawl home_superliga -a match=$1 -o data/$d-home-superliga-$1.csv &&
scrapy crawl guest_superliga -a match=$1 -o data/$d-guest-superliga-$1.csv

exec bash