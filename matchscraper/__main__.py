import argparse
import os
import sys
from scrapy.crawler import CrawlerProcess

from matchscraper.spiders.match import HomeStatsSpider, GuestStatsSpider
from matchscraper.spiders.competition import CompetitionMatchesSpider

parser = argparse.ArgumentParser()

parser.add_argument(
	'--fed',
	type=str,

	help='Federation Acronym'
)

parser.add_argument(
	'--match',
	type=int,

	help='Stats of a single match'
)

parser.add_argument(
	'--comp',
	type=int,

	help='List of matches in a competition'
)

args = vars(parser.parse_args())

process = CrawlerProcess(settings={
	'FEEDS': {
		'data/%(name)s.csv': {
		'format': 'csv',
		'overwrite': True
		},
	},
})

if args['match']:
	fed_acronym = args['fed']
	match_id = args['match']

    # https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
	print('\x1b[6;30;42m' + '\nMatchscraper: started!' + '\x1b[0m\n')

	process.crawl(GuestStatsSpider, fed_acronym=fed_acronym, match_id=match_id)
	process.crawl(HomeStatsSpider, fed_acronym=fed_acronym, match_id=match_id)
	process.start()

	print('\x1b[6;30;42m' + '\nMatchscraper: finished!' + '\x1b[0m\n')
elif args['comp']:
    fed_acronym = args['fed']
    competition_id = args['comp']

    print('\x1b[6;30;42m' + '\nMatchscraper: started!' + '\x1b[0m\n')

    process.crawl(CompetitionMatchesSpider, fed_acronym=fed_acronym, competition_id=competition_id)
    process.start()

    print('\x1b[6;30;42m' + '\nMatchscraper: finished!' + '\x1b[0m\n')
