import scrapy
import os
import re
import sys

from ..utils import *

class HomeStatsSpider(scrapy.Spider):
    name = 'home_stats'

    def __init__(self, fed_acronym='', match_id='', **kwargs):
        self.start_urls = [f'https://{fed_acronym}-web.dataproject.com/MatchStatistics.aspx?mID={match_id}']
        self.fed_acronym = fed_acronym
        self.match_id = match_id
        match_date = ''
        home_team = ''

        super().__init__(**kwargs)

    def start_requests(self):        
        cookies = {f'CompetitionLangCode{self.fed_acronym}': 'en-GB'}
        yield scrapy.Request(self.start_urls[0], cookies=cookies, callback=self.parse)

    def parse(self, response):
        match_date_text = response.xpath("normalize-space(//span[@id='Content_Main_LB_DateTime']/text())").get()
        enGB = response.xpath("//*[contains(@class, 'RCB_Culture_en-GB')]/span/input/@value").get()

        if enGB == 'EN':
            match_date = parse_engb_date(match_date_text)

        home_team_string = response.xpath("normalize-space(//span[@id='Content_Main_LBL_HomeTeam']/text())").get().replace(' ', '-').lower()
        home_team = re.sub('[^A-Za-z0-9]+', '-', home_team_string)

        home_players = response.xpath("//div[@id='Content_Main_ctl17_RP_MatchStats_RPL_MatchStats_0']/div[3]/div/div/table/tbody/tr")

        for player in home_players:
            player_number = player.xpath('./td[1]/p/span/text()').get()
            player_name = player.xpath('./td[2]/p/span/b/text()').get().lower()
            points_tot = player.xpath('./td[8]/p/span/text()').get()
            points_BP = player.xpath('./td[9]/p/span/text()').get()
            points_WL = player.xpath('./td[10]/p/span/text()').get()

            yield {
                'Match ID': self.match_id,
                'Match Date': match_date,
                'Home Team': home_team,
                'Number': player_number,
                'Name': player_name,
                'Total Points': points_tot,
                'Break Points': points_BP,
                'W-L': points_WL
            }

        self.match_date = match_date
        self.home_team = home_team

    def closed(spider, reason):
        src = 'data/home_stats.csv'
        dst = f'data/{spider.fed_acronym}-{spider.match_id}-{spider.match_date}-home-{spider.home_team}.csv'

        try:
            os.rename(src, dst)

            print(f'volleystats: {dst} file was created')
        except(FileExistsError):
            print(f'volleystats: file {dst} already exists.\n{src} was created or renamed')

class GuestStatsSpider(scrapy.Spider):
    name = 'guest_stats'

    def __init__(self, fed_acronym='', match_id='', **kwargs):
        self.start_urls = [f'https://{fed_acronym}-web.dataproject.com/MatchStatistics.aspx?mID={match_id}']
        self.fed_acronym = fed_acronym
        self.match_id = match_id
        match_date = ''
        guest_team = ''

        super().__init__(**kwargs)

    def start_requests(self):        
        cookies = {f'CompetitionLangCode{self.fed_acronym}': 'en-GB'}
        yield scrapy.Request(self.start_urls[0], cookies=cookies, callback=self.parse)

    def parse(self, response):
        match_date_text = response.xpath("normalize-space(//span[@id='Content_Main_LB_DateTime']/text())").get()
        enGB = response.xpath("//*[contains(@class, 'RCB_Culture_en-GB')]/span/input/@value").get()

        if enGB == 'EN':
            match_date = parse_engb_date(match_date_text)

        guest_team_string = response.xpath("normalize-space(//span[@id='Content_Main_LBL_GuestTeam']/text())").get().replace(' ', '-').lower()
        guest_team = re.sub('[^A-Za-z0-9]+', '-', guest_team_string)

        guest_players = response.xpath("//div[@id='Content_Main_ctl17_RP_MatchStats_RPL_MatchStats_0']/div[5]/div/div/table/tbody/tr")

        for player in guest_players:
            player_number = player.xpath('./td[1]/p/span/text()').get()
            player_name = player.xpath('./td[2]/p/span/b/text()').get().lower()
            points_tot = player.xpath('./td[8]/p/span/text()').get()
            points_BP = player.xpath('./td[9]/p/span/text()').get()
            points_WL = player.xpath('./td[10]/p/span/text()').get()

            yield {
                'Match ID': self.match_id,
                'Match Date': match_date,
                'Guest Team': guest_team,
                'Number': player_number,
                'Name': player_name,
                'Total Points': points_tot,
                'Break Points': points_BP,
                'W-L': points_WL
            }

        self.match_date = match_date
        self.guest_team = guest_team

    def closed(spider, reason):
        src = 'data/guest_stats.csv'
        dst = f'data/{spider.fed_acronym}-{spider.match_id}-{spider.match_date}-guest-{spider.guest_team}.csv'

        try:
            os.rename(src, dst)

            print(f'volleystats: {dst} file was created')
        except(FileExistsError):
            print(f'volleystats: file {dst} already exists.\n{src} was created or renamed')
