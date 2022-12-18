import scrapy
import os
from . import utils

class SuperligaGuestSpider(scrapy.Spider):
    name = 'guest_superliga'

    def __init__(self, match_id='', **kwargs):
        self.start_urls = [f'https://cbv-web.dataproject.com/MatchStatistics.aspx?mID={match_id}&ID=18&CID=70&PID=34']
        self.match_id = match_id
        match_date = ''
        guest_team = ''

        super().__init__(**kwargs)

    def parse(self, response):
        match_date_text = response.xpath("normalize-space(//span[@id='Content_Main_LB_DateTime']/text())").get()
        match_date = utils.parse_ptbr_date(match_date_text)

        guest_team = response.xpath("normalize-space(//span[@id='Content_Main_LBL_GuestTeam']/text())").get().replace(' ', '-').lower()
        guest_players = response.xpath("//div[@id='Content_Main_ctl17_RP_MatchStats_RPL_MatchStats_0']/div[5]/div/div/table/tbody/tr")

        for player in guest_players:
            player_number = player.xpath("./td[1]/p/span/text()").get()
            player_name = player.xpath("./td[2]/p/span/b/text()").get()
            points_tot = player.xpath("./td[8]/p/span/text()").get()
            points_BP = player.xpath("./td[9]/p/span/text()").get()
            points_WL = player.xpath("./td[10]/p/span/text()").get()

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
        os.rename('data/guest_superliga.csv', 'data/{}_{}_guest_{}.csv'.format(spider.match_id, spider.match_date, spider.guest_team))