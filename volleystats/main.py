import argparse
import os
import sys
import logging
import csv

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
		description='Command-line tool to scrape volleyball statistics from Data Project Web Competition websites',
		epilog='Found a bug? https://github.com/claromes/volleystats/issues'
	)

	parser.add_argument(
		'-f', '--fed',
		dest='fed',
		required=True,
		help='Federation acronym: <Fed_Acronym>-web.dataproject.com'
	)

	group = parser.add_mutually_exclusive_group(required=True)

	group.add_argument(
		'-m', '--match',
		dest='match',
		type=int,
		help='ID of the match: <Fed_Acronym>-web.dataproject.com/MatchStatistics?mID=<Match_ID>'
	)

	group.add_argument(
		'-c', '--comp',
		dest='comp',
		type=int,
		help='ID of the competition: <Fed_Acronym>-web.dataproject.com/CompetitionMatches?ID=<Competition_ID>'
	)

	group.add_argument(
		'-b', '--batch',
		dest='batch',
		type=str,
		help='CSV batch file (output of the Competition Matches): data/<Fed_Acronym>-<Competition_ID>-<start_year>-<end_year>-competition_matches.csv'
	)

	parser.add_argument(
		'-l', '--log',
		dest='log',
		action='store_true',
		required=False,
		help='Output log'
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
	elif args['batch']:
		fed_acronym = args['fed']
		csv_file_path = args['batch']

		match_ids = []

		with open(csv_file_path, 'r') as f:
			csv_reader = csv.DictReader(f)
			for row in csv_reader:
				match_ids.append(row['Match ID'])

		for match_id in match_ids:
			match_id_started_msg = f'\nvolleystats: starting {match_id}...'
			print(match_id_started_msg)

			process.crawl(GuestStatsSpider, fed_acronym=fed_acronym, match_id=match_id)
			process.crawl(HomeStatsSpider, fed_acronym=fed_acronym, match_id=match_id)

		process.start()
		print(finished_msg)

if __name__ == '__main__':
    main()
