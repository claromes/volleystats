import argparse
import os
import sys
from scrapy.crawler import CrawlerProcess

from matchscraper.spiders.match import HomeStatsSpider, GuestStatsSpider
from matchscraper.spiders.competition import CompetitionMatchesSpider
from matchscraper.version import __version__

version = __version__
welcome_msg = '''
                    .
                    |`.
                    |  `.
                    |-_  `.
                    |  -_  `._
____________________|____-_ _|_______________,
',                         -_|                ',
  ',                         |                  ',
    ',                       |                    ',
      ',_____________________|______________________',
	Matchscraper v{}
'''.format(version)

# https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
started_msg = '\x1b[6;30;42m' + '\n Matchscraper: started! ' + '\x1b[0m\n'
finished_msg = '\x1b[6;30;42m' + '\n Matchscraper: finished! ' + '\x1b[0m\n'

def main():
	print(welcome_msg)

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

	print(started_msg)

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
