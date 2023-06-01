import scrapy
import os
import re
import sys

class CompetitionMatchesSpider(scrapy.Spider):
    name = 'competition_matches'

    def __init__(self, fed_acronym='', competition_id='', **kwargs):
        self.start_urls = [f'https://{fed_acronym}-web.dataproject.com/CompetitionMatches.aspx?ID={competition_id}']
        self.competition_id = competition_id
        match_id = ''
        home_team = ''
        guest_team = ''

        super().__init__(**kwargs)

    def parse(self, response):
        matches = response.xpath("//div[@id='printableArea']/div/div/div/div/div[position() >= 1]/div[2]/div")

        for match in matches:
            match_id_string = match.xpath("./div/div/div[5]/p/@onclick").get()
            match_id = re.search(r'mID=(\d+)', match_id_string).group(1)

            home_team = match.xpath("./div/div/div[5]/p/span/*/text() | ./div/div/div[5]/p/span/text()").get().lower()
            guest_team = match.xpath("./div/div/div[9]/p/span/*/text() | ./div/div/div[9]/p/span/text()").get().lower()

            yield {
                'Match ID': match_id,
                'Home Team': home_team,
                'Guest Team': guest_team
            }

    def closed(spider, reason):
        src = 'data/competition_matches.csv'
        dst = 'data/{}_competition_matches.csv'.format(spider.competition_id)

        try:
            os.rename(src, dst)

            print('\x1b[6;30;42m' + '\n Matchscraper: {} file was created! '.format(dst) + '\x1b[0m\n')
        except(FileExistsError):
            print('\x1b[6;30;43m' + '\n Matchscraper: file {} already exists.\n{} was created or renamed! '.format(dst, src) + '\x1b[0m\n')