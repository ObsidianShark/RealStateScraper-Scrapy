# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class HouseItem(Item):
    # House description
    price = Field()
    address = Field()
    bedrooms = Field()
    bathrooms = Field()
    park = Field()
    residence_type = Field()

    # Spider info
    url = Field()
    spider = Field()
    date = Field()
