print('WELCOME TO PENNY DONATIONS!')
from datetime import date
today = date.today()

account = input('ENTER YOUR USERNAME: ')
pas = True

if account == 'kate penny':
 while pas == True: 
   
    

    password = input('ENTER PASSWORD: ')
    
    if password == 'mickey22':
        balance = 2300000
        print('YOUR LOCATION: MUKONO DISTRICT')
        
        print('''WOULD YOU LIKE TO :
            1.Donate 
            2.Seek Assistance''')
        choice = int(input('ENTER CHOICE: '))
        if choice == 1:
            print('''DONATE TO:
                1.Food Bank
                2.Children's home
                3.Community Fundraiser''')
            donate = int(input('ENTER CHOICE: '))
            if donate == 1:
                print('''ARE YOU DONATING IN TERMS OF :
                1.Food Items
                2.Money''')
                Don = int(input('ENTER CHOICE: '))
                if Don == 1:
                    print('''Send items:
                        1.In person
                        2.Pick up and Delivery''')
                    send = int(input('ENTER CHOICE: '))
                    if send == 1 :
                        print('''FOOD BANK IN MUKONO:
                            1.Ntawo Food Bank
                            2.Kigunga Food Bank''')
                        fbank =int(input('ENTER CHOICE: '))
                        if fbank == 1:
                            print('LOCATION : Ntawo Food Bank is located 5km off Ntawo Road opposite Green Bank.\n CONTACT:0785432465/0706538374 For further directions. ')
                        elif fbank == 2:
                            print('LOCATION : kigunga Food Bank is located opposite Ciaro Hosptial.\n CONTACT:0764434564/0704566543 For further directions.')
                    elif send == 2:
                            print('For Pickup and Delivery:\nCONTACT:075432345/07684932\nTo reach out to our faithful service providers. ')
                elif Don == 2:

                    mula = int(input('ENTER AMOUNT: ')) 
                    bal = balance - mula
                    print('''FOOD BANK IN MUKONO:
                            1.Nakabago Food Bank
                            2.Kigunga Food Bank''')
                    fbank =int(input('ENTER CHOICE: '))
                    if fbank == 1:
                        print('You have donated UGX{0} to Ntawo FB\nDate:{1}\nAccount Balance:UGX{2}'.format(mula,today,bal))
                    elif fbank == 2:
                        print('You have donated UGX{0} to kigunga FB\nDate:{1}\nAccount Balance:UGX{2}'.format(mula,today,bal))
            elif donate == 2:
                
                print('''ARE YOU DONATING IN TERMS OF :
                1.Food Items or Clothes
                2.Money
                ''')
                Don = int(input('ENTER CHOICE: '))
                if Don == 1 :
                    print('''Send items:
                        1.In person
                        2.Pick up and Delivery
                        3.post office''')
                    send = int(input('ENTER CHOICE: '))
                    if send == 1 :
                        print('''ORPHANAGES IN MUKONO:
                            1.Samuel's kids Ministeries
                            2.Graben Orphanage Foundation
                            3.Noah's Ark Children's Ministries

                            ''')
                        fbank =int(input('ENTER CHOICE: '))
                        if fbank == 1:
                            print('''LOCATION :Samuel's kids Ministeries is located along Kayunga Road opposite Green Bank.\nCONTACT:0787247587\nFor further directions. ''')
                        elif fbank == 2:
                            print('LOCATION :Graben Orphanage Foundation is located in Ntawo Ward.\n CONTACT:0785737474 For further directions.')
                        elif fbank == 3:
                            print('''LOCATION :Noah's Ark Children's Ministries is located in Takkajjunge/Nsambwe.\n CONTACT:077481142 For further directions.''')
                        
                    elif send == 2:
                            print('For Pickup and Delivery:\nCONTACT:075432345/07684932\nTo reach out to our faithful service providers. ')
                    
                    elif send ==3:
                        print('''
                                    1.Samuel's kids Ministeries
                                    2.Graben Orphanage Foundation
                                    3.Noah's Ark Children's Ministries ''')
                        fbank =int(input('ENTER CHOICE: '))
                        if fbank == 3:
                            print('''POSTAL ADDRESS: Noah's Ark Children's Ministries P.O 335,Mukono.''')
                        elif fbank == 2:
                            print('''POST OFFICE ADDRESS:Graben Orphanage Foundation P.O 844,Mukono.''')
                        elif fbank == 1:
                            print('''POST OFFICE ADDRESS:Samuel's kids Ministeries P.O 878,Mukono.''')
                elif Don == 2:

                    mula = int(input('ENTER AMOUNT: ')) 
                    bal = balance - mula
                    print('''   
                                1.Samuel's kids Ministeries
                                2.Graben Orphanage Foundation
                                3.Noah's Ark Children's Ministries ''')
                    fbank =int(input('ENTER CHOICE: '))
                    if fbank == 1:
                        print('''You have donated UGX{0} to Samuel's kids Ministries\nDate:{1}\nAccount Balance:UGX{2}'''.format(mula,today,bal))
                    elif fbank == 2:
                        
                        print('You have donated UGX{0} to Graben Orphanage Foundation \nDate:{1}\nAccount Balance:UGX{2}'.format(mula,today,bal))
                    elif fbank == 3:
                        print('''You have donated UGX{0} to Noah's Ark Children's Ministries \nDate:{1}\nAccount Balance:UGX{2}'''.format(mula,today,bal))
                
            elif donate ==3:
                print('''SELECT ONE:
                        1.Volunteer
                        2.Donate''')
                vol = int(input('ENTER CHOICE: '))
                if vol == 1:
                    print('''COMMUNITY FUNDRAISERS  IN MUKONO:
                        1.Ntawo single Mother's Fund
                        2.Nasuuti School for the Blind fund
                        3.Mukono SDA church Fund''')
                    join = int(input('ENTER CHOICE: '))
                    if join ==1:
                        print('''The Ntawo Single Mothers fund is a fundraiser to assist struggling single mothers
                        to provide for their children basic needs and their own.
                                Volunteers can help through:
                        1.Gathering items that can assist mother/children
                        2.Spreading the message
                        3.Participate in the visiting of these mothers
                                To volunteer please contact: 0768003876/078654374
                                    ''')

                    elif join ==2:
                        print('''Nasuuti School for the Blind fund is a fundraiser being carried out by the
                        community to help improve and advance on the school's welfare.
                                Any possible type of assistance by volunteers is accepted
                                please contact :0760975775/0876433456/0707654435''')

                    elif join == 3:
                        print('''Mukono SDA church Fund is a fudraiser being carried out by the church 
                        to assist struggling and less advantaged families .
                                    This fundraiser is being carried out through the sale of
                        notebooks made by the church.
                                    Volunteers can help through participating in the sale of books
                                    TO Volunteer contact 0786445679/0786435688''')

                elif vol == 2:
                    x = int(input('Enter Amount: '))
                    bal = balance - x
                    
                    print('''COMMUNITY FUNDRAISERS  IN MUKONO:
                        1.Ntawo single Mother's Fund
                        2.Nasuuti School for the Blind fund
                        3.Mukono SDA church Fund''')

                    dina = int(input('ENTER CHOICE:'))
                    y ='Ntawo single Mothers Fund'
                    r ='Nasuuti School for the Blind fund'
                    p ='Mukono SDA church Fund'
                    if dina ==1:
                        
                        print ('''You have donated UGX{0} to {3}\nDate:{1}\nBalance:{2}'''.format(x,today,bal,y))
                        
                    elif dina ==2:
                        print ('''You have donated UGX{0} to {3}\nDate:{1}\nBalance:{2}'''.format(x,today,bal,r))
                        
                    elif dina == 3:
                        print ('''You have donated UGX{0} to {3}\nDate:{1}\nBalance:{2}'''.format(x,today,bal,p))
        elif choice == 2:
            print('''ARE  YOU :
                1.Organisation/school
                2.Individual
                ''')
            assist = int(input('ENTER CHOICE: '))
            if assist == 1:
                NAMER = input('ENTER NAMES OF ORGANISATION/SCHOOL: ')
                EMAIL = input('ENTER EMAIL OF ORGANISATION/SCHOOL: ') 
                LOC =  input('ENTER LOCATION OF ORGANISATION?SCHOOL: ')
                print('''WHAT TYPE OF ASSISTANCE DO YOU SEEK:
                        1. Financial assistance
                        2. Housing
                        3. Other''')                                                          
                fine = int(input('ENTER CHOICE: '))
                if fine == 1:
                    
                    print('''HERE IS A LIST OF SPONSORS IN YOUR AREA THAT YOU CAN REACH OUT TO:
                            1.Helping hands
                            2.Jill and Co.
                            3.Nakabago Women Association
                            4.Nasuuti Children Fund
                            5.kigunga healing Hands
                            6.Seeta Community Fund''')
                    spon = int(input('SELECT A SPONSER: '))
                    mon = int(input('ENTER AMOUNT NEEDED: '))
                    print('THANK YOU,{}.REQUEST HAS BEEN FORWARDED TO THE SPONSER.PLEASE WAIT FOR A RESPONSE IN YOUR EMAIL'.format(NAMER))
                    print('THANK YOU FOR USING PENN DONATIONS! ')
                elif fine == 3 :
                    print('''
                        THIS OPTION INCLUDES:
                           1. Clothes
                           2. food items
                           3. School Material
                        ''')
                    fodie = int(input('ENTER CHOICE:'))
                    if fodie == 1 or 2 or 3:
                
                        print('''AVAILABLE SPONSERS/ORGANISATIONS:
                                1.Helping hands
                                2.Jill and Co.
                                3.Nakabago Women Association
                                4.Nasuuti Children Fund
                                5.kigunga healing Hands
                                6.Fungs charity clothing
                                7.Ntawo Food Bank
                                8.Kigunga Food Bank
                                9.Mukono Helping hands
                                10.Seeta Community Fund''')
                        spon = int(input('ENTER CHOICE: '))
                        print('THANK YOU,{}.REQUEST HAS BEEN FORWARDED TO THE SPONSER.PLEASE WAIT FOR A RESPONSE IN YOUR EMAIL'.format(NAMER))
                elif 2:
                    print('''AVAILABLE SPONSERS:
                            1. Namawojolo Housing Assistants
                            2. Seeta Housing Aid
                            3. 1.Helping hands
                            2. Jill and Co.
                            3. Nakabago Women Association
                            4. Nasuuti Children Fund
                            5. kigunga healing Hands''')
                    on = input('ENTER CHOICE: ')
                    print('THANK YOU,{}.REQUEST HAS BEEN FORWARDED TO THE SPONSER.PLEASE WAIT FOR A RESPONSE IN YOUR EMAIL'.format(NAMER))
            elif assist == 2:
                occ = input('ENTER FULL NAMES: ')
                age = int(input('ENTER YOUR AGE: '))
                gender = input('ENTER YOUR GENDER (F/M): ')
                contact = int(input('ENTER CONTACT: '))
                if age<=18:
                    if gender == 'F':
                        print('''HERE IS A LIST OF COMPATIBLE ORGANISATIONS:
                            1. Nasuuti Children Fund
                            2. Kigunga healing Hands
                            3. Mukono children Fund
                            4. Seeta Girls community
                            5. Global Girls Association
                            
                            ''')
                        chooce = int(input('ENTER CHOICE:'))
                        print('Thank you, {0} .You Shall Be Contacted By The Selected Organisation in a bit. '.format(occ))
                    elif gender == 'M':
                        print('''HERE IS A LIST OF COMPATIBLE ORGANISATIONS:
                            1. Nasuuti Children Fund
                            2. Kigunga healing Hands
                            3. Mukono children Fund
                            4. Seeta boys community
                            5. Global boys Association
                            ''')
                        chooce = int(input('ENTER CHOICE:'))
                        print('Thank you, {0} .You Shall Be Contacted By The Selected Organisation in a bit. '.format(occ))
                    print('THANK YOU FOR USING PENN DONATIONS!')

                elif age>=18:
                    
                    NAME = input('ENTER NAMES OF ORGANISATION/SCHOOL: ')
                    EMAIL = input('ENTER EMAIL OF ORGANISATION/SCHOOL: ') 
                    CONTACT = input('ENTER CONTACT')
                    LOC =  input('ENTER LOCATION OF ORGANISATION?SCHOOL: ')
                    print('''WHAT TYPE OF ASSISTANCE DO YOU SEEK:
                        1. Financial assistance
                        2. Housing
                        3. Other''')                                                          
                    fine = int(input('ENTER CHOICE: '))
                    if fine == 1:
                        
                        print('''HERE IS A LIST OF SPONSORS IN YOUR AREA THAT YOU CAN REACH OUT TO:
                            1.Helping hands
                            2.Jill and Co.
                            3.Nakabago Women Association
                            4.Nasuuti Children Fund
                            5.kigunga healing Hands
                            6.Seeta Community Fund
                            7.KOlaso Helps 
                            8.Mukono Helping Hands''')
                        spon = int(input('SELECT A SPONSER: '))
                        mon = int(input('ENTER AMOUNT NEEDED: '))
                        print('REQUEST HAS BEEN FORWARDED TO THE SPONSER.PLEASE WAIT FOR A RESPONSE IN YOUR EMAIL')
                    elif fine == 3 :
                        print('''
                                1.Clothes
                                2.food items
                                3.School Material
                            ''')
                        
                    
                        print('''AVAILABLE SPONSERS/ORGANISATIONS:
                                1.Helping hands
                                2.Jill and Co.
                                3.Nakabago Women Association
                                4.Nasuuti Children Fund
                                5.kigunga healing Hands
                                6.Fungs charity clothing
                                7.Ntawo Food Bank
                                8.Kigunga Food Bank
                                9.Mukono Helping hands
                                10.Seeta Community Fund
                                11.Mukono Mens Fund
                                10.Kigaga Mens fund''')
                        spon = int(input('ENTER CHOICE: '))
                        print('YOUR REQUEST HAS BEEN SENT TO THE SPONSER/ORGANISATION.PLEASE WAIT FOR A RESPONSE!')
                    elif 2:
                        print('''AVAILABLE SPONSERS:
                                1. Namawojolo Housing Assistants
                                2. Seeta Housing Aid
                                3. 1.Helping hands
                                2. Jill and Co.
                                3. Nakabago Women Association
                                4. Nasuuti Children Fund
                                5. kigunga healing Hands
                                11.Mukono Mens Fund
                                10.Kigaga Mens fund''')
                        on = input('ENTER CHOICE: ')
                        print('YOUR REQUEST HAS BEEN SENT TO THE SPONSER/ORGANISATION.PLEASE  WAIT FOR A RESPONSE!')
                
            
                    print('THANK YOU FOR USING PENN DONATIONS! ')
        pas == False
        
    else:
     print('TRY AGAIN!')                                 
else:
    print('Your account is not available in Penn Donations.')                          