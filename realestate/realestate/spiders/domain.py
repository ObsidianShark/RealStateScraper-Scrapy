from datetime import datetime

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from scrapy.loader import ItemLoader

from realestate.items import HouseItem


class SouthEastQueenslandSpider(scrapy.Spider):
    """Spider for scraping residences with a base price in South East Queensland"""

    name = "domain_SEQ"
    allowed_domains = ["domain.com.au"]
    start_urls = [
        "https://www.domain.com.au/sale/south-east-queensland-greater-region-qld/"
    ]
    custom_settings = {
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_DEBUG": True,
        "HTTPCACHE_ENABLED": True,
    }

    def parse(self, response):
        # Follow links to house pages
        for link in response.css("a.address::attr('href')"):
            yield response.follow(link, callback=self.parse_house)

        # Next page
        next_page = response.css("a.css-1lkjjfg:nth-child(3)::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_house(self, response):
        house_description = ItemLoader(item=HouseItem(), selector=response)
        house_description.default_input_processor = MapCompose()
        house_description.default_output_processor = TakeFirst()

        # Scrape House description
        house_description.add_css("price", "div.css-1texeil::text")
        house_description.add_css("address", "h1.css-164r41r::text")
        house_description.add_css(
            "bedrooms",
            ".css-ghc6s4 > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)::text",
        )
        house_description.add_css(
            "bathrooms",
            ".css-ghc6s4 > div:nth-child(1) > span:nth-child(2) > span:nth-child(1)::text",
        )
        house_description.add_css(
            "park",
            ".css-ghc6s4 > div:nth-child(1) > span:nth-child(3) > span:nth-child(1)::text",
        )
        house_description.add_css(
            "residence_type", ".css-dvvls9 > span:nth-child(1)::text"
        )

        # Spider info
        house_description.add_value("url", response.request.url)
        house_description.add_value("spider", self.name)
        house_description.add_value("date", datetime.now())

        yield house_description.load_item()


class CentralQueenslandSpider(scrapy.Spider):
    """Spider for scraping residences with a base price in Central Queensland"""

    name = "domain_CQ"
    allowed_domains = ["domain.com.au"]
    start_urls = [
        "https://www.domain.com.au/sale/central-queensland-greater-region-qld/"
    ]
    custom_settings = {
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_DEBUG": True,
        "HTTPCACHE_ENABLED": True,
    }

    def parse(self, response):
        # Follow links to house pages
        for link in response.css("a.address::attr('href')"):
            yield response.follow(link, callback=self.parse_house)

        # Next page
        next_page = response.css(".css-xixru3::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_house(self, response):
        house_description = ItemLoader(item=HouseItem(), selector=response)
        house_description.default_input_processor = MapCompose()
        house_description.default_output_processor = TakeFirst()

        # Scrape House description
        house_description.add_css("price", "div.css-1texeil::text")
        house_description.add_css("address", "h1.css-164r41r::text")
        house_description.add_css(
            "bedrooms",
            ".css-ghc6s4 > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)::text",
        )
        house_description.add_css(
            "bathrooms",
            ".css-ghc6s4 > div:nth-child(1) > span:nth-child(2) > span:nth-child(1)::text",
        )
        house_description.add_css(
            "park",
            ".css-ghc6s4 > div:nth-child(1) > span:nth-child(3) > span:nth-child(1)::text",
        )
        house_description.add_css(
            "residence_type", ".css-dvvls9 > span:nth-child(1)::text"
        )

        # Spider info
        house_description.add_value("url", response.request.url)
        house_description.add_value("spider", self.name)
        house_description.add_value("date", datetime.now())

        yield house_description.load_item()


class NorthQueenslandSpider(scrapy.Spider):
    """Spider for scraping residences with a base price in North Queensland"""

    name = "domain_NQ"
    allowed_domains = ["domain.com.au"]
    start_urls = ["https://www.domain.com.au/sale/north-queensland-greater-region-qld/"]
    custom_settings = {
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_DEBUG": True,
        "HTTPCACHE_ENABLED": True,
    }

    def parse(self, response):
        # Follow links to house pages
        for link in response.css("a.address::attr('href')"):
            yield response.follow(link, callback=self.parse_house)

        # Next page
        next_page = response.css(".css-xixru3::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_house(self, response):
        house_description = ItemLoader(item=HouseItem(), selector=response)
        house_description.default_input_processor = MapCompose()
        house_description.default_output_processor = TakeFirst()

        # Scrape House description
        house_description.add_css("price", "div.css-1texeil::text")
        house_description.add_css("address", "h1.css-164r41r::text")
        house_description.add_css(
            "bedrooms",
            ".css-ghc6s4 > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)::text",
        )
        house_description.add_css(
            "bathrooms",
            ".css-ghc6s4 > div:nth-child(1) > span:nth-child(2) > span:nth-child(1)::text",
        )
        house_description.add_css(
            "park",
            ".css-ghc6s4 > div:nth-child(1) > span:nth-child(3) > span:nth-child(1)::text",
        )
        house_description.add_css(
            "residence_type", ".css-dvvls9 > span:nth-child(1)::text"
        )

        # Spider info
        house_description.add_value("url", response.request.url)
        house_description.add_value("spider", self.name)
        house_description.add_value("date", datetime.now())

        yield house_description.load_item()


class FarNorthQueenslandSpider(scrapy.Spider):
    """Spider for scraping residences with a base price in Far North Queensland"""

    name = "domain_FNQ"
    allowed_domains = ["domain.com.au"]
    start_urls = [
        "https://www.domain.com.au/sale/far-north-queensland-greater-region-qld/"
    ]
    custom_settings = {
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_DEBUG": True,
        "HTTPCACHE_ENABLED": True,
    }

    def parse(self, response):
        # Follow links to house pages
        for link in response.css("a.address::attr('href')"):
            yield response.follow(link, callback=self.parse_house)

        # Next page
        next_page = response.css(".css-xixru3::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_house(self, response):
        house_description = ItemLoader(item=HouseItem(), selector=response)
        house_description.default_input_processor = MapCompose()
        house_description.default_output_processor = TakeFirst()

        # Scrape House description
        house_description.add_css("price", "div.css-1texeil::text")
        house_description.add_css("address", "h1.css-164r41r::text")
        house_description.add_css(
            "bedrooms",
            ".css-ghc6s4 > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)::text",
        )
        house_description.add_css(
            "bathrooms",
            ".css-ghc6s4 > div:nth-child(1) > span:nth-child(2) > span:nth-child(1)::text",
        )
        house_description.add_css(
            "park",
            ".css-ghc6s4 > div:nth-child(1) > span:nth-child(3) > span:nth-child(1)::text",
        )
        house_description.add_css(
            "residence_type", ".css-dvvls9 > span:nth-child(1)::text"
        )

        # Spider info
        house_description.add_value("url", response.request.url)
        house_description.add_value("spider", self.name)
        house_description.add_value("date", datetime.now())

        yield house_description.load_item()
