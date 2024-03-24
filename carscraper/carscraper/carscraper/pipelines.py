# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class CarscraperPipeline:
    def process_item(self, item, spider):
        #RAISE DROPITEM IS FOR NOT SAVING A ITEM TO FILE OR DATABASE
        #USE THIS IN NEWER PIPELINE - MODIFY THIS ONE
        #extracting spider name
        if spider.name == "carspider":
            adapter = ItemAdapter(item)
            value_price = adapter.get('price')
            value_price = value_price.strip()
            if value_price is not None:
                value_price = value_price.replace('€','')
                value_price = value_price.replace('\n','')
                value_price = value_price.replace('VB','')
                value_price = value_price.replace('.','')
                adapter['price'] = int(value_price)
            else:
                raise DropItem(item)
            #making year an intiger
            value_year = adapter['year']
            if value_year is not None:
                adapter['year'] = int(value_year)
            else:
                raise DropItem(item)
            #delating km sign, dots and whitespaces from mileage
            value_mileage = adapter['mileage']
            value_mileage = value_mileage.replace('.','')
            value_mileage = value_mileage.replace('km','')
            value_mileage = value_mileage.strip()
            if value_mileage is not None:
                if value_mileage == "Gesuch":
                    raise DropItem(item)
                else:
                    adapter['mileage'] = int(value_mileage)
            else:
                raise DropItem(item)
            return item
        elif spider.name == "carspiderOTOMOTO":
            #processing otomoto items:
            #data structure:
            #in the documentation about specific spider
            #this too:
            #if item is not None:
            adapter = ItemAdapter(item)
            val_price = adapter['price']
            val_year = adapter['year']
            val_mileage = adapter['mileage']
            #this line is not necessary:
            #if val_mileage is not None and val_year is not None and val_price is not None:
            #year
            adapter['year'] = int(val_year)
            #price:
            val_price = val_price.strip()
            val_price = val_price.replace(' ','')
            adapter['price'] = int(val_price)
            #mileage:
            val_mileage = val_mileage.replace('km','')
            val_mileage = val_mileage.strip()
            val_mileage = val_mileage.replace(' ','')
            adapter['mileage'] = int(val_mileage)
            return item


