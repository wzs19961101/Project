# -*- coding: utf-8 -*-
import scrapy
from gamelol.items import GamelolItem

class GamelolSpiderSpider(scrapy.Spider):
    name = 'gamelol_spider'
    allowed_domains = ['euw.op.gg']
    start_urls = ['http://euw.op.gg/champion/sett/statistics/top/matchup']
    def parse(self, response):
        hero_lists = response.xpath("//div[@class='champion-matchup-champion-list']/div")
        for i_item in hero_lists:
            gamelol_item=GamelolItem()
            gamelol_item['hero_name'] = i_item.xpath('.//@data-champion-name').extract()
            gamelol_item['win_rate'] =i_item.xpath('.//@data-value-winrate').extract()
            yield gamelol_item