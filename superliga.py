import os
import sys

match_id = int(sys.argv[1])

os.system('scrapy crawl home_superliga -a match_id={}'.format(match_id))
os.system('scrapy crawl guest_superliga -a match_id={}'.format(match_id))

print('Done!')