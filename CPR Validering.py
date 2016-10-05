from datetime import datetime
import pickle
cpr = 0
checkDiget = (4, 3, 2, 7, 6, 5, 4, 3, 2, 1)
moduloCheck = False
dateCheck = False
run = True  #while loop for validate
Run = True  #bool for moduleChecck and dateCheck to run
def validate(cpr):
    cpr = input('Indsæt dit cpr dd/mm/åå/xxxx f.eks. 1234567890: ')

    if cpr == 'quit' or cpr == 'exit':
        print('I quit')
        global run
        run = False
        exit()

    if '-' or '/' in cpr:
        cpr = cpr.replace('-', '')
        cpr = cpr.replace('/', '')
    if len(cpr) != 10:
        print('Der skal være 10 cifre i dit CPR nummer')
#       raise Exception("Der skal være 10 tal i dit CPR")
    try:
        int(cpr)
        global Run
        Run = True
    except:
        Run = False
        print('Dit cpr skal bestå af tal')

    if Run == True:
        int(cpr)
        listCpr = list(cpr)
        sumCpr = 0
        for x in range (0,10):
            sumCpr += (checkDiget[x]* int(listCpr[x]))

        #modulo 11 kontrol
        if (sumCpr % 11) != 0:
            global moduloCheck
            moduloCheck = False
        else:
            moduloCheck = True

        #dato kontrol
        global dateCheck
        global year
        global month
        global day
        year = int(cpr[4:6])
        month = int(cpr[2:4])
        day = int(cpr[0:2])
        cpr6 = int(cpr[6])
        if cpr6 <= 3:
            year = year + 1900

        elif cpr6 == 4 and year <= 36:
            year = year + 2000

        elif cpr6 == 4 and year > 36:
            year = year + 1900

        elif 4 < cpr6 < 9 and year <= 57:
            year = year + 2000

        elif 4 < cpr6 < 9 and year > 57:
            year = year + 1800

        elif cpr6 == 9 and year <= 36:
            year = year + 2000

        else:
            year = year + 1900

        try:
            datetime(year, month, day)
            dateCheck = True
        except:
            dateCheck = False
        f = open('log', 'w')
        if moduloCheck == True:
            if dateCheck == True:
                print('Fødselsdato: ' + str(day) + '-' + str(month) + '-' + str(year))
            #køn
                if int(cpr[-1]) % 2 == 0:
                    print('Køn: Kvinde')
                else:
                    print('Køn: Mand')

                print('CPR godkend')
            else:
                print('Invalid CPR')
                f.write('dateCheck error \nThe date does not exist')
                print('dateCheck error')
        else:
            print('Invalid CPR')
            f.write('moduloCheck error \nThe modulo does not mach up with modulo 11')
            print('moduloError')
    f.close()


while run == True:
    validate(cpr)


# print(modulo)
