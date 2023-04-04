import scrapy
import os
import re

class MatchListSpider(scrapy.Spider):
    name = 'match_list'

    def __init__(self, fed_acronym='', competition_id='', **kwargs):
        self.start_urls = [f'https://{fed_acronym}-web.dataproject.com/CompetitionMatches.aspx?ID={competition_id}']
        self.competition_id = competition_id
        match_id = ''
        home_team = ''
        guest_team = ''

        super().__init__(**kwargs)

    def parse(self, response):
        for j in range(0, 60, 2):
            for i in range(0, 12, 2):
                match = response.xpath("//div[@id='ctl00_Content_Main_70_userControl_RADLIST_Legs_ctrl{}_RADLIST_Matches_ctrl{}_MatchRow']/div/div".format(j, i))

                match_id_string = match.xpath("./div[4]/p/@onclick").get()
                match_id = re.search(r'mID=(\d+)', match_id_string).group(1)

                home_team = match.xpath("./div[5]/p/span/*/text() | ./div[5]/p/span/text()").get().lower()
                guest_team = match.xpath("./div[9]/p/span/*/text() | ./div[9]/p/span/text()").get().lower()

                yield {
                    'Match ID': match_id,
                    'Home Team': home_team,
                    'Guest Team': guest_team
                }

    def closed(spider, reason):
        os.rename('data/match_list.csv', 'data/{}_match_list.csv'.format(spider.competition_id))