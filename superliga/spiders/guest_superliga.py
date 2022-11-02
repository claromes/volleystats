import scrapy

class SuperligaPointsSpider(scrapy.Spider):
    name = 'guest_superliga'

    def __init__(self, match='', **kwargs):
        self.start_urls = [f'https://cbv-web.dataproject.com/MatchStatistics.aspx?mID={match}&ID=18&CID=70&PID=34']
        super().__init__(**kwargs)

    def parse(self, response):
        guest_team = response.xpath("//span[@id='Content_Main_LBL_GuestTeam']/text()").get()
        guest_players = response.xpath("//div[@id='Content_Main_ctl17_RP_MatchStats_RPL_MatchStats_0']/div[5]/div/div/table/tbody/tr")

        for player in guest_players:
            player_number = player.xpath("./td[1]/p/span/text()").get()
            player_name = player.xpath("./td[2]/p/span/b/text()").get()
            points_tot = player.xpath("./td[8]/p/span/text()").get()
            points_BP = player.xpath("./td[9]/p/span/text()").get()
            points_WL = player.xpath("./td[10]/p/span/text()").get()

            yield {
                'Guest Team': guest_team,
                'Number': player_number,
                'Name': player_name,
                'Total Points': points_tot,
                'Break Points': points_BP,
                'W-L': points_WL
            }