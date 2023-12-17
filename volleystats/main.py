import argparse
import os
import sys
import logging

from scrapy.crawler import CrawlerProcess
from volleystats.spiders.match import HomeStatsSpider, GuestStatsSpider
from volleystats.spiders.competition import CompetitionMatchesSpider
from volleystats.version import __version__

version = __version__
welcome_msg = f'''
                    .
                    |`.
                    |  `.
                    |-_  `.
                    |  -_  `._
____________________|____-_ _|_______________,
',                         -_|                ',
  ',                         |                  ',
    ',                       |                    ',
      ',_____________________|______________________', v{version}
'''

started_msg = '\nvolleystats: started'
finished_msg = 'volleystats: finished'

def main():
	print(welcome_msg)

	parser = argparse.ArgumentParser(
		prog='volleystats',
		description='CLI tool to get volleyball statistics from the Data Project Web Competition websites (WCM)',
		epilog='Found a bug? https://github.com/claromes/volleystats/issues'
	)

	parser.add_argument(
		'-f', '--fed',
		dest='fed',
		required=True,
		help='Federation Acronym'
	)

	group = parser.add_mutually_exclusive_group(required=True)

	group.add_argument(
		'-m', '--match',
		dest='match',
		type=int,
		help='Stats of a single match'
	)

	group.add_argument(
		'-c', '--comp',
		dest='comp',
		type=int,
		help='List of matches in a competition'
	)

	parser.add_argument(
		'-l', '--log',
		dest='log',
		action='store_true',
		required=False,
		help='Set log'
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

	print(started_msg)

	logging.disable(logging.CRITICAL)

	if args['log']:
		logging.disable(logging.NOTSET)

	if args['match']:
		fed_acronym = args['fed']
		match_id = args['match']

		process.crawl(GuestStatsSpider, fed_acronym=fed_acronym, match_id=match_id)
		process.crawl(HomeStatsSpider, fed_acronym=fed_acronym, match_id=match_id)
		process.start()

		print(finished_msg)
	elif args['comp']:
		fed_acronym = args['fed']
		competition_id = args['comp']

		process.crawl(CompetitionMatchesSpider, fed_acronym=fed_acronym, competition_id=competition_id)
		process.start()

		print(finished_msg)

if __name__ == '__main__':
    main()
