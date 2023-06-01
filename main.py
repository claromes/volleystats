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

	process.crawl(HomeStatsSpider, fed_acronym=fed_acronym, match_id=match_id)
	process.crawl(GuestStatsSpider, fed_acronym=fed_acronym, match_id=match_id)
	process.start()
elif args['comp']:
    fed_acronym = args['fed']
    competition_id = args['comp']

    process.crawl(CompetitionMatchesSpider, fed_acronym=fed_acronym, competition_id=competition_id)
    process.start()
