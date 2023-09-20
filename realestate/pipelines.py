# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


def to_int(value):
    return int(value if value.isdigit() else 0)


def clean_price(value):
    return int(value.replace("$", "").replace(",", "").replace(".", ""))


class ValidPricePipeline:
    def process_item(self, item, spider):
        # Sort houses with a base price tag
        adapter = ItemAdapter(item)
        price = adapter.get("price")
        if price.startswith("$") and price.endswith("0") and ("-" and " ") not in price:
            priceValue = clean_price(price)
            adapter["price"] = priceValue
            return item
        else:
            raise DropItem(f"Not a valid price in {item}")


class StringNumPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Convert values to int
        i_bedrooms = to_int(adapter.get("bedrooms"))
        i_bathrooms = to_int(adapter.get("bathrooms"))
        i_park = to_int(adapter.get("park"))

        # Updates item fields
        adapter["bedrooms"] = i_bedrooms
        adapter["bathrooms"] = i_bathrooms
        adapter["park"] = i_park
        return item
