import os
import sys

fed_acronym = str(sys.argv[1])
competition_id = int(sys.argv[2])

os.system('scrapy crawl --nolog competition_matches -a fed_acronym={} -a competition_id={}'.format(fed_acronym, competition_id))