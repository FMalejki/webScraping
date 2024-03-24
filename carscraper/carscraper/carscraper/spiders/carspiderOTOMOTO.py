import scrapy
from carscraper.items import CarsItems

class CarspiderotomotoSpider(scrapy.Spider):
    name = "carspiderOTOMOTO"
    allowed_domains = ["www.otomoto.pl"]
    #first look at main carspider for instructions
    # INPUT MUST BE DONE IN SPECIFIED WAY
    input_table = [
        # BRAND: (f.e. mercedes_benz) - 0 MUST BE  !!!!
        # !!! it must be written with '-' instead od '_'
        'mercedes-benz',
        #########
        # MODEL: - 1 (ML)
        'm-klasa',
        ##########
        # MILEAGE IN KILOMERERS: (wtf is a kilometer?)(FROM -> TO) - 2 , 3 MUST BE 2 VALUES !!!
        '10000',
        '300000',
        ##########
        # PRODUCTION YEAR: - 4 , 5 (FROM -> TO) MUST BE 2 VALUES !!!
        '2000',
        '2024',
        ##########
        # FUEL TYPE: - 6
        '',
        ##########
        # POWER OF AUTO: - 7 , 8 (FROM -> TO) MUST BE 2 VALUES !!!
        '',
        '',
        ###############
        # DAMAGES: - 9
        '0',
        #############
        # SHIFT - 10
        '',
    ]
    ##########################################################
    ###################INPUT IN POLISH########################
    ##########################################################
    #################### END OF INPUT ########################
    ##########################################################
    ######### THE REST OF IT IS A FUNCTIONING PROGRAM ########
    ##########################################################
    ################## DO NOT EDIT ! ! ! #####################
    ##########################################################
    TMPstart_urls = "https://www.otomoto.pl/osobowe"
    for i in range(0, 11):
        if input_table[i] != '':
            if i == 0:
                TMPstart_urls = TMPstart_urls + "/" + input_table[0]
            elif i == 1:
                TMPstart_urls = TMPstart_urls + "/" + input_table[1]

    flag = False
    for j in range(2, 11):
        if input_table[j] != '':
            flag = True
            TMPstart_urls = TMPstart_urls + '?'
            break

    if flag == True:
        for i in range(2, 11):
            if i == 2:
                if input_table[i] != '':
                    if TMPstart_urls[len(TMPstart_urls) - 1] == '?':
                        TMPstart_urls = TMPstart_urls + "search%5Bfilter_float_mileage%3Afrom%5D=" + input_table[
                            2] + "&search%5Bfilter_float_mileage%3Ato%5D=" + input_table[3]
                    else:
                        TMPstart_urls = TMPstart_urls + "&search%5Bfilter_float_mileage%3Afrom%5D=" + input_table[
                            2] + "&search%5Bfilter_float_mileage%3Ato%5D=" + input_table[3]
            elif i == 10:  # this must be done as the last one so at the 10th position (i index should be changed)
                # here must be years
                if input_table[4] != '' and input_table[5] != '':
                    pos_of = TMPstart_urls.find('?')

                    url_to_replace = TMPstart_urls[pos_of:]
                    url_to_work_at = url_to_replace

                    print(url_to_work_at)
                    if pos_of == len(TMPstart_urls) - 1:
                        replacing_url = '/od-' + input_table[
                            4] + url_to_work_at + 'search%5Bfilter_float_year%3Ato%5D=' + input_table[5]
                        TMPstart_urls = TMPstart_urls.replace(url_to_replace, replacing_url)
                    else:
                        replacing_url = '/od-' + input_table[
                            4] + url_to_work_at + '&search%5Bfilter_float_year%3Ato%5D=' + input_table[5]
                        TMPstart_urls = TMPstart_urls.replace(url_to_replace, replacing_url)
            elif i == 6:
                if input_table[i] != '':
                    if TMPstart_urls[len(TMPstart_urls) - 1] == '?':
                        TMPstart_urls = TMPstart_urls + "search%5Bfilter_enum_fuel_type%5D%5B0%5D=" + input_table[6]
                    else:
                        TMPstart_urls = TMPstart_urls + "&search%5Bfilter_enum_fuel_type%5D%5B0%5D=" + input_table[6]
            elif i == 7:
                if input_table[i] != '' and input_table[i + 1] != '':
                    if TMPstart_urls[len(TMPstart_urls) - 1] == '?':
                        TMPstart_urls = TMPstart_urls + "search%5Bfilter_float_engine_power%3Afrom%5D=" + input_table[
                            7] + "&search%5Bfilter_float_engine_power%3Ato%5D=" + input_table[8]
                    else:
                        TMPstart_urls = TMPstart_urls + "&search%5Bfilter_float_engine_power%3Afrom%5D=" + input_table[
                            7] + "&search%5Bfilter_float_engine_power%3Ato%5D=" + input_table[8]
            elif i == 9:
                if input_table[i] != '':
                    if TMPstart_urls[len(TMPstart_urls) - 1] == '?':
                        TMPstart_urls = TMPstart_urls + "search%5Bfilter_enum_damaged%5D=" + input_table[9]
                    else:
                        TMPstart_urls = TMPstart_urls + "&search%5Bfilter_enum_damaged%5D=" + input_table[9]
            elif i == 4:
                if input_table[10] != '':
                    if TMPstart_urls[len(TMPstart_urls) - 1] == '?':
                        TMPstart_urls = TMPstart_urls + "search%5Bfilter_enum_gearbox%5D%5B0%5D=" + input_table[10]
                    else:
                        TMPstart_urls = TMPstart_urls + "&search%5Bfilter_enum_gearbox%5D%5B0%5D=" + input_table[10]

    start_urls = [TMPstart_urls]

    def parse(self, response):
        full_cars = response.css('article.ooa-yca59n')
        car_items = CarsItems()
        for car in full_cars:
            price_val = car.css('h3.e1oqyyyi16.ooa-1n2paoq.er34gjf0 ::text').get()
            mileage_val = car.xpath("//section[@class='ooa-10gfd0w e1oqyyyi1']/div[@class='ooa-d3dp2q e1oqyyyi2']/dl[@class='ooa-uioh5d e1oqyyyi11']/dd[@data-parameter='mileage']/text()").get()
            year_val = car.xpath("//section[@class='ooa-10gfd0w e1oqyyyi1']/div[@class='ooa-d3dp2q e1oqyyyi2']/dl[@class='ooa-uioh5d e1oqyyyi11']/dd[@data-parameter='year']/text()").get()
            car_items['year'] = year_val
            car_items['mileage'] = mileage_val
            car_items['price'] = price_val
            yield car_items

        #so there is no link associated with next-page arrow >
        #so we need to somehow craft it
        #we just increase the single number in page link (at the end of it)[if it is here - if not we need to add it]
        #but if we dont check if there is another page we are going to loop the program on the last page
        #so to increase the number in link we need to check if there is an next-page arrow
        #TO DO!!!
        #if an arrow exist
        whole_list = response.css('ul.pagination-list.ooa-1vdlgt7')
        check_element = whole_list.xpath("//li[@data-testid='pagination-step-forwards'][@aria-disabled='false']").get()
        if check_element is not None:
            next_page = response.url
            if next_page.find("&page=") != -1:
                last_occurence = next_page.rfind('=')
                page_num = int(next_page[last_occurence+1:])
                page_num += 1
                first_part = next_page[:last_occurence+1]
                #I needed to change string to list in order to modify it
                next_page = first_part + str(page_num)
                #A NUMBER CAN HAVE MULTIPLE LETTERS!!!!!!
            else:
                next_page = next_page + "&page=2"
            yield response.follow(next_page, callback=self.parse)



