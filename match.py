import os
import sys

fed_acronym = str(sys.argv[1])
match_id = int(sys.argv[2])

os.system('scrapy crawl --nolog home_stats -a fed_acronym={} -a match_id={}'.format(fed_acronym, match_id))
os.system('scrapy crawl --nolog guest_stats -a fed_acronym={} -a match_id={}'.format(fed_acronym, match_id))