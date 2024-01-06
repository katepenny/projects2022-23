print('WELCOME TO ECORENE!')
#ecorene enables a person estimate their household  monthly exipenditure
#this helps a person regulate their expenditure on household bills 

print('ECORENE IS A PLATFORM THAT HELPS YOU OPTIMIZE YOUR ENERGY AND HOUSEHOLD CONSUMPTION')
name=input('ENTER YOUR NAMES: ')
money = float(input('ENTER YOUR MONTHLY SALARY/BUDGET: '))
saving = float(input('WHAT PERCENTAGE WOULD YOU LIKE TO SAVE?: '))
total_22 = total_11 = total_33 = total_55 =total_44 = 0

for x in range(7):
   
    print('''WHERE WOULD YOU LIKE TO BEGIN?
        1.GROCERIES
        2.ELECTRICITY BILL
        3.WATER BILL
        4.SAVINGS
        5.OTHER
        0.EXIT''')
    answer = int(input('ENTER CHOICE: '))



    if answer == 1:
                print('''
                1.Milk
                2.Beans
                3.Chicken
                4.Maize flour
                5.Rice
                6.Fish
                7.Other
                0.exit
            ''')
            
                milk_total = beans_total = rice_total = maize_total =  chicken_total = fish_total = item_total = 0
                
                
                for y in range(9):
                    answer_1 = int(input('ENTER CHOICE: '))
                    if answer_1 == 1:
                        milk1= 'MILK'
                        milk = int(input('ENTER AN ESTIMATE OF THE LITRES OF {} CONSUMED PER MONTH: '.format(milk1)))
                        milk_price= int(input('ENTER COST FOR ONE LITRE: '))# because of the changing prices i couldnt put a fixed price
                        milk_total = milk*milk_price
                    
                        print('Milk: UGX',milk_total)
                        
                        
                    elif answer_1 == 2:
                        beans1 ='BEANS'
                        beans = int(input('ENTER AN ESTIMATE OF KILOS OF {} CONSUMED PER MONTH: '.format(beans1)))
                        beans_price = int(input('ENTER COST OF ONE KILOGRAM: '))
                        beans_total = beans*beans_price
                        print('Beans: UGX',beans_total)
                    
                        
                        
                    elif answer_1 == 3:
                        
                        chicken = int(input('ENTER AN ESTIMATE OF KILOS/CHICKEN CONSUMED PER MONTH: '))
                        chicken_price = int(input('ENTER COST OF ONE KILOGRAM CHICKEN: '))
                        chicken_total = chicken*chicken_price
                        print('Chicken: UGX',chicken_total)
                    
                    
                    elif answer_1 == 4:
                        MAIZE ='MAIZE'
                        maize = int(input('ENTER AN ESTIMATE OF KILOS OF {} CONSUMED PER MONTH: '.format(MAIZE)))
                        maize_price = int(input('ENTER COST OF ONE KILOGRAM: '))
                        maize_total = maize*maize_price
                        print('Maize: UGX',maize_total)
                    
                        
                        
                    elif answer_1 == 5:
                        rice1= 'RICE'
                        rice = int(input('ENTER AN ESTIMATE OF KILOS CONSUMED PER MONTH: '.format(rice1)))
                        rice_price = int(input('ENTER COST OF ONE KILOGRAM:UGX '))
                        rice_total = rice*rice_price
                        print('Rice: UGX',rice_total)
                    
                    elif answer_1 == 6:
                        fish1= 'FISH'
                        fish = int(input('ENTER AN ESTIMATE OF KILOS/FISH CONSUMED A MONTH: '.format(fish1)))
                        fish_price = int(input('ENTER COST OF ONE KILOGRAM/FISH: '))
                        fish_total = fish*fish_price
                        print('Fish: UGX',fish_total)
                        
                    elif answer_1 == 7:
                        
                        item =input('ENTER NAME OF ITEM: ')
                        item = int(input('ENTER THE AMOUNT ITEM USED PER MONTH(kgs/litres/pack/other): '))
                        item_price = int(input('ENTER COST OF ONE UNIT: '))
                        item_total = item*item_price
                        print('Item: UGX',item_total)
                    
                    elif answer_1 == 0 :
                        total_22 = milk_total + beans_total + rice_total + maize_total+  chicken_total +fish_total + item_total
                        print('Your total monthly expenditure is roughly: UGX',total_22 )
                        break
                    else:
                        print('INVALID INPUT!TRY AGAIN')            
                                
                    
        
        
    elif answer ==2:
            print('''Please select an appliance:
        1.bulb 
        2.blender
        3.decorder
        4.Flat iron
        5.fridge
        6.phone charger
        7.TV
        8.Water Heater
        9.woofers
        10.other
        0.Exit''')

            total1 = total2 =  total3 = total4= total5= total6 = total7 = total8 = total9 = total10 = 0
            

            for x in range(12):
                appliance = int(input('SELECT APPLIANCE : '))
                
                if appliance == 1:
                    appliance = 'Bulb'
                    use = float(input('ENTER NUMBER OF APPLIANCES : '))
                    hours = float(input('ENTER NUMBER OF HOURS WHEN IN USE: '))
                    def usage(use,hours):
                        unit_cal = use*35*hours*30/1000
                        return unit_cal
                    units_consumed = usage(use,hours)
                    units_cost = usage(use,hours)*580 
                    service_fee = 3360
                    VAT = units_cost*18/100 
                    total1 = VAT + units_cost 
                    print('''Appliance = {0}\nUnits= {1}Units per month\nService fee = UGX {2}\nVAT = UGX {3}\nTotal = UGX {4}'''.format (appliance,units_consumed,service_fee,VAT,total1)) 

                elif appliance == 2:
                    appliance = 'Blender'

                    use = float(input('ENTER NUMBER OF APPLIANCES : '))
                    hours = float(input('ENTER NUMBER OF HOURS WHEN IN USE: '))
                    def usage(use,hours):
                        unit_cal1 = use*450*hours*30/1000
                        return unit_cal1
                    units_consumed = usage(use,hours)
                    units_cost = usage(use,hours)*580 
                    service_fee = 3360
                    VAT = units_cost*18/100 
                    total2 = VAT + units_cost
                    print('''Appliance = {0}\nUnits= {1}Units per month\nService fee = UGX {2}\nVAT = UGX {3}\nTotal = UGX {4}'''.format (appliance,units_consumed,service_fee,VAT,total2)) 


                elif appliance == 3:
                    appliance = 'Decorder'
                    use = float(input('ENTER NUMBER OF APPLIANCES : '))
                    hours = float(input('ENTER NUMBER OF HOURS WHEN IN USE: '))
                    def usage(use,hours):
                        unit_cal2 = use*30*hours*30/1000
                        return unit_cal2
                    units_consumed = usage(use,hours)
                    units_cost = usage(use,hours)*580 
                    service_fee = 3360
                    VAT = units_cost*18/100 
                    total3 = VAT + units_cost 
                    print('''Appliance = {0}\nUnits= {1}Units per month\nService fee = UGX {2}\nVAT = UGX {3}\nTotal = UGX {4}'''.format (appliance,units_consumed,service_fee,VAT,total3)) 


                elif appliance == 4:
                    appliance = 'Flat iron'
                    use = float(input('ENTER NUMBER OF APPLIANCES : '))

                    minutes = float(input('ENTER NUMBER OF MINUTES   WHEN IN USE: '))
                    def usage(use,minutes):
                        unit_cal3= use*1000*minutes/60*30/1000
                        return unit_cal3
                    units_consumed = usage(use,minutes)
                    units_cost = usage(use,minutes)*580 
                    service_fee = 3360
                    VAT = units_cost*18/100 
                    total4 = VAT + units_cost 
                    print('''Appliance = {0}\nUnits= {1}Units per month\nService fee = UGX {2}\nVAT = UGX {3}\nTotal = UGX {4}'''.format (appliance,units_consumed,service_fee,VAT,total4)) 


                elif appliance == 5:
                    appliance = 'Fridge'
                    use = float(input('ENTER NUMBER OF APPLIANCES : '))
                    hours = float(input('ENTER NUMBER OF HOURS WHEN IN USE: '))
                    def usage(use,hours):
                        unit_cal4 = use*800*hours*30/1000
                        return unit_cal4
                    units_consumed = usage(use,hours)
                    units_cost = usage(use,hours)*580 
                    service_fee = 3360
                    VAT = units_cost*18/100 
                    total5 = VAT + units_cost 
                    print('''Appliance = {0}\n Units= {1}Units per month\nService fee = UGX {2}\nVAT = UGX {3}\nTotal = UGX {4}'''.format (appliance,units_consumed,service_fee,VAT,total5)) 


                

                elif appliance == 6:
                    appliance = 'Phone charger'
                    use = float(input('ENTER NUMBER OF APPLIANCES : '))
                    hours = float(input('ENTER NUMBER OF HOURS WHEN IN USE: '))
                    def usage(use,hours):
                        unit_cal5 = use*6*hours*30/1000
                        return unit_cal5
                    units_consumed = usage(use,hours)
                    units_cost = usage(use,hours)*580 
                    service_fee = 3360
                    VAT = units_cost*18/100 
                    total6 = VAT + units_cost 
                    print('''Appliance = {0}\n Units= {1}Units per month\nService fee = UGX {2}\nVAT = UGX {3}\nTotal = UGX {4}'''.format (appliance,units_consumed,service_fee,VAT,total6)) 


                elif appliance == 7:
                    appliance = 'TV'
                    use = float(input('ENTER NUMBER OF APPLIANCES : '))
                    hours = float(input('ENTER NUMBER OF HOURS WHEN IN USE: '))
                    def usage(use,hours):
                        unit_cal6 = use*60*hours*30/1000
                        return unit_cal6
                    units_consumed = usage(use,hours)
                    units_cost = usage(use,hours)*580 
                    service_fee = 3360
                    VAT = units_cost*18/100 
                    total7 = VAT + units_cost 
                    print('''Appliance = {0}\nUnits= {1}Units per month\nService fee = UGX {2}\nVAT = UGX {3}\nTotal = UGX {4}'''.format (appliance,units_consumed,service_fee,VAT,total7)) 


                elif appliance == 8:
                    appliance = 'Water heater'
                    use = float(input('ENTER NUMBER OF APPLIANCES : '))
                    hours = float(input('ENTER NUMBER OF HOURS WHEN IN USE: '))
                    def usage(use,hours):
                        unit_cal7 = use*2500*hours*30/1000
                        return unit_cal7
                    units_consumed = usage(use,hours)
                    units_cost = usage(use,hours)*580 
                    service_fee = 3360
                    VAT = units_cost*18/100 
                    total8 = VAT + units_cost 
                    print('''Appliance = {0}\nUnits= {1}Units per month\nService fee = UGX {2}\nVAT = UGX {3}\nTotal = UGX {4}'''.format (appliance,units_consumed,service_fee,VAT,total8)) 

                elif appliance == 9 :
                    appliance = 'Woofer'
                    use = float(input('ENTER NUMBER OF APPLIANCES : '))
                    hours = float(input('ENTER NUMBER OF HOURS WHEN IN USE: '))
                    def usage(use,hours):
                        unit_cal8 = use*50*hours*30/1000
                        return unit_cal8
                    units_consumed = usage(use,hours)
                    units_cost = usage(use,hours)*580 
                    service_fee = 3360
                    VAT = units_cost*18/100 
                    total9 = VAT + units_cost 
                    print('''Appliance = {0}\nUnits= {1}Units per month\nService fee = UGX {2}\nVAT = UGX {3}\nTotal = UGX {4}'''.format (appliance,units_consumed,service_fee,VAT,total9)) 
                elif appliance == 10:
                    appliance = input('ENTER NAME OF APPLIANCE: ')
                    use = float(input('ENTER NUMBER OF APPLIANCES : '))
                    hours = float(input('ENTER NUMBER OF HOURS WHEN IN USE: '))
                    watts = float(input('ENTER NUMBER OF WATTS CONSUMED: '))
                    def usage(use,hours):
                        unit_cal8 = use*watts*hours*30/1000
                        return unit_cal8
                    units_consumed = usage(use,hours)
                    units_cost = usage(use,hours)*580 
                    service_fee = 3360
                    VAT = units_cost*18/100 
                    total9 = VAT + units_cost 
                    
                elif appliance == 0 :
                    total_11 = total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10
                    print('Your total monthly expenditure is: UGX ',total_11 +3360)
                    print('THANK YOU, FOR USING PENNY ELECTRONICS!')
                    
                    break 
                else:
                    print('INVALID INPUT!TRY AGAIN')            
                            
    
    
    elif answer == 3:
       print('SORRY CUSTOMER, SERVICE NOT YET UPDATED')         
       pass       
    elif answer == 4:
        savings = saving/100*money
        total_44 = savings
        print('YOU SAVED; UGX ',savings)
    elif answer == 5:
        clothes1 = items = 0
        for t in range(4):
            print('''OTHER ITEMS:
                1.CLOTHES
                2.OTHER
                0.EXIT''')
            answer_2 = int(input('ENTER CHOICE: '))
            if answer_2 == 1:
                clothes1= int(input('ENTER AMOUNT SPENT ON CLOTHES: '))
            elif  answer_2 ==2:
                other = input('ENTER NAME OF OTHER:')
                items = int(input('ENTER AMOUNT SPENT ON {}: '.format(other)))
                
            elif answer_2 == 0:
                total_55 = clothes1 + items
                print('TOTAL; UGX',total_55)
                break
    elif answer == 0:
        tots = float(total_55 + total_11 + total_22 + total_33 +total_44)
        spent = money - tots 
        if spent<0:
            print("{} YOU ARE SPENDING MONEY BEYOND YOUR GIVEN BUGDET/SALARY.")
        
        print(''' {0},YOU'RE TOTAL EXPIDITURE IS: UGX{1} '''.format(name,tots))
        print('''{0}, YOU ARE ESTIMATED TO REMAIN WITH: UGX{1}'''.format(name,spent))
       
        if spent <= 0:
            if total_11>total_22 or total_11>total_33 or total_11>total_44 or total_11>total_55:
                
                print('PLEASE MINIMIZE HOW MUCH ELECTRICITY YOU ARE USING TO AVOID OVER SPENDING!')
   
            elif total_22>total_11 or total_22>total_33 or total_22>total_44 or total_22>total_55:
                print('PLEASE MINIMIZE YOUR GROCERY CONSUMPTION TO REDUCE ON THE MONEY SPENT ON THEM!')
                
            elif total_33>total_11 or total_33>total_22 or total_33>total_44 or total_33>total_55:
                print('PLEASE MINIMIZE YOUR GROCERY CONSUMPTION TO REDUCE ON THE MONEY SPENT ON THEM!')
            elif total_44>total_11 or total_44>total_22 or total_44>total_33 or total_44>total_55:
                print('PLEASE MINIMIZE YOUR GROCERY CONSUMPTION TO REDUCE ON THE MONEY SPENT ON THEM!')
            elif total_55>total_11 or total_55>total_22 or total_55>total_33 or total_55>total_44:
                print('PLEASE MINIMIZE YOUR GROCERY CONSUMPTION TO REDUCE ON THE MONEY SPENT ON THEM!')
            
                
                        
        break
    else:
        print('INVALID INPUT!TRY AGAIN')            
                
print('THANKS FOR USING ECORENE!SEE YOU NEXT TIME!.')  




                        
                            
                    
                        
                    
                        
                    
                    
                        
                    
                    
                
                
