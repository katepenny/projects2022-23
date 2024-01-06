print('WELCOME TO PENNYELECTRICS')
names = input('ENTER USERNAME:')
passWORD = input('ENTER YOUR PASSWORD : ')
if passWORD == 'mickey22':
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
     0.Exit''')

    total1 = total2 =  total3 = total4= total5= total6 = total7 = total8 = total9 = 0
    

    for x in range(11):
        appliance = int(input('SELECT APPLIANCE : '))
        
        if appliance == 1:
            appliance = 'Bulb'
            use= int(input('ENTER NUMBER OF APPLIANCES : '))
            hours = int(input('ENTER NUMBER OF HOURS WHEN IN USE: '))
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

            use = int(input('ENTER NUMBER OF APPLIANCES : '))
            hours = int(input('ENTER NUMBER OF HOURS WHEN IN USE: '))
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
            use = int(input('ENTER NUMBER OF APPLIANCES : '))
            hours = int(input('ENTER NUMBER OF HOURS WHEN IN USE: '))
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
            use = int(input('ENTER NUMBER OF APPLIANCES : '))
            hours = int(input('ENTER NUMBER OF HOURS WHEN IN USE: '))
            def usage(use,hours):
                unit_cal3= use*1000*hours*30/1000
                return unit_cal3
            units_consumed = usage(use,hours)
            units_cost = usage(use,hours)*580 
            service_fee = 3360
            VAT = units_cost*18/100 
            total4 = VAT + units_cost 
            print('''Appliance = {0}\nUnits= {1}Units per month\nService fee = UGX {2}\nVAT = UGX {3}\nTotal = UGX {4}'''.format (appliance,units_consumed,service_fee,VAT,total4)) 


        elif appliance == 5:
            appliance = 'Fridge'
            use = int(input('ENTER NUMBER OF APPLIANCES : '))
            hours = int(input('ENTER NUMBER OF HOURS WHEN IN USE: '))
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
            use = int(input('ENTER NUMBER OF APPLIANCES : '))
            hours = int(input('ENTER NUMBER OF HOURS WHEN IN USE: '))
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
            use = int(input('ENTER NUMBER OF APPLIANCES : '))
            hours = int(input('ENTER NUMBER OF HOURS WHEN IN USE: '))
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
            use = int(input('ENTER NUMBER OF APPLIANCES : '))
            hours = int(input('ENTER NUMBER OF HOURS WHEN IN USE: '))
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
            use = int(input('ENTER NUMBER OF APPLIANCES : '))
            hours = int(input('ENTER NUMBER OF HOURS WHEN IN USE: '))
            def usage(use,hours):
                unit_cal8 = use*50*hours*30/1000
                return unit_cal8
            units_consumed = usage(use,hours)
            units_cost = usage(use,hours)*580 
            service_fee = 3360
            VAT = units_cost*18/100 
            total9 = VAT + units_cost 
            print('''Appliance = {0}\nUnits= {1}Units per month\nService fee = UGX {2}\nVAT = UGX {3}\nTotal = UGX {4}'''.format (appliance,units_consumed,service_fee,VAT,total9)) 

        elif appliance == 0 :
           total = total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 
           print('Your total monthly expenditure is : UGX ',total +3360)
           print('THANK YOU, FOR USING PENNY ELECTRONICS!')
           
           break 
        
       



