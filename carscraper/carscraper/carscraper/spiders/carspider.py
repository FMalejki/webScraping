#ITS AN EBAYKLEINEINZEGIEN SPIDER - FOR OTHERS CHECK THE PROJECT!!!
#this spiders purpose is to check prices of SPECIFIED CAR - by specified i mean all of the important data for a car,
#it need to have year of a car a specific model and the best for the output is to have all of this information
#complete - the program will please you to input all of it

#THE COMPLETE DOCUMENTATION IS LOCATED IN A WORD FILE INSIDE THE PROJECT
#the documentation include way the filtering of cars is done and some other things

import scrapy
from carscraper.items import CarsItems

class CarspiderSpider(scrapy.Spider):
    name = "carspider"
    allowed_domains = ["www.kleinanzeigen.de"]
    #we want to start parsing webpage in a final place so we need to know where we want to start
    #so according to documentation in a word file firstly we need to create our link
    #we will do it now:
    #INFORMATION ABOUT SPECIFIED CAR:
    #firstly complete the specific info here
    #(later I will create a tkinter python program that will do this input and data validation automaticly)
    #INPUT MUST BE DONE IN SPECIFIED WAY
    input_table = [
    #BRAND: (f.e. mercedes_benz) - 0 MUST BE  !!!!
    'mercedes_benz',
    #########
    #MODEL: - 1
    'm_klasse',
    ##########
    #MILEAGE IN KILOMERERS: (wtf is a kilometer?)(FROM -> TO) - 2 , 3 MUST BE 2 VALUES !!!
    '10000',
    '300000',
    ##########
    #PRODUCTION YEAR: - 4 , 5 (FROM -> TO) MUST BE 2 VALUES !!!
    '2000',
    '2024',
    ##########
    #FUEL TYPE: - 6
    '',
    ##########
    #POWER OF AUTO: - 7 , 8 (FROM -> TO) MUST BE 2 VALUES !!!
    '',
    '',
    ###############
    #DAMAGES: - 9
    'nein',
    #############
    #SHIFT - 10
    '',
        ]
    ##########################################################
    #################### END OF INPUT ########################
    ##########################################################
    ######### THE REST OF IT IS A FUNCTIONING PROGRAM ########
    ##########################################################
    ################## DO NOT EDIT ! ! ! #####################
    ##########################################################

    ADDstart_urls = "https://www.kleinanzeigen.de/s-autos/"+input_table[0]+"/c216+autos.marke_s:"+input_table[0]
    for i in range(1,11):
        if input_table[i] != '':
            if i == 1:
                ADDstart_urls = ADDstart_urls+"+autos.model_s:"+input_table[i]
            elif i == 2:
                ADDstart_urls = ADDstart_urls+"+autos.km_i:"+input_table[2]+"%2C"+input_table[3]
            elif i == 4:
                ADDstart_urls = ADDstart_urls+"+autos.ez_i:"+input_table[4]+"%2C"+input_table[5]
            elif i == 6:
                ADDstart_urls = ADDstart_urls+"+autos.fuel_s:"+input_table[6]
            elif i == 7:
                ADDstart_urls = ADDstart_urls+"+autos.power_i:"+input_table[7]+"%2C"+input_table[8]
            elif i == 9:
                ADDstart_urls = ADDstart_urls+"+autos.schaden_s:"+input_table[9]
            elif i == 10:
                ADDstart_urls = ADDstart_urls+"+autos.shift_s:"+input_table[10]
    ###### HERE WE START ######
    start_urls = [ADDstart_urls]
    #FIRST I NEED TO CHECK HOW TO DON'T LISTEN TO ROBOTS.TXT BECAUSE IT DESTROYS URLS WITH FILTERS#
    #### WORKS !!!! ####
    #### i did just a little change in settings.py file ####

    def parse(self, response):

        cars = response.css('article.aditem')
        for car in cars:
            car_items = CarsItems()
            price_value = car.css('.aditem-main--middle--price-shipping--price ::text').get()
            mileage_value = car.css('span.simpletag ::text').get()
            year_value = car.xpath("//div[@class = 'aditem-main']/div[@class = 'aditem-main--middle']/div[@class = 'aditem-main--bottom']/p[@class = 'text-module-end']/span[@class = 'simpletag']/following-sibling::span[@class = 'simpletag']/text()").get()
            if (str(price_value).strip()).replace('\n','') != 'VB':
                if price_value is not None and mileage_value is not None:
                    car_items['year'] = year_value
                    car_items['mileage'] = mileage_value
                    car_items['price'] = price_value
                    yield car_items


        next_page = response.css('a.pagination-next ::attr(href)').get()
        if next_page is not None:
            next_page_url = "https://www.kleinanzeigen.de"+next_page
            yield response.follow(next_page_url, callback=self.parse)

        #okay so we need to ensure we have full data complete, we need to check if we
        #have everything we need and ONLY data we need
        #brand is like Volkswagen, Volvo or Mercedes-Benz
        #model is for (in case of Volkswagen brand) Golf, Passat or Arteon
        #model = ""
        #response.follow(, callback= self.parse)
        #https://www.kleinanzeigen.de/s-autos/citroen/c216+autos.ez_i:2013%2C2016+autos.km_i:50000%2C200000+autos.marke_s:citroen+autos.model_s:c_crosser
