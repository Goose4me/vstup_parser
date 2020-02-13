# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from vstup_parser.items import VstupParserItem


class MySpider(scrapy.Spider):
    name = 'spider'
    BASIC_URL = "http://vstup.info/2019/"
    urls = ["http://vstup.info/2019/i2019o5.html", "http://vstup.info/2019/i2019o27.html", "http://vstup.info/2019/i2019o9.html", "http://vstup.info/2019/i2019o14.html"  ]
    start_urls = urls

    def parse(self, response):
        hrefs = response.xpath('//*[@id="vnzt0"]/tbody/tr/td/a/@href').extract()
        for href in hrefs[:2]:
            url = self.BASIC_URL + href[2:]
            print(url)

            yield Request(url=url, callback=self.university_pars)

    def university_pars(self, response):
        bs = response.xpath('//*[@id="denna1"]/tbody/tr/td[1]/b[2]/text()').extract()
        urls = response.xpath('//*[@id="denna1"]/tbody/tr/td[2]/a/@href').extract()
        if bs != [] and urls != []:
            for b in range(len(bs)):
                if bs[b] == "ПЗСО 11кл.":
                    url = "http://vstup.info/2018/" + urls[b][2:]
                    yield Request(url=url, callback=self.koncurs_parse)

    def koncurs_parse(self, response):
        name_of_university = response.xpath('//*[@id="list"]/div/div[1]/div/div/h3/text()').extract_first()
        url = response.url
        number = response.xpath(
            '//*[@class="tablesaw tablesaw-stack tablesaw-sortable"]/tbody/tr/td[1]/text()').extract()
        names_of_pupil = response.xpath(
            '//*[@class="tablesaw tablesaw-stack tablesaw-sortable"]/tbody/tr/td[2]/text()').extract()
        priority = response.xpath(
            '//*[@class="tablesaw tablesaw-stack tablesaw-sortable"]/tbody/tr/td[3]/text()').extract()
        av_mark = response.xpath(
            '//*[@class="tablesaw tablesaw-stack tablesaw-sortable"]/tbody/tr/td[4]/text()').extract()
        state = response.xpath(
            '//*[@class="tablesaw tablesaw-stack tablesaw-sortable"]/tbody/tr/td[4]/text()').extract()
        a = response.xpath(
            '//*[@class="tablesaw tablesaw-stack tablesaw-sortable"]/tbody/tr/td[6]/ul/li[1]/strong/text()').extract()
        b = response.xpath(
            '//*[@class="tablesaw tablesaw-stack tablesaw-sortable"]/tbody/tr/td[6]/ul/li[2]/strong/text()').extract()
        c = response.xpath(
            '//*[@class="tablesaw tablesaw-stack tablesaw-sortable"]/tbody/tr/td[6]/ul/li[3]/strong/text()').extract()
        d = response.xpath(
            '//*[@class="tablesaw tablesaw-stack tablesaw-sortable"]/tbody/tr/td[6]/ul/li[4]/strong/text()').extract()
        # print(a,b,c,d)
        print(names_of_pupil, name_of_university, url)
        for name in range(len(names_of_pupil)):
            item = VstupParserItem()
            item["name_of_university"] = name_of_university.strip()
            item["number"] = number[name].strip()
            item["url"] = url.strip()
            item["name_of_pupil"] = names_of_pupil[name].strip()
            item["priority"] = priority[name].strip()
            item["av_mark"] = av_mark[name].strip()
            item["state"] = state[name].strip()
            item["a"] = a[name].strip()
            item["b"] = b[name].strip()
            item["c"] = c[name].strip()
            item["d"] = d[name].strip()
            if "Шевченко" in item["name_of_pupil"] or "огиба" in item["name_of_pupil"]:
                print("\n"*10)
                print(item)
                print("\n"*10)
            yield item
