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
        dst = f'data/{spider.competition_id}_competition_matches.csv'

        try:
            os.rename(src, dst)

            print(f'volleystats: {dst} file was created')
        except(FileExistsError):
            print(f'volleystats: file {dst} already exists.\n{src} was created or renamed')