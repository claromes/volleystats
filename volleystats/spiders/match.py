import scrapy
import os
import re

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

        home_team_string = response.xpath("normalize-space(//span[@id='Content_Main_LBL_HomeTeam']/text())").get().replace(' ', '-')
        home_team = re.sub('[^A-Za-z0-9]+', '-', home_team_string)
        if home_team:
            home_team = home_team.lower()

        coach = response.xpath("//span[@id='Content_Main_ctl17_RP_MatchStats_Coach_Home_0']/text()").get()
        if coach:
            coach = coach.lower()
            coach = parse_coach(coach)

        location = response.xpath("//span[@id='Content_Main_LB_Stadium']/text()").get()
        if location:
            location = location.lower()

        home_players = response.xpath("//div[@id='Content_Main_ctl17_RP_MatchStats_RPL_MatchStats_0']/div[3]/div/div/table/tbody/tr")

        for player in home_players:
            player_number = player.xpath('./td[1]/p/span/text()').get()
            player_name = player.xpath('./td[2]/p/span/b/text()').get()
            if player_name:
                player_name = player_name.lower()

            points_tot = player.xpath('./td[8]/p/span/text()').get()
            points_BP = player.xpath('./td[9]/p/span/text()').get()
            points_WL = player.xpath('./td[10]/p/span/text()').get()

            serve_tot = player.xpath('./td[12]/p/span/text()').get()
            serve_err = player.xpath('./td[13]/p/span/text()').get()
            serve_ace = player.xpath('./td[14]/p/span/text()').get()

            reception_tot = player.xpath('./td[15]/p/span/text()').get()
            reception_err = player.xpath('./td[16]/p/span/text()').get()
            reception_pos = player.xpath('./td[17]/p/span/text()').get()
            reception_exec = player.xpath('./td[18]/p/span/text()').get()

            attack_tot = player.xpath('./td[21]/p/span/text()').get()
            attack_err = player.xpath('./td[22]/p/span/text()').get()
            attack_block = player.xpath('./td[23]/p/span/text()').get()
            attack_exc = player.xpath('./td[24]/p/span/text()').get()
            attack_exc_perc = player.xpath('./td[25]/p/span/text()').get()

            block_points = player.xpath('./td[27]/p/span/text()').get()

            yield {
                'Match ID': self.match_id,
                'Match Date': match_date,
                'Home Team': home_team,
                'Home Coach': coach,
                'Stadium': location,
                'Number': player_number,
                'Name': player_name,
                'Total Points': points_tot,
                'Break Points': points_BP,
                'W-L': points_WL,
                'Total Serve': serve_tot,
                'Serve Errors': serve_err,
                'Ace': serve_ace,
                'Total Receptions': reception_tot,
                'Reception Erros': reception_err,
                'Positive Pass Percentage': reception_pos,
                'Excellent/ Perfect Pass Percentage': reception_exec,
                'Total Attacks': attack_tot,
                'Attack Erros': attack_err,
                'Blocked Attack': attack_block,
                'Attack Points (Exc.)': attack_exc,
                'Attack Points Percentage (Exc.%)': attack_exc_perc,
                'Block Points': block_points
            }

        self.match_date = match_date
        self.home_team = home_team

    def closed(spider, reason):
        src = f'data/{spider.fed_acronym}-{spider.match_id}-home_stats.csv'
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

        guest_team_string = response.xpath("normalize-space(//span[@id='Content_Main_LBL_GuestTeam']/text())").get().replace(' ', '-')
        guest_team = re.sub('[^A-Za-z0-9]+', '-', guest_team_string)
        if guest_team:
            guest_team = guest_team.lower()

        coach = response.xpath("//span[@id='Content_Main_ctl17_RP_MatchStats_Coach_Guest_0']/text()").get()
        if coach:
            coach = coach.lower()
            coach = parse_coach(coach)

        location = response.xpath("//span[@id='Content_Main_LB_Stadium']/text()").get()
        if location:
            location = location.lower()

        guest_players = response.xpath("//div[@id='Content_Main_ctl17_RP_MatchStats_RPL_MatchStats_0']/div[5]/div/div/table/tbody/tr")

        for player in guest_players:
            player_number = player.xpath('./td[1]/p/span/text()').get()
            player_name = player.xpath('./td[2]/p/span/b/text()').get()
            if player_name:
                player_name = player_name.lower()

            points_tot = player.xpath('./td[8]/p/span/text()').get()
            points_BP = player.xpath('./td[9]/p/span/text()').get()
            points_WL = player.xpath('./td[10]/p/span/text()').get()

            serve_tot = player.xpath('./td[12]/p/span/text()').get()
            serve_err = player.xpath('./td[13]/p/span/text()').get()
            serve_ace = player.xpath('./td[14]/p/span/text()').get()

            reception_tot = player.xpath('./td[15]/p/span/text()').get()
            reception_err = player.xpath('./td[16]/p/span/text()').get()
            reception_pos = player.xpath('./td[17]/p/span/text()').get()
            reception_exc = player.xpath('./td[18]/p/span/text()').get()

            attack_tot = player.xpath('./td[21]/p/span/text()').get()
            attack_err = player.xpath('./td[22]/p/span/text()').get()
            attack_block = player.xpath('./td[23]/p/span/text()').get()
            attack_exc = player.xpath('./td[24]/p/span/text()').get()
            attack_exc_perc = player.xpath('./td[25]/p/span/text()').get()

            block_points = player.xpath('./td[27]/p/span/text()').get()

            yield {
                'Match ID': self.match_id,
                'Match Date': match_date,
                'Guest Team': guest_team,
                'Guest Coach': coach,
                'Stadium': location,
                'Number': player_number,
                'Name': player_name,
                'Total Points': points_tot,
                'Break Points': points_BP,
                'W-L': points_WL,
                'Total Serve': serve_tot,
                'Serve Errors': serve_err,
                'Ace': serve_ace,
                'Total Receptions': reception_tot,
                'Reception Erros': reception_err,
                'Positive Pass Percentage (Pos%)': reception_pos,
                'Excellent/ Perfect Pass Percentage (Exc.%)': reception_exc,
                'Total Attacks': attack_tot,
                'Attack Erros': attack_err,
                'Blocked Attack': attack_block,
                'Attack Points (Exc.)': attack_exc,
                'Attack Points Percentage (Exc.%)': attack_exc_perc,
                'Block Points': block_points
            }

        self.match_date = match_date
        self.guest_team = guest_team

    def closed(spider, reason):
        src = f'data/{spider.fed_acronym}-{spider.match_id}-guest_stats.csv'
        dst = f'data/{spider.fed_acronym}-{spider.match_id}-{spider.match_date}-guest-{spider.guest_team}.csv'

        try:
            os.rename(src, dst)

            print(f'volleystats: {dst} file was created')
        except(FileExistsError):
            print(f'volleystats: file {dst} already exists.\n{src} was created or renamed')
