input_table = [
    # BRAND: (f.e. mercedes_benz) - 0 MUST BE  !!!!
    'mercedes-benz',
    #########
    # MODEL: - 1
    'c-klasa',
    ##########
    # MILEAGE IN KILOMERERS: (wtf is a kilometer?)(from_to) - 2 , 3 MUST BE 2 VALUES !!!
    '40000',
    '230000',
    ##########
    # PRODUCTION YEAR: - 4 , 5 MUST BE 2 VALUES !!!
    '2009',
    '2013',
    ##########
    # FUEL TYPE: - 6
    'petrol',
    ##########
    # POWER OF AUTO: - 7 , 8 MUST BE 2 VALUES !!!
    '100',
    '200',
    ###############
    # DAMAGES: - 9
    '0',
    #############
    # SHIFT - 10
    'manual',
]
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
TMPstart_urls[5] = 'a'
print(TMPstart_urls)