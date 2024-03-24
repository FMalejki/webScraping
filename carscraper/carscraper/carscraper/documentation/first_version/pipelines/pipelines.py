# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CarscraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)
        value = adapter.get('price')
        adapter['price'] = value.strip()

        value = adapter.get('price')
        value = value.replace('€','')
        value = value.replace('\n','')
        value = value.replace('VB','')
        value = value.replace('.','')
        if value != '':
            adapter['price'] = int(value)
        else:
            adapter['price'] = ''
        return item
