import scrapy
import os

class SuperligaHomeSpider(scrapy.Spider):
    name = 'home_superliga'

    def __init__(self, match_id='', **kwargs):
        self.start_urls = [f'https://cbv-web.dataproject.com/MatchStatistics.aspx?mID={match_id}&ID=18&CID=70&PID=34']
        self.match_id = match_id
        match_date = ''
        home_team = ''

        super().__init__(**kwargs)

    def parse(self, response):
        match_date_1 = response.xpath("normalize-space(//span[@id='Content_Main_LB_DateTime']/text())").get().replace(' ', '')
        match_date_2 = match_date_1.split(',',1)[1]
        match_date = match_date_2.split('-')[0]

        home_team = response.xpath("normalize-space(//span[@id='Content_Main_LBL_HomeTeam']/text())").get().replace(' ', '-')
        home_players = response.xpath("//div[@id='Content_Main_ctl17_RP_MatchStats_RPL_MatchStats_0']/div[3]/div/div/table/tbody/tr")

        for player in home_players:
            player_number = player.xpath("./td[1]/p/span/text()").get()
            player_name = player.xpath("./td[2]/p/span/b/text()").get()
            points_tot = player.xpath("./td[8]/p/span/text()").get()
            points_BP = player.xpath("./td[9]/p/span/text()").get()
            points_WL = player.xpath("./td[10]/p/span/text()").get()

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
        os.rename('data/home_superliga.csv', 'data/{}_{}_home_{}.csv'.format(spider.match_id, spider.match_date, spider.home_team))