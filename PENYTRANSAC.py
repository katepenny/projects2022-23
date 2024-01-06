print('HELLO CUSTOMER! WELCOME TO PENYTRANSAC')
from datetime import date
today = date.today()
paa = True



while paa == True:

 password = input('ENTER YOUR PASSWORD : ')
 if password == 'PassWord12345':
    user = input('CHOOSE A NETWORK (MTN / AIRTEL) : ')
    if user == 'MTN' or 'mtn':
        balance = 1470000
        print ('WELCOME TO MTN MOBILE MONEY!')
        print('''PLEASE CHOOSE ONE :  
                    1.Send Money
                    2.Withdraw Money''')
        mtn = int(input('ENTER RESPONSE : '))
        if mtn == 1:
            print('''SEND MONEY : Would you like to send to ;
                        1.MTN number 
                        2.AIRTEL number OR Other 
                        3.International number''')
            sending = int(input('ENTER RESPONSE : '))
            
            if sending == 1 :
                MT =int(input('ENTER NUMBER : '))
            
                mN = int(input('ENTER AMOUNT : '))
                balance = balance - mN
                
                def myrange(n):
                    
                    if n in range(0,60000):
                        print( 'SENT UGX {0} to {1}.\n Fee UGX 500.\n Bal UGX {2}.\n Date:{3}',format(money,mN,(balance -500),today ) )
                    elif n in range(60001,5000000):
                        print( 'SENT UGX {0} to {1}.\n Fee UGX 500.\n Bal UGX {2}.\n Date:{3}',format(money,mN,(balance -1000),today ) )
                    else:
                        
                        print('AMOUNT IS BEYOND THE LIMIT')  
                myrange(mN)
                
            elif sending == 3:

                print('''CHOOSE A COUNTRY:
                                1.Cote D’Ivoire
                                2.Ghana
                                3.Nigeria, 
                                4.Liberia, 
                                5.Guinea Bissau, 
                                6.Guinea, 
                                7.Rwanda, 
                                8.Swaziland, 
                                9.Benin, 
                                10.Yemen, 
                                11.Cameroon, 
                                12.Ivory Coast, 
                                13.South Africa, 
                                14. Zambia''')
                x = int(input('ENTER CHOICE : '))
                

                INTE =int(input('ENTER NUMBER WITH COUNTRY CODE : '))
                

                intmon = int(input('ENTER AMOUNT : '))
                balance = balance - intmon
                def myrange(n):
                 

                    if n in range(0,60000):
                        print( 'SENT UGX {0} to {1}.\n Fee UGX 500.\n Bal UGX {2}.\n Date:{3}'.format(intmon,INTE,(balance -500),today ) )
                    elif n in range(60001,5000000):
                        print( 'SENT UGX {0} to {1}.\n Fee UGX 500.\n Bal UGX {2}.\n Date:{3}'.format(intmon,INTE,(balance -1000),today ) )
                    else:
                        print('AMOUNT IS BEYOND THE LIMIT')                        

                        
            
                        
                myrange(intmon)
            
            elif sending == 2:
                at =int(input('ENTER NUMBER : '))
            
                AT= int(input('ENTER AMOUNT : '))
                balance = balance - AT
                def myrange(n):
                    if n in range(0,60000):
                        print( 'SENT UGX {0} to {1}.\n Fee UGX 500.\n Bal UGX {2}.\n Date:{3}'.format(AT,at,(balance -500),today ) )
                    elif n in range(60001,5000000):
                        print( 'SENT UGX {0} to {1}.\n Fee UGX 500.\n Bal UGX {2}.\n Date:{3}'.format(AT,at,(balance -1000),today ) )
                    else:
                        print('AMOUNT IS BEYOND THE LIMIT')                        

                        
                myrange(AT)
        elif mtn ==2:
            mula = int(input('ENTER AMOUNT:'))
            tax = 0.005*mula
            
            balance = balance - mula - tax 

            def n_range(v):
                    
                    if v in range(0,2500):
                       print( 'You have withdrawn UGX {0} on {3}.\nFee:UGX 330 \nTax: UGX {1} \nNew Balance: UGX {2}. \nThank you for choosing MTN'.format(v,tax,(balance - 330),today ))
                    elif v in range(2501,5000):
                       print( 'You have withdrawn UGX {0} on  {3}.\nFee:UGX 440 \nTax: UGX {1} \nNew Balance: UGX {2}. \nThank you for choosing MTN'.format(v,tax,(balance - 440),today ))
                    elif v in range(5001,15000):
                       print( 'You have withdrawn UGX {0} on  {3}.\nFee:UGX 700 \nTax: UGX {1} \nNew Balance: UGX {2}. \nThank you for choosing MTN'.format(v,tax,(balance - 700),today))
                    elif v in range(15001,30000):
                       print( 'You have withdrawn UGX {0} on  {3}.\nFee:UGX 880 \nTax: UGX {1} \nNew Balance: UGX {2}. \nThank you for choosing MTN'.format(v,tax,(balance - 880),today ))
                    elif v in range(30000,45000):
                       print( 'You have withdrawn UGX {0} on  {3}.\nFee:UGX 1500 \nTax: UGX {1} \nNew Balance: UGX {2}. \nThank you for choosing MTN'.format(v,tax,(balance - 1500),today ))
                    elif v in range(30000,45000):
                       print( 'You have withdrawn UGX {0} on  {3}.\nFee:UGX 1925 \nTax: UGX {1} \nNew Balance: UGX {2}. \nThank you for choosing MTN'.format(v,tax,(balance - 1925),today ))
                    
                    elif v in range(45001,60000):
                    
                       print( 'You have withdrawn UGX {0} on  {3}.\nFee:UGX 7000 \nTax: UGX {1} \nNew Balance: UGX {2}. \nThank you for choosing MTN'.format(v,tax,(balance - 7000),today ))
                    elif v in range(60001,5000000):
                       print( 'You have withdrawn UGX {0} on  {3}.\nFee:UGX 12500 \nTax: UGX {1} \nNew Balance: UGX {2}. \nThank you for choosing MTN'.format(v,tax,(balance - 12500),today ))
                    
                
                
            n_range(mula)
            
        print('THANK YOU FOR USING MTN!')       


                        
                        




        


    elif user == 'AIRTEL' or user == 'airtel':
        
        print ('WELCOME TO AIRTEL MONEY!')
        mymula = 2000000
        print('''PLEASE CHOOSE ONE :  
                    1.Send Money
                    2.Withdraw Money''')
        airtel = int(input('ENTER RESPONSE : '))
        if airtel == 1:
            print('''SEND MONEY : Would you like to send to ;
                        1.Airtel number
                        2.MTN number 
                        3.International number''')
            send = int(input('ENTER RESPONSE : '))
            if send == 1:
                ART =int(input('ENTER NUMBER : '))
                
                money = int(input('ENTER AMOUNT : '))
                bal = mymula - money 
                def myrange(n):
                    if n in range(0,60000):
                        print( 'SENT UGX {0} to {1}.\n Fee UGX 500.\n Bal UGX {2}.\n Date:{3}'.format(money,ART,(bal -500),today ) )
                    elif n in range(60001,5000000):
                        print( 'SENT UGX {0} to {1}.\n Fee UGX 500.\n Bal UGX {2}.\n Date:{3}'.format(money,ART,(bal -1000),today ) )
                        print('AMOUNT IS BEYOND THE LIMIT')
                        
                myrange(money)
            elif send ==3:
            

                print('''CHOOSE A COUNTRY:
                                1.Cote D’Ivoire
                                2.Ghana
                                3.Nigeria, 
                                4.Liberia, 
                                5.Guinea Bissau, 
                                6.Guinea, 
                                7.Rwanda, 
                                8.Swaziland, 
                                9.Benin, 
                                10.Yemen, 
                                11.Cameroon, 
                                12.Ivory Coast, 
                                13.South Africa, 
                                14. Zambia''')
                x = int(input('ENTER CHOICE : '))
                

                INTE =int(input('ENTER NUMBER WITH COUNTRY CODE : '))
                

                intmon = int(input('ENTER AMOUNT : '))
                

                def myrange(n):
                    mymula = mymula - intmon
                  
                    if n in range(0,60000):
                        print( 'SENT UGX {0} to {1}.\n Fee UGX 500.\n Bal UGX {2}.\n Date:{3}'.format(money,intmon,(bal -500),today ) )
                    elif n in range(60001,5000000):
                        print( 'SENT UGX {0} to {1}.\n Fee UGX 500.\n Bal UGX {2}.\n Date:{3}'.format(money,intmon,(bal -1000),today ) )
                        print('AMOUNT IS BEYOND THE LIMIT')
                        
                
                myrange(intmon)
                print('THANK YOU FOR USING AIRTEL!')
            
            elif send == 2:
                mula = int(input('ENTER AMOUNT:'))
                tax = 0.005*mymula
                
                balance = mymula - mula - tax 

                def n_range(v):
                    
                    if v in range(0,2500):
                       print( 'You have withdrawn UGX {0} on {3}.\nFee:UGX 330 \nTax: UGX {1} \nNew Balance: UGX {2}. \nThank you for choosing MTN'.format(v,tax,(balance - 330),today ))
                    elif v in range(2501,5000):
                       print( 'You have withdrawn UGX {0} on  {3}.\nFee:UGX 440 \nTax: UGX {1} \nNew Balance: UGX {2}. \nThank you for choosing MTN'.format(v,tax,(balance - 440),today ))
                    elif v in range(5001,15000):
                       print( 'You have withdrawn UGX {0} on  {3}.\nFee:UGX 700 \nTax: UGX {1} \nNew Balance: UGX {2}. \nThank you for choosing AIRTEL'.format(v,tax,(balance - 700),today))
                    elif v in range(15001,30000):
                       print( 'You have withdrawn UGX {0} on  {3}.\nFee:UGX 880 \nTax: UGX {1} \nNew Balance: UGX {2}. \nThank you for choosing AIRTEL'.format(v,tax,(balance - 880),today ))
                    elif v in range(30000,45000):
                       print( 'You have withdrawn UGX {0} on  {3}.\nFee:UGX 1500 \nTax: UGX {1} \nNew Balance: UGX {2}. \nThank you for choosing AIRTEL'.format(v,tax,(balance - 1500),today ))
                    elif v in range(30000,45000):
                       print( 'You have withdrawn UGX {0} on  {3}.\nFee:UGX 1925 \nTax: UGX {1} \nNew Balance: UGX {2}. \nThank you for choosing AIRTEL'.format(v,tax,(balance - 1925),today ))
                    
                    elif v in range(45001,60000):
                    
                       print( 'You have withdrawn UGX {0} on  {3}.\nFee:UGX 7000 \nTax: UGX {1} \nNew Balance: UGX {2}. \nThank you for choosing AIRTEL'.format(v,tax,(balance - 7000),today ))
                    elif v in range(60001,5000000):
                       print( 'You have withdrawn UGX {0} on  {3}.\nFee:UGX 12500 \nTax: UGX {1} \nNew Balance: UGX {2}. \nThank you for choosing AIRTEL'.format(v,tax,(balance - 12500),today ))
                    
                
                
                n_range(mula)
            
                

        print('THANK YOU FOR USING AIRTEL!')
    paa == False 
 else:
    print('TRY AGAIN!')
