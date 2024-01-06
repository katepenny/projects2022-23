
import webbrowser
from abc import ABC, abstractmethod

print('WELCOME TO LUCY RECYCLE!')

print('Get money back from recyclable wastes')


class Rubbish(ABC):

    @abstractmethod
    def call_company(self):
        call = input(
            'WOULD YOU LIKE TO CONTACT A COMPANY TO PICK UP RUBBISH?(YES/NO): ')
        if call == 'yes' or call == 'YES':

            print('COMPANY IS BEING CONTACTED.')
            for r in range(3):
                location = input('ENTER LOCATION: ')
                time = int(input('WOULD YOU LIKE TO\n1.LOOK AT THE SCHEDULED DATES FOR THE NEXT PICK UP IN YOUR AREA \n2.CONTACT COMPANY IMMEDIATELY AND SCHEDULE A DATE OF YOUR OWN PREFERENCE(CHARGES MAY APPLY)\n0.EXIT: '))
                while time == '':
                    print('TRY AGAIN!')
                    time = int(input('WOULD YOU LIKE TO\n1.LOOK AT THE SCHEDULED DATES FOR THE NEXT PICK UP IN YOUR AREA \n2.CONTACT COMPANY IMMEDIATELY AND SCHEDULE A DATE OF YOUR OWN PREFERENCE(CHARGES MAY APPLY)\n0.EXIT: '))

                if time == 1:
                    print(
                        f'NEXT PICK UP AROUND {location} WILL BE ON:\n 29/05/2023')
                elif time == 2:
                    webbrowser.open('https://www.google.com/search?q=' +
                                    'garbage collection companies near '+location)
                elif time == 0:
                    break
        else:
            print('NO PROBLEM\nTHANK YOU FOR USING LUCKY RECYCLE!\n')


class WasteManagement(Rubbish):

    def call_company(self):

        call = input(
            'WOULD YOU LIKE TO CONTACT A COMPANY TO PICK UP RUBBISH?(YES/NO): ')

        for r in range(3):
            if call == 'yes' or call == 'YES':

                print('COMPANY IS BEING CONTACTED.')

                location = input('ENTER LOCATION: ')
                time = int(input('WOULD YOU LIKE TO\n1.LOOK AT THE SCHEDULED DATES FOR THE NEXT PICK UP IN YOUR AREA \n2.CONTACT COMPANY IMMEDIATELY AND SCHEDULE A DATE OF YOUR OWN PREFERENCE(CHARGES MAY APPLY)\n0.EXIT: '))
                if time == 1:
                    print(
                        f'NEXT PICK UP AROUND {location} WILL BE ON:\n 29/05/2023')
                elif time == 2:
                    webbrowser.open('https://www.google.com/search?q=' +
                                    'garbage collection companies near '+location)
                elif time == 0:
                    break
        else:
            print('NO PROBLEM\nTHANK YOU FOR USING LUCKY RECYCLE!\n')

    def information(self):
        for x in range(4):
            srch = int(input(
                '\nWOULD YOU LIKE:\n1.VIDEO SEARCH\n2.GOOGLE SEARCH\n3.RECOMMENDED REFERENCE\n0.DONE \nENTER CHOICE: '))

            if srch == 1:
                yt = input('Search: ')
                webbrowser.open(
                    'https://www.youtube.com/results?search_query=' + yt)
            elif srch == 2:
                google = input('Search: ')
                webbrowser.open('https://www.google.com/search?q=' + google)
            elif srch == 3:
                webbrowser.open('https://www.youtube.com/watch?v=8krzjlHaGes')
            elif srch == 0:
                print('\nTHANK YOU FOR USING LUCKY RECYCLE!\n')
                break

    def sell(self):
        for x in range(6):
            print('Some materials can be resold after use instead of disposal\n1.Old furniture\n2.Clothes\n3.Kitchenware\n4.Shoes etc')
            web = int(input('HERE IS A NUMBER OF WEBSITES WHERE THESE ITEMS/MATERIALS CAN BE RESOLD.\nPLEASE SELECT ANY:\n1.FACEBOOK MARKET PLACE\n2.JIJI UGANDA.\n3.TTUNDA.COM\n4.REBUYDEAL\n0.EXIT'))
            if web == 1:
                webbrowser.open(
                    'https://www.facebook.com/marketplace/114935148521194/')
            elif web == 2:
                webbrowser.open('https://jiji.ug')
            elif web == 3:
                webbrowser.open('https://ttunda.com/')
            elif web == 4:
                webbrowser.open('https://www.rebuydeal.com/en')
            elif web == 0:
                print('Thank you for using our platform')
                break

    def donate(self):
        print('Many items can be donated to organisations instead of being thrown away')
        for r in range(6):
            print('''Here is a list of organisations where the items can be donated
                1.Love Uganda Foundation-Volunteer In Uganda-Orphanage
                2.Exodus care and charity home uganda
                3.Sanyu Babies Home
                4.Nsambya Babies Home
                0.Exist''')
            select = int(input('SELECT CHOICE:'))
            if select == 1:
                print('''Address: Plot 1490, After Kubbiri Roundabout, Gayaza -Kampala Rd, Kampala, Uganda

                    Phone: +256 772 633920''')
            elif select == 2:
                print('''Address: C6WP+5M7, Walukuba-Masese Rd, Jinja, Uganda

                    Phone: +256 706 168927''')
            elif select == 3:
                print('''Address: Plot 346, Albert Cook Rd, Kampala, Uganda

                    Phone: +256 788 162147''')

            elif select == 4:
                print(
                    '''Address: Nsambya-Ggaba Road Junction, Millenium House\nSuite 19-2nd Floor, Kampala, Uganda''')

            elif select == 0:
                print('\nTHANK YOU FOR USING LUCKY RECYCLE!\n')
                break


class Recyclable(WasteManagement):

    def __init__(self):
        super().__init__()

        self.__balance = 0

    def money_back(self, phone_no):
        moneyback1 = moneyback2 = moneyback3 = moneyback4 = moneyback5 = 0
        for choice in range(5):

            print('''You can be rewarded with money for the following recyclable items:
                1.scrapmetal
                2.plastic
                3.fabric
                4.shoes
                5.sandals
                0.exit
                ''')

            select2 = int(input('ENTER CHOICE: '))
            while select2 == '':
                select2 = int(input('ENTER CHOICE: '))

            if select2 == 1:
                weigh = int(input('ENTER ESTIMATED WEIGHT: '))
                while weigh == '':
                    weigh = int(input('ENTER ESTIMATED WEIGHT: '))
                if weigh >= 1:
                    moneyback1 = 1000*weigh
                    print('YOU EARNED UGX', moneyback1)
                else:
                    print('THE SCRAP SHOULD BE GREATER THAN ONE KG')
            elif select2 == 2:
                weigh2 = int(input('ENTER ESTIMATED WEIGHT: '))
                while weigh2 == '':
                    weigh2 = int(input('ENTER ESTIMATED WEIGHT: '))
                while weigh2 == '':
                    weigh2 = int(input('ENTER ESTIMATED WEIGHT: '))
                if weigh2 >= 1:
                    moneyback2 = 500*weigh2
                    print('YOU EARNED UGX', moneyback2)
                else:
                    print('THE PLASTICS SHOULD BE GREATER THAN ONE KG')
            elif select2 == 3:
                weigh3 = int(input('ENTER ESTIMATED WEIGHT: '))
                while weigh3 == '':
                    weigh3 = int(input('ENTER ESTIMATED WEIGHT: '))
                if weigh3 >= 5:
                    moneyback3 = 3000*weigh3
                    print('YOU EARNED UGX', moneyback3)
                else:
                    print('THE FABRIC SHOULD BE GREATER THAN FIVE KG')

            elif select2 == 4:
                weigh4 = int(input('ENTER ESTIMATED WEIGHT: '))
                while weigh4 == '':
                    weigh4 = int(input('ENTER ESTIMATED WEIGHT: '))
                if weigh4 >= 5:
                    moneyback4 = 2000*weigh4
                    print('YOU EARNED UGX', moneyback4)
                else:
                    print('THEY GREATER MUST BE THAN 4 PAIRS  ')

            elif select2 == 5:
                weigh5 = int(input('ENTER ESTIMATED WEIGHT: '))
                while weigh5 == int(''):
                    print('Invalid input')
                    weigh5 = int(input('ENTER ESTIMATED WEIGHT: '))

                if weigh5 >= 5:
                    moneyback5 = 1000*weigh5
                    print('YOU EARNED UGX', moneyback5)
                else:
                    print('THEY GREATER MUST BE THAN 4 PAIRS  ')
            elif select2 == 0:
                print('Thank you for using our platform')
                totals = moneyback1 + moneyback2 + moneyback3 + moneyback4 + moneyback5
                print('You have earned: UGX', totals)

                pin = int(input('ENTER PIN: '))
                print(f'YOU HAVE RECEIVED UGX{totals} FROM LUCKY RECYCLE')
                self.__balance += totals
                ('\nTHANK YOU FOR USING LUCKY RECYCLE!\n')
                break

    def account(self):
        print(f'Your account balance is UGX:{self.__balance}')

    def more_info(self):
        print('\nAnything that can serve as the source to make other things is called recyclable material.\n-The materials that can be recycled are:\nGlass, aluminum, plastic water bottles, metal scrap,\nDifferent kinds of paper, electronics computers, cellular phones\nKeyboards, batteries and other small electronic equipment\nTextile, wood, wire, cables, plastic product, rubber, etc.')


class Biodegradable(WasteManagement):
    def inform(self):
        inform = input(
            'WOULD YOU LIKE MORE INFORMATION ON BIODEGRADABLE MATERIAL/SUBSTANCES?(YES/NO):')
        if inform == 'yes' or 'YES':
            options = int(input('1.Video reference\n2.word reference'))
            while options == '':
                options = int(input('1.Video reference\n2.word reference'))

            if options == 1:
                webbrowser.open(
                    'https://www.youtube.com/watch?v=YeVLBkypPRU&t=135s')
            else:
                print('Biodegradable materials are those, which degrade or break down in a natural manner. \nIn other words, their decomposition happens with the help of natural agents like sunlight, microorganisms, water, ozone and more which turns it into organic manure.\nThus, these substances are non-toxic to the environment comprising of only natural materials. ')

        else:
            print('No worries')

        print('''BIODEGRADABLE WASTES/MATERIALS/ITEMS CAN BE USED FOR A NUMBER OF THINGS SUCH AS:
                -Manure for crops 
                -Feeds for animals
                -biogas
                -electricity 
                -e.t.c''')

    def biogas(self):
        print('Biogas is a mixture of gases, primarily consisting of methane, carbon dioxide and hydrogen sulphide, produced from raw materials such as agricultural waste, manure, municipal waste, plant material, sewage, green waste, wastewater, and food waste.\nIt is a renewable energy source.')
        webbrowser.open('https://www.youtube.com/watch?v=jgd0t7Z_wHA')
        for r in range(3):
            print('''Here is a list of some Biogas Setup Companies in Uganda:
                    1.Biogas Solutions Uganda Limited 
                    2.Biogas by Tusk Engineers
                    0.exit''')
            select3 = int(input('ENTER CHOICE: '))
            while select3 == '' or select3 > 2:
                select3 = int(input('ENTER CHOICE: '))
            if select3 == 1:
                open = input('WOULD YOU LIKE TO OPEN WEBSITE:(YES/NO): ')
                if open == 'yes' or open == 'YES':
                    webbrowser.open('https://biogassolutions.co.ug/')
                elif open == 'no' or open == 'NO':
                    print('''Plot 36 Luthuli Rise, Bugolobi, P.O.Box 8339 Kampala, Uganda.
                            Toll Free: 0800 399 236
                            Email: info@biogassolutions.co.ug''')
                else:
                    print('invalid input')
            elif select3 == 2:
                open = input('WOULD YOU LIKE TO OPEN WEBSITE:(YES/NO): ')
                if open == 'yes' or open == 'YES':
                    webbrowser.open('https://www.facebook.com/biodigesters/')
                elif open == 'no' or open == 'NO':
                    print('''Box 30335 kla, 256 Kampala, Kampala, Central · ~30.4 km
                                +256 776 422424''')
                else:
                    print('invalid input')
            elif select3 == 0:
                print('\nTHANK YOU FOR USING LUCKY RECYCLE!\n')
                break


class Nonrecyclable_nonBiodegradable(WasteManagement):
    def utilize(self):
        print("For more information on  Non-recyclable and Non-biodegradable waste,Please use our information method")
        print('''Waste that is non recyclable aswell as non biodegradable can be managed by:
            1.Proper Disposal
            2.Use of better environmental friendly alternatives
            3.limiting use''')
        alternate = input(
            'Would you like to look for alternatives to a nonreyclable item(yes/no)?: ')
        while alternate == '':
            alternate = input(
                'Would you like to look for alternatives to a nonreyclable item(yes/no)?: ')

        for t in range(3):
            if alternate == 'yes' or alternate == 'yes':
                google = input('ENTER NAME OF ITEM: ')
                webbrowser.open_new_tab(
                    'https://www.google.com/search?q=' + 'environmentally friendly alternatives for' + google)
            elif alternate == 'no' or alternate == 'NO':
                print('\nTHANK YOU FOR USING LUCKY RECYCLE!\n')
                break


kate = Recyclable()
mary = Nonrecyclable_nonBiodegradable()
kate.call_company()
kate.money_back('0756684725')
